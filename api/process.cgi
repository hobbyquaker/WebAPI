#!/bin/tclsh

#   process.cgi
#   Ausführen eines Prozesses
#   2'2013 https://github.com/hobbyquaker
#
#



load tclrega.so

proc escape { str } {
  set map {
    "\"" "\\\""
    "\\" "\\\\"
    "\b"  "\\b"
    "\f"  "\\f"
    "\n"  "\\n"
    "\r"  "\\r"
    "\t"  "\\t"
  }
  return "[string map $map $str]"
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

set debug "false"
set content "plain"
set session ""
set process "/bin/sh"

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname [url-decode $val]
    }
  }
}

set script [read stdin]
set ausgabe ""
set fehler ""

puts "Content-Type: text/$content;Charset=ISO-8859-1"
puts "Access-Control-Allow-Origin: *"
puts ""

append script "\nexit"
set pipe [open "|$process" r+]
puts $pipe $script
catch {flush $pipe}
while {[gets $pipe this] >= 0} {
    append ausgabe $this
    append ausgabe "\n"
}
if {[catch {close $pipe} stderr] != 0} {
    append fehler $stderr
}

if {$debug == "false"} {
    puts $ausgabe
} else {
    switch $content {
        json {
            puts -nonewline "{\"STDOUT\":\"[escape $ausgabe]\",\"STDERR\":\"[escape $fehler]\"}"
        }
        xml {
            puts -nonewline "<?xml version=\"1.0\"?><response><STDOUT>[escape $ausgabe]</STDOUT><STDERR>[escape $fehler]</STDERR></response>"
        }
        html {
            puts "<html><h3>STDOUT</h3><p>[escape $ausgabe]</p><h3>STDERR</h3><p>[escape $fehler]</p></html>"
        }
        plain {
            puts "STDOUT:"
            puts $ausgabe
            puts ""
            puts "STDERR:"
            puts $fehler
        }
    }
}

