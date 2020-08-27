#!/bin/bash

nombrePhotoPrise=0
nombrePhotoAPrendre=10

until [ $nombrePhotoPrise -eq $nombrePhotoAPrendre ]
do
	raspistill --rotation 270 -ex auto -o /var/www/html/script/camera/photo/$(date +"%Y-%m-%d_%H:%M:%S").jpg >> /dev/null
	nombrePhotoPrise=$(($nombrePhotoPrise+1))
	#echo "Photo numero $nombrePhotoPrise"
done
