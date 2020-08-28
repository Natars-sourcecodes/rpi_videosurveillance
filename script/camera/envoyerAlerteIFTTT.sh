#!/bin/bash

date=$(date +"%d/%m/%Y %H:%M:%S")
curl -X POST -H "Content-Type: application/json" -d '{"value1":"test"}' https://maker.ifttt.com/trigger/presence_detecte/with/key/[something]
