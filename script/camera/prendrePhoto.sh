#!/bin/bash

nombrePhotoPrise=0
nombrePhotoAPrendre=5
dossierSauvegardePhoto='/var/www/html/script/camera/photo'

commandePhoto="raspistill --rotation 270 -ex auto -ae 128,0xff,0x0808000 -a 12 "

if [[ $# -eq 0 ]]
then
	listePhoto=""
	until [ $nombrePhotoPrise -eq $nombrePhotoAPrendre ]
	do
		nomPhoto="$(date +%Y-%m-%d_%H-%M-%S).jpg"
		commandePhotoAExecuter+="$commandePhoto -o $dossierSauvegardePhoto/$nomPhoto"
		$($commandePhotoAExecuter)

		nombrePhotoPrise=$(($nombrePhotoPrise+1))
		listePhoto+="$dossierSauvegardePhoto/$nomPhoto "
	done

	echo $listePhoto

elif [[ $# -eq 1 && $1 == "telegram" ]]
then
	#Si une photo est demandée par le bot Telegram, on l'identifie pour qu'il la trouve
	nomPhoto="telegram.jpg"
	commandePhoto+="-o $dossierSauvegardePhoto/$nomPhoto"
	$($commandePhoto)
fi
