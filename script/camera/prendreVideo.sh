#!/bin/bash

dateHeure=$(date +"%Y-%m-%d_%H:%M:%S")
enregistrement="$dateHeure.mp4"

raspivid -a 4 -a "%d/%m/%Y %X" -drc med -ex auto -t 60000 -w 1640 -h 1232 -fps 25 -vf -hf -o camera.h264 >> /dev/null

MP4Box -add camera.h264 $enregistrement
mv $enregistrement "video/$enregistrement"

#Système de péremption automatique des vidéos, non-actif, à étudier
#at now+1 month <<< "rm video/$enregistrement"

rm camera.h264
