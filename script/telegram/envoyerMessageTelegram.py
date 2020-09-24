#!/usr/bin/python
# coding: utf-8
#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import sys
import os, os.path
from datetime import datetime
import telegram

def cleAPIbot():
	with open('/var/www/html/script/telegram/cleAPI.txt', 'r') as fichierCleAPI:
		cleAPI = fichierCleAPI.read()
	return cleAPI

#Fonction chargée de l'envoi de message à un utilisateur
def envoyer_message(id_utilisateur, message):
	global bot
	infoExpediteur = bot.getMe()
	infoDestinataire = bot.getChat(id_utilisateur)

	bot.sendMessage(id_utilisateur, message)
	journaliser_message(datetime.now(),infoExpediteur.username,infoExpediteur.id,infoDestinataire.username,infoDestinataire.id,message)

def envoyer_photo(id_utilisateur, chemin_vers_la_photo):
	global bot
	infoExpediteur = bot.getMe()
	infoDestinataire = bot.getChat(id_utilisateur)

	bot.send_photo(id_utilisateur, open(chemin_vers_la_photo, 'rb'))

	message = "[photo: %s]" % chemin_vers_la_photo
	journaliser_message(datetime.now(),infoExpediteur.username,infoExpediteur.id,infoDestinataire.username,infoDestinataire.id,message)

#Fonction servant à enregistrer les activités du chat dans un fichier de log
def journaliser_message(date_envoi,expediteur,id_expediteur,destinataire,id_destinataire,message):
	nomFichierLOG = '/var/www/html/script/telegram/chat.log'

	#On prépare la ligne qui sera enregistrée dans le fichier de log
	entree_journal_log = '"%s","None","%s","%s","%s","%s","%s"\n' % (date_envoi,expediteur,id_expediteur,destinataire,id_destinataire,message)

	#Si le fichier de log n'existe pas, on le créé et on inscrit les titres de colonnes
	if os.path.exists(nomFichierLOG) == False:
		with open(nomFichierLOG,'w') as fichierLOG:
			fichierLOG.write('"Date d\'envoi","Date de réception","Expéditeur","ID expéditeur","Destinataire","ID destinataire","Message"\n')

	#Écriture de l'entrée dans le journal
	with open(nomFichierLOG,'a') as fichierLOG:
		fichierLOG.write(entree_journal_log)

#l'ID de mon compte Telegram (peut être utilisé comme 'chat_id' pour converser en chat privé avec un utilisateur)
id_destinataire = "Something"

#Initialisation du bot avec sa clé API
bot = telegram.Bot(token=cleAPIbot())

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
