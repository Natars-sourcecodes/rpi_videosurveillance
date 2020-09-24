#!/usr/bin/python coding: utf-8
import os

#On verifie que la bibliotheque necessaire soit installee
try:
	import RPi.GPIO as GPIO

except:
	print("RPi.GPIO non installe, veuillez taper la commande suivante pour l'installer:")
	print("sudo apt install rpi.gpio")
	exit()

#Fonction declenchee a chaque detection
def presenceDetecte():
	scriptEnvoiMessageTelegram = '/var/www/html/script/telegram/envoyerMessageTelegram.py'

	#On recupere la liste des noms des photos realisees
	stream = os.popen('bash prendrePhoto.sh')
	listePhoto = stream.read()
	listePhoto = listePhoto.rstrip()

	#On envoie les photos via le bot Telegram
	os.system("/usr/bin/python3 %s photo %s" % (scriptEnvoiMessageTelegram, str(listePhoto)))

### CODE PRINCIPAL ###

pinBCM_capteurPIR = 4

try:
	#Parametrage de la pin utilisee par le capteur PIR
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pinBCM_capteurPIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	print("Caméra prête")

	while True:
		#En attente d'une detection (d'un front montant(0->1) sur la pin du capteur PIR)
		GPIO.wait_for_edge(pinBCM_capteurPIR, GPIO.RISING)
		presenceDetecte()

except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
