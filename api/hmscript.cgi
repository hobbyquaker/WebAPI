#!/bin/tclsh

#   hmscript.cgi
#   Ausf�hren eines Homematic Scripts
#   2'2013 https://github.com/hobbyquaker
#
#   Erwartet das Ausgabeformat im Querystring sowie ein Homematic Script als POST Daten
#   M�gliche Ausgabeformate: xml, json, html, plain
#       Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen,
#       die Ausgabe selbst muss im TCL Script eigenst�ndig erzeugt werden.
#   Beispielaufruf: hmscript.cgi?content=json
#
#   Debug-Modus: ein Aufruf mit hmscript.cgi?debug=true erzeugt eine Ausgabe die alle Variablen beinhaltet
#


load tclrega.so

set debug "false"
set content "plain"

proc escape { str } {
  set jsonmap {
    "\"" "\\\""
    "\\" "\\\\"
    "\b"  "\\b"
    "\f"  "\\f"
    "\n"  "\\n"
    "\r"  "\\r"
    "\t"  "\\t"
  }

  return "[string map $jsonmap $str]"
}

proc utf8-decode str {
  set utfmap {
   "ä" "�"
   "ö" "�"
   "ü" "�"
   "Ä" "�"
   "Ö" "�"
   "Ü" "�"
   "ß" "�"
  }
  return "[string map $utfmap $str]"
}

proc init {} {
    variable map
    variable alphanumeric a-zA-Z0-9
    for {set i 0} {$i <= 256} {incr i} {
        set c [format %c $i]
        if {![string match \[$alphanumeric\] $c]} {
            set map($c) %[format %.2x $i]
        }
    }
    # These are handled specially
    array set map { " " + \n %0d%0a }
}
init

proc url-decode str {
    set str [string map [list + { } "\\" "\\\\"] $str]
    regsub -all -- {%([A-Fa-f0-9][A-Fa-f0-9])} $str {\\u00\1} str
    return [subst -novar -nocommand $str]
}

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname [utf8-decode $val]
    }
  }
}

puts "Content-Type: text/$content;Charset=ISO-8859-1"
puts "Access-Control-Allow-Origin: *"
puts ""


append postdata [utf8-decode [read stdin]]

array set script_result [rega_script $postdata]




if {$debug == "true"} {
    set first 1

    switch $content {
        json {
            set result "\{"
            foreach name [array names script_result] {
                if {1 != $first} {append result ","} {set first 0}
                set value $script_result($name)
                append result "\"[escape $name]\":\"[escape $value]\""
            }
            append result "\}"
        }
        xml {
            set result "<xml><exec>hmscript.cgi</exec>"
            foreach name [array names script_result] {
                set value $script_result($name)
                append result "<$name>[escape $value]</$name>"
            }
            append result "</xml>"

        }
        plain {
            foreach name [array names script_result] {
                if {1 != $first} {append result "\n"} {set first 0}
                set value $script_result($name)
                append result "$name = \"[escape $value]\""
            }
        }
        html {
            foreach name [array names script_result] {
                if {1 != $first} {append result "<br>"} {set first 0}
                set value $script_result($name)
                append result "$name = \"$value\""
            }
        }
    }



    puts $result
} else {
    puts $script_result(STDOUT)
}

