#!/bin/bash
# A script that takes a URL and sends a message with the a specific header
curl -s -H "X-School-User-Id: 98" "$1"
