# coding: utf-8
#Script contenant l'ensemble des commandes que le bot sait traiter

import message
import os

def start(update):
	os.environ['TELEGRAM_BOT_ACTIF'] = 'True'
	message.repondre_texte(update, "Bot activé")

def stop(update):
	os.environ['TELEGRAM_BOT_ACTIF'] = 'False'
	message.repondre_texte(update, "Bot désactivé")

def statut(update):
	if os.environ.get('TELEGRAM_BOT_ACTIF') == 'True':
		message_a_envoyer = "Bot actif"
	else:
		message_a_envoyer = "Bot inactif"

	message.repondre_texte(update, message_a_envoyer)

#On créé un dictionnaire dans lequel sont listées les commandes actives
#Elles sont associé à la fonction correspondantes définie ci-dessus
commandeActive = {}
commandeActive['start'] = start
commandeActive['stop'] = stop
commandeActive['statut'] = statut

#Fonction principal, permet de traiter une commande reçue par le bot
def traiter_commande(update):
	#On commence par journaliser le nouveau message reçu sur le chat
	message.journaliser_message_recu(update)

	#On récupère la commande et lui supprime son '/'
	commandeRecue = update.message.text
	commandeRecue = commandeRecue[1:]

	#On essaie de lancer la fonction correspondante
	#On renvoie le resultat via un booléen:
	#
	#	True => ça fonctionne à merveille
	#	False => commande inconnue/désactivée
	#
	try:
		commandeActive[commandeRecue](update)
		return True

	except KeyError:
		return False

#Renvoie la liste des commandes actives
def get_commande_active():
	return commandeActive.keys()
