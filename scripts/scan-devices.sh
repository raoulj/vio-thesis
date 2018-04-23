#!/bin/bash

# We need to strip the whitespace from the hostname
computer_ip="$(echo "$(hostname -I)" | tr -d '[:space:]')"

# Query the router for the connected devices.
# This is specific to the Card-King AC 1200M Wireless Router
# Need to be connected to server for this to run properly.
content=$(curl -s -X POST 'http://192.168.0.1/protocol.csp?fname=system&opt=main&function=get' -H 'Content-Length: 0' --compressed)

# Parse the JSON, make an array out of it.
data=($(jq '.terminals[].ip' <<< "${content}"))

for i in "${data[@]}"
do
    temp="${i%\"}"
    temp="${temp#\"}"
    if [ ${#temp} -ge 3 ] && [ $temp != $computer_ip ] 
    then
        echo "$temp"
    fi
done