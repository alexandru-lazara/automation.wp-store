#!/bin/bash

_directory=docker/nginx
_validity=3650
_hostname=automation.wp.local

cd $_directory || { echo "Unable to change directory."; exit 1; }
if [ -d ssl ]; then
  cd ssl
  rm -f *.pem
else
  mkdir ssl
  cd ssl
fi

openssl req \
  -x509 \
  -outform pem \
  -out chain.pem \
  -keyout privkey.pem \
  -newkey rsa:4096 \
  -nodes \
  -sha256 \
  -days $_validity \
  -subj "//CN=$_hostname"

if [ -f chain.pem ] && [ -f privkey.pem ]; then
  echo "SSL certificates generation successful."
else
  rm -f *.pem
  echo "SSL certificates generation failed."
fi
