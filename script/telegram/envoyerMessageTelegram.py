#!/usr/bin/python
# coding: utf-8
#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import fonctionCommune
import sys
import os, os.path
from datetime import datetime
import telegram

#Fonction chargée de l'envoi de message à un utilisateur
def envoyer_message(id_utilisateur, message):
	global bot
	infoExpediteur = bot.getMe()
	infoDestinataire = bot.getChat(id_utilisateur)

	bot.sendMessage(id_utilisateur, message)
	fonctionCommune.journaliser_message_chat(datetime.now(),None,infoExpediteur.username,infoExpediteur.id,infoDestinataire.username,infoDestinataire.id,message)

#Fonction chargée de l'envoi d'une photo à un utilisateur
def envoyer_photo(id_utilisateur, chemin_vers_la_photo):
	global bot
	infoExpediteur = bot.getMe()
	infoDestinataire = bot.getChat(id_utilisateur)

	bot.send_photo(id_utilisateur, open(chemin_vers_la_photo, 'rb'))

	message = "[photo: %s]" % chemin_vers_la_photo
	fonctionCommune.journaliser_message_chat(datetime.now(),None,infoExpediteur.username,infoExpediteur.id,infoDestinataire.username,infoDestinataire.id,message)

#Fonction chargée de l'envoi d'une vidéo à un utilisateur
def envoyer_video(id_utilisateur, chemin_vers_la_video):
	global bot
	infoExpediteur = bot.getMe()
	infoDestinataire = bot.getChat(id_utilisateur)

	bot.send_video(id_utilisateur, open(chemin_vers_la_video, 'rb'))

	message = "[video: %s]" % chemin_vers_la_video
	fonctionCommune.journaliser_message_chat(datetime.now(),None,infoExpediteur.username,infoExpediteur.id,infoDestinataire.username,infoDestinataire.id,message)

#l'ID de mon compte Telegram (peut être utilisé comme 'chat_id' pour converser en chat privé avec un utilisateur)
id_destinataire = "something"

try:
	print("Démarrage")
	print(fonctionCommune.cle_api_bot())

	#Initialisation du bot avec sa clé API
	bot = telegram.Bot(token=fonctionCommune.cle_api_bot())

except:
	print("Erreur de lancement du script")
	exit()

#On contrôle les arguments reçus et on adopte le comportement adapté
if len(sys.argv) > 2: #Contrôle du nombre d'argument reçus (arg. n°1: titre du script, arg. n°2: type d'action à réaliser, arg. n°3,4,...: paramètres nécessaire à la fonction )

	#Message texte
	if sys.argv[1] == "texte":
		envoyer_message(id_destinataire,sys.argv[2])

	#Photo (une ou plusieurs)
	if sys.argv[1] == "photo":
		#On supprime les deux 1ers éléments du tableau (nom du script et l'argument "photo")
		del sys.argv[0:2]

		#Il ne nous reste alors que la liste des photos à envoyer, on boucle alors dessus
		for photo in sys.argv:
			envoyer_photo(id_destinataire,str(photo))

	#Vidéo (une ou plusieurs)
	if sys.argv[1] == "video":
		del sys.argv[0:2]

		for video in sys.argv:
			envoyer_video(id_destinataire,str(video))
