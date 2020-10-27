#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import fonctionCommune
import os.path
from datetime import datetime, timezone
from telegram.ext import Updater, CommandHandler

#Interruption declenchee a la reception de nouveau messages
def command_handler(update, context):
	global botActif, infoBot
	message = update.message
	expediteur = message.from_user
	commandeRecue = message.text

	#On journalise la commande recue
	fonctionCommune.journaliser_message_chat(message.date,datetime.now(),expediteur.username,expediteur.id,infoBot.username,infoBot.id,commandeRecue)

	if fonctionCommune.utilisateur_autorise(expediteur.id) == True:
		#On determine l'action a faire en fonction de la commande
		if commandeRecue == '/start' and botActif == False:
			botActif = True
			envoyerMessage(update, 'activation_bot')
			print('Bot activé')

		elif commandeRecue == '/stop' and botActif == True:
			botActif = False
			envoyerMessage(update, 'desactivation_bot')
			print('Bot désactivé')

		elif commandeRecue == '/statut':
			if botActif: statutBot = 'activé'
			else: statutBot = 'désactivé'

			envoyerMessage(update, 'statut_bot', statutBot)

#Fonction chargee de l'envoi de message standardise a un utilisateur
def envoyerMessage(update, id_message, *parametre):
	global infoBot
	message = update.message
	expediteur = message.from_user

	#On envoie le message standard en fonction de l'ID passe en argument
	if id_message == 'activation_bot' :
		messageBot = "Bot activé"

	elif id_message == 'desactivation_bot' :
		messageBot = "Bot désactivé"

	elif id_message == 'statut_bot':
		messageBot = "Le bot est actuellement %s" % parametre[0]

	message.reply_text(messageBot)
	fonctionCommune.journaliser_message_chat(datetime.now(),None,infoBot.username,infoBot.id,expediteur.username,expediteur.id,messageBot)

#Convertit une date/heure UTC en date/heure locale
def date_utc_vers_local(date_utc):
	date_locale = date_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
	return date_locale.replace(tzinfo=None)

botActif = False
commandesAutorises = ['start','stop', 'statut']

#On essaie de démarrer le bot, en cas d'echec on arrete le script
try:
	#Initialisation de l'updater avec la cle API du bot
	cleAPI = fonctionCommune.cle_api_bot()
	updater = Updater(token=cleAPI, use_context=True)

	#On récupères les infos sur le bot
	infoBot = updater.bot

	#Configuration de la capture d'interruptions par le dispatcher
	dispatcher = updater.dispatcher

	#Ajout des differentes commandes pouvant reagir à l'interruption
	dispatcher.add_handler(CommandHandler(commandesAutorises, command_handler))

	#Demarrage du bot
	updater.start_polling()
	print("Bot démarré, en attente de messages...")

except:
	print("Erreur d'initialisation du bot, arrêt du script")

#Empeche l'arret du script jusqu'a reception d'un signal d'arret (SIGINT, ...)
updater.idle()
