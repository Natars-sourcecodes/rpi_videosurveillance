#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import sys
import os, os.path
from datetime import datetime, timezone
import telegram

def cleAPIbot():
	with open('cleAPI.txt', 'r') as fichierCleAPI:
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
	nomFichierLOG = 'chat.log'

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
id_destinataire = "something"

#Initialisation du bot avec sa clé API
bot = telegram.Bot(token=cleAPIbot())

print(str(sys.argv))

#On contrôle les arguments reçus et on adopte le comportement adapté
if len(sys.argv) > 2: #Contrôle du nombre d'argument reçus (argument n°1: titre du script)
	if sys.argv[1] == "texte":
		envoyer_message(id_destinataire,sys.argv[2])
	if sys.argv[1] == "photo":
		envoyer_photo(id_destinataire,sys.argv[2])
