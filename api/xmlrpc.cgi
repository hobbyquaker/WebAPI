#!/bin/tclsh

#   xmlrpc.cgi
#   Proxy für Zugriff auf XMLRPC via Port 80
#   11'2012 https://github.com/hobbyquaker
#
#
#   Erwartet den Zielport (2000,2001,2002) im Querystring
#       Beispielaufruf: xmlrpc.cgi?port=2001
#

load tclrega.so

set port "2000"
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

set postdata [read stdin]


package require http
set url "http://127.0.0.1:$port/"
set token [::http::geturl $url -query $postdata]
set response [::http::data $token]
puts "Access-Control-Allow-Origin: *"
puts ""
puts $response

