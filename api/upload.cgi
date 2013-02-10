#!/bin/tclsh

#
#   upload.cgi
#   2'2013 https://github.com/hobbyquaker
#
#
#

source /www/config/cgi.tcl
load tclrega.so

set file ""
set path ""
set overwrite "false"

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname $val
    }
  }
}

cgi_eval {

    cgi_input

    cgi_content_type "text/plain"
    cgi_http_head

    cgi_import "file"

    set tmpfile "/var"
    append tmpfile [lindex $file 0]
    set filename [lindex $file 1]
    set mimetype [lindex $file 2]
    set newfile $path
    append newfile $filename

    puts $tmpfile
    puts $newfile

    if {$overwrite == "true"} {
        file rename -force -- $tmpfile $newfile
    } else {
        file rename -- $tmpfile $newfile
    }

}