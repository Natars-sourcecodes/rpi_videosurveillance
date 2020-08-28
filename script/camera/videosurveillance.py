# coding=utf-8

import RPi.GPIO as GPIO
import os
import time

brocheCapteurPIR = 4
presenceDetecte = False
enregistrementVideo = False # True = vidéo ; False = photo
nombreLigneAffichee = 25
nombreMaxLigneAffichee = 24

def init():
	# Définition de la broche sur laquelle est connecté le capteur PIR
	# et création de l'interruption

	GPIO.setmode(GPIO.BCM) #BOARD = n° de broche, BCM = nom de la broche
	GPIO.setup(brocheCapteurPIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #GPIO 4 en entrée

def prendrePhoto(): os.system('bash /var/www/html/script/camera/prendrePhoto.sh 2>&1 /dev/null')
def prendreVideo(): os.system('bash /var/www/html/script/camera/prendreVideo.sh 2>&1 /dev/null')
def alerteIFTTT(): os.system('bash /var/www/html/script/camera/envoyerAlerteIFTTT.sh 2>&1 /dev/null')

if __name__ == '__main__':
	init()

	while True:
		if nombreLigneAffichee >= nombreMaxLigneAffichee:
			os.system('clear')
			print('Pour quitter: CTRL + MAJ + ANTISLASH\n')
			nombreLigneAffichee = 1

		#En attente d'un front montant (= nouvelle détection)
		GPIO.wait_for_edge(brocheCapteurPIR, GPIO.RISING)

		alerteIFTTT()
		now = time.strftime("%d/%m/%Y %H:%M")
		if enregistrementVideo == False:
			prendrePhoto()
			print(now + ": Nouvelle enregistrement photo")
			nombreLigneAffichee += 1
		else:
			prendreVideo()
                        print(now + ": Nouvelle enregistrement video")
                        nombreLigneAffichee += 4
	pass
