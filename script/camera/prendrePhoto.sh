#!/bin/bash

nombrePhotoPrise=0
nombrePhotoAPrendre=10
dossierSauvegardePhoto='/var/www/html/script/camera/photo'

commandePhoto="raspistill --rotation 270 -ex auto "

if [[ $# -eq 0 ]]
then
	until [ $nombrePhotoPrise -eq $nombrePhotoAPrendre ]
	do
		nomPhoto="$(date +%Y-%m-%d_%H-%M-%S).jpg"
		commandePhoto+="-o $dossierSauvegardePhoto/$nomPhoto"
		$($commandePhoto)
		nombrePhotoPrise=$(($nombrePhotoPrise+1))
		#echo "Photo numero $nombrePhotoPrise"
	done
elif [[ $# -eq 1 && $1 == "telegram" ]]
then
	#Si une photo est demandée par le bot Telegram, on l'identifie pour qu'il la trouve
	nomPhoto="telegram.jpg"
	commandePhoto+="-o $dossierSauvegardePhoto/$nomPhoto"
	$($commandePhoto)
fi
