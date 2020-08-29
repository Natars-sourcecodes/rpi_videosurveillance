#!/bin/bash

nombrePhotoPrise=0
nombrePhotoAPrendre=10
dossierSauvegardePhoto='/var/www/html/script/camera/photo/'

#La commande de base à exécuter
commandePhoto="raspistill --rotation 270 -ex auto"

if [[ $# -eq 0 ]]
then
	until [ $nombrePhotoPrise -eq $nombrePhotoAPrendre ]
	do
		#On génère le nom de la photo puis on l'ajoute à la commande
		nomPhoto="$(date +%Y-%m-%d_%H-%M-%S).jpg"
		commandePhoto+=" -o $dossierSauvegardePhoto$nomPhoto"

		#Une fois terminée, on exécute la commande
		$($commandePhoto)

		#On comptabilise la photo prise
		nombrePhotoPrise=$(($nombrePhotoPrise+1))
		#echo "Photo numero $nombrePhotoPrise"
	done
elif [[ $# -eq 1 ]]
then
	sleep 1
fi
