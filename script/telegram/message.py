#!/usr/bin/python
# coding: utf-8
#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

from datetime import datetime, timezone
#import telegram
import os

#Fonction chargée de l'envoi de message à un utilisateur
def repondre_texte(update, texte_a_envoyer):
	message = update.message

	#Le texte à envoyer
	message.reply_text(texte_a_envoyer)

	#On créé une nouvelle entrée dans le journal de chat
	bot_username = os.environ.get('TELEGRAM_BOT_USERNAME')
	bot_id = os.environ.get('TELEGRAM_BOT_ID')
	journaliser_message(datetime.now(),None,bot_username,bot_id,message.from_user.username,message.from_user.id,texte_a_envoyer)

#Convertit une date/heure UTC en date/heure locale
def date_utc_vers_local(date_utc):
	date_locale = date_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
	date_locale = date_locale.replace(tzinfo=None)
	return date_locale.replace(microsecond=0)

def journaliser_message_recu(update):
	message = update.message

	#On récupère toutes les infos nécessaire à la fonction "journaliser_message()"
	date_envoi = message.date
	date_reception = datetime.now()
	expediteur = message.from_user.username
	id_expediteur = message.from_user.id
	destinataire = os.environ.get('TELEGRAM_BOT_USERNAME')
	id_destinataire = os.environ.get('TELEGRAM_BOT_ID')
	commandeRecue = message.text

	#Puis on les envoient dans la fonction
	journaliser_message(date_envoi, date_reception, expediteur, id_expediteur, destinataire, id_destinataire, commandeRecue)

#Permet d'enregistrer chaque message reçu ou envoyé dans un fichier de log pour des raisons de contrôle/de surveillance
def journaliser_message(date_envoi,date_reception,expediteur,id_expediteur,destinataire,id_destinataire,message):
	nomFichierLOG = '/var/www/html/script/telegram/chat.log'

	#On formate les date à la date/heure locale
	date_envoi = date_utc_vers_local(date_envoi)
	if date_reception != None:
		date_reception = date_utc_vers_local(date_reception)

	#On prépare la ligne qui sera enregistrée dans le fichier de log
	entree_journal_log = '"%s","%s","%s","%s","%s","%s","%s"\n' % (date_envoi,date_reception,expediteur,id_expediteur,destinataire,id_destinataire,message)

	#Si le fichier de log n'existe pas, on le créé et on ajoute les titres des colonnes
	if os.path.exists(nomFichierLOG) == False:
		with open(nomFichierLOG,'w') as fichierLOG:
			fichierLOG.write('"Date d\'envoi","Date de réception","Expéditeur","ID expéditeur","Destinataire","ID destinataire","Message"\n')

	#Écriture de l'entrée dans le journal
	with open(nomFichierLOG,'a') as fichierLOG:
		fichierLOG.write(entree_journal_log)
