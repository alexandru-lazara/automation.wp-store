#!/bin/bash

echo ""

echo "Automation Testing for containerized Wordpress Store"
echo ""

echo "SSL certificates are Generating..."
echo ""
./generate-ssl.sh
echo ""

echo "Docker Setup is Starting..."
echo ""
docker-compose up -d
echo ""
