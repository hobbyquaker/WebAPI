#!/bin/tclsh

#
#   Proxy für HTTP POST an beliebige URLs
#
#   2'2013 https://github.com/hobbyquaker
#


load tclrega.so

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  set first 1
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname $val
      if {$varname == "hmwa_urls"} {
        set url "$val?"

      } else {
        append querystring "$varname=$val"
      }
      set first 0
    }
  }
}
append url $querystring
set postdata [read stdin]


package require http

set token [::http::geturl $url -query $postdata]
set response [::http::data $token]
puts "Access-Control-Allow-Origin: *"
puts ""
puts $response

