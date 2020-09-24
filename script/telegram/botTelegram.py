#Python Telegram Bot
#Documentation: https://python-telegram-bot.readthedocs.io

import os.path
from datetime import datetime, timezone
from telegram.ext import Updater, CommandHandler

def cleAPIbot():
	with open('cleAPI.txt', 'r') as fichierCleAPI:
		cleAPI = fichierCleAPI.read()
	return cleAPI

#Interruption déclenchée à la réception de nouveau messages
def command_handler(update, context):
	global botActif
	message = update.message
	expediteur = message.from_user.id
	utilisateurValide = utilisateur_autorise(expediteur)
	commandeRecue = message.text

	#On journalise la commande reçue
	journaliserMessage(date_utc_vers_local(message.date),expediteur,utilisateurValide,'bot',commandeRecue,datetime.now())

	if utilisateurValide == True:
		#On détermine l'action à faire en fonction de la commande
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

#Fonction chargée de l'envoi de message standardisé à un utilisateur
def envoyerMessage(update, id_message, *parametre):
	message = update.message
	expediteur = message.from_user.username

	#On envoie le message standard en fonction de l'ID passé en argument
	if id_message == 'activation_bot' :
		messageBot = "Bot activé"

	elif id_message == 'desactivation_bot' :
		messageBot = "Bot désactivé"

	elif id_message == 'statut_bot':
		messageBot = "Le bot est actuellement %s" % parametre[0]

	message.reply_text(messageBot)
	journaliserMessage(datetime.now(),'bot',True,expediteur,messageBot)

#Fonction servant à enregistrer les activités du chat dans un fichier de log
def journaliserMessage(date_envoi,expediteur,expediteur_valide,destinataire,message,date_reception=None):
	nomFichierLOG = 'chat.log'

	#On formate correctement les dates (retrait des millisecondes)
	date_envoi = date_envoi.isoformat(" ","seconds")
	if date_reception != None:
		date_reception = date_reception.isoformat(" ","seconds")

	#On prépare la ligne qui sera enregistrée dans le fichier de log
	entree_journal_log = '"%s","%s","%s","%s","%s","%s"\n' % (date_envoi,date_reception,expediteur,destinataire,message,expediteur_valide)

	#Si le fichier de log n'existe pas, on le créé et on inscrit les titres de colonnes
	if os.path.exists(nomFichierLOG) == False:
		with open(nomFichierLOG,'w') as fichierLOG:
			fichierLOG.write('"Date d\'envoi","Date de réception","Expéditeur","Destinataire","Message","Expéditeur autorisé"\n')

	#Écriture de l'entrée dans le journal
	with open(nomFichierLOG,'a') as fichierLOG:
		fichierLOG.write(entree_journal_log)

#Convertit une date/heure UTC en date/heure locale
def date_utc_vers_local(date_utc):
	date_locale = date_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
	return date_locale.replace(tzinfo=None)

#Vérifie si l'utilisateur spécifié est autorisé à dialoguer avec le bot
def utilisateur_autorise(utilisateurRecherche):
	nomFichierWhitelist = "whitelist.txt"

	#On récupère la liste des utilisateurs autorisés
	with open(nomFichierWhitelist, 'r') as fichierWhitelist:
		listeUtilisateur = fichierWhitelist.readlines()

	for utilisateur in listeUtilisateur:
		#On supprime le '\n' au bout de la ligne
		utilisateur = utilisateur.rstrip()

		#S'il s'agit de l'utilisateur recherché, on renvoie True
		if str(utilisateur) == str(utilisateurRecherche):
			return True

	#Sinon, on renvoie False
	return False

botActif = False
commandesAutorises = ['start','stop', 'statut']

#On essaie de démarrer le bot, en cas d'echec on arrête le script
try:
	#Initialisation de l'updater avec la clé API du bot
	updater = Updater(token=cleAPIbot(), use_context=True)

	#Configuration de la capture d'interruptions par le dispatcher
	dispatcher = updater.dispatcher

	#Ajout des différentes commandes pouvant réagir à l'interruption
	dispatcher.add_handler(CommandHandler(commandesAutorises, command_handler))

	#Démarrage du bot
	updater.start_polling()
	print("Bot démarré, en attente de messages...")

except:
	print("Erreur d'initialisation du bot, arrêt du script")

#Empêche l'arrêt du script jusqu'à réception d'un signal d'arret (SIGINT, ...)
updater.idle()
