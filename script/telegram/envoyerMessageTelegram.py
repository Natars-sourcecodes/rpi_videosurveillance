#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

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
	bot.sendMessage(id_utilisateur, message)

#Fonction servant à enregistrer les activités du chat dans un fichier de log
def journaliser_message(date_envoi,expediteur,expediteur_valide,destinataire,id_destinataire,message):
	nomFichierLOG = 'chat.log'

	#On prépare la ligne qui sera enregistrée dans le fichier de log
	entree_journal_log = '"%s","None","%s","%s","%s","%s"\n' % (date_envoi,expediteur,destinataire,message,expediteur_valide)

	#Si le fichier de log n'existe pas, on le créé et on inscrit les titres de colonnes
	if os.path.exists(nomFichierLOG) == False:
		with open(nomFichierLOG,'w') as fichierLOG:
			fichierLOG.write('"Date d\'envoi","Date de réception","Expéditeur","Destinataire","Message","Expéditeur autorisé"\n')

	#Écriture de l'entrée dans le journal
	with open(nomFichierLOG,'a') as fichierLOG:
		fichierLOG.write(entree_journal_log)

#l'ID de mon compte Telegram (peut être utilisé comme 'chat_id' pour converser en chat privé avec un utilisateur)
ID_destinataire = "something"

#Initialisation du bot avec sa clé API
bot = telegram.Bot(token=cleAPIbot())

envoyer_message(ID_destinataire,"test")

#Commandes de test
print(bot.getChat(ID_destinataire).username)
print(bot.getMe())
