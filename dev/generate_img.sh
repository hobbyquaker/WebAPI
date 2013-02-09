#!/bin/sh
rm -r tmp
mkdir -p tmp/webapi

cp -a api/* tmp/webapi/
cp dev/update_script tmp/
cp dev/webapi tmp/
cd tmp
tar -czvf ../webapi.tar.gz *
