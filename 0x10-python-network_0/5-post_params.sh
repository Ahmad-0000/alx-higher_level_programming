#!/bin/bash
# A script that taskes a URL and sends a client method with "POST" method
curl -X POST -d "email=test@gmial.com&subject=I+will+always+be+here+for+PLD" "$1"
