#!/bin/tclsh

#   tclscript.cgi
#   Ausführen eines TCL Scripts
#   11'2012 https://github.com/hobbyquaker
#
#   Erwartet das Ausgabeformat im Querystring sowie ein TCL Script als POST Daten
#   Mögliche Ausgabeformate: xml, json, html, plain
#       Diese Angabe dient lediglich dazu einen passenden Header und passende Fehlermeldungen zu erzeugen,
#       die Ausgabe selbst muss im TCL Script eigenständig erzeugt werden.
#   Beispielaufruf: tclscript.cgi?content=json
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

set content "plain"
set session ""

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname $val
    }
  }
}

puts "Content-Type: text/$content;Charset=ISO-8859-1"
puts "Access-Control-Allow-Origin: *"
puts ""

if { [catch {
  set postdata [read stdin]
  eval $postdata
} errorMessage] } {
    switch $content {
    json {
        puts "{error:{source:\"tcl\",message:\"[escape $errorMessage]\"}}"
    }
    xml {
        puts -nonewline {<?xml version="1.0"?><response><error source="tcl" message="}
        puts -nonewline [escape $errorMessage]
        puts {"/></response>}
    }
    html {
        puts "<html><h3>TCL error: $errorMessage</h3></html>"
    }
    plain {
        puts "TCL error: $errorMessage"
        }
    }
}
