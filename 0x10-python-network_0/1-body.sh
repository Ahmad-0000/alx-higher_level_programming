#!/bin/bash
# A script to show the body of the response message with status code 200
status="$(curl -sI -f "$1" | head -1 | cut -d ' ' -f 2)"; if [ "$status" == "200" ] ; then curl -s "$1"; fi
