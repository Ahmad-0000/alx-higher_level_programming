#!/bin/bash
# A script to use "OPTIONS" http method on a client message
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
