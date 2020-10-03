#!/bin/bash

#Génération du nom du fichier de sortie
dateHeure=$(date +"%Y-%m-%d_%H:%M:%S")
enregistrement="$dateHeure.mp4"

#Enregistrement de la vidéo
raspivid -a 4 -a "%d/%m/%Y %X" -drc med -ex auto -t 120000 -w 1640 -h 1232 -fps 25 --rotation 270 -o camera.h264 >> /dev/null

#Conversion en MP4 et déplacement dans le dossier adéquat
MP4Box -add camera.h264 $enregistrement >> /dev/null
mv $enregistrement "video/$enregistrement"

#Indication du nom du fichier de sortie
echo "video/$enregistrement"

#Système de péremption automatique des vidéos, non-actif, à étudier
#at now+1 month <<< "rm video/$enregistrement"

rm camera.h264
