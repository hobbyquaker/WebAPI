#!/bin/sh
rm -r tmp
mkdir -p tmp/webapi

cp -a webapi_auth/* tmp/webapi/
cp dev/update_script tmp/
cp dev/hq-webapi_auth tmp/
cd tmp
tar -czvf ../webapi_auth.tar.gz *
