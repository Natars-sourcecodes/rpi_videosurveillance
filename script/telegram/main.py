#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import authentification, commande
import os, os.path
from telegram.ext import Updater, CommandHandler

#Interruption declenchee a la reception de nouveau messages
def command_handler(update, context):

	#Dès réception d'une commande, on vérifie que l'expéditeur est autorisé.
	#S'il l'est, on traite la commande
	if authentification.utilisateur_autorise(update.message.from_user.id) == True:
		commande.traiter_commande(update)


#On essaie de démarrer le bot, en cas d'echec on arrete le script
try:
	#Initialisation de l'updater avec la cle API du bot
	cleAPI = authentification.cle_api_bot()
	updater = Updater(token=cleAPI, use_context=True)

	#On stocke les infos sur le bot
	os.environ['TELEGRAM_BOT_USERNAME'] = updater.bot.username
	os.environ['TELEGRAM_BOT_ID'] = str(updater.bot.id)
	os.environ['TELEGRAM_BOT_ACTIF'] = 'False'

	#Configuration de la capture d'interruptions par le dispatcher
	dispatcher = updater.dispatcher

	#Ajout des differentes commandes pouvant reagir à l'interruption
	dispatcher.add_handler(CommandHandler(commande.get_commande_active(), command_handler))

	#Demarrage du bot
	updater.start_polling()
	print("Bot démarré, en attente de messages...")

except:
	print("Erreur d'initialisation du bot")
	print("Erreur: %s" % sys.exc_info()[0])
	exit()

#Empeche l'arret du script jusqu'a reception d'un signal d'arret (SIGINT, ...)
updater.idle()
