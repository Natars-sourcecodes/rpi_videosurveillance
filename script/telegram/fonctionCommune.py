import os.path
from datetime import datetime

#Récupération de la clé API
def cle_api_bot():
	with open('cleAPI.txt', 'r') as fichierCleAPI:
		cleAPI = fichierCleAPI.read()

	return cleAPI

#Convertit une date/heure UTC en date/heure locale
def date_utc_vers_local(date_utc):
	date_locale = date_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
	return date_local.replace(tzinfo=None)

#Permet de rechercher un utilisateur parmis ceux autorisés à dialoguer avec le bot
def utilisateur_autorise(utilisateurRecherche):
	nomFichierWhitelist = "whitelist.txt"

	#On récupère la liste des utilisateurs autorisés
	with open(nomFichierWhitelist,'r') as fichierWhitelist:
		listeUtilisateur = fichierWhitelist.readlines()

	#On supprime le '\n' au bout de chaque lignes
	for utilissateur in listeUtilisateur:
		utilisateur = utilisateur.rstrip()

	#S'il sagit de l'utilisateur recherché, on renvoie True
	if str(utilisateur) == str(utilisateurRecherche):
		return True

	#Sinon, on renvoie False
	return False

def journaliser_message_chat(date_envoi,date_reception,expediteur,id_expediteur,destinataire,id_destinataire,message):
	nomFichierLOG = '/var/www/html/script/telegram/chat.log'

	#On prépare la ligne qui sera enregistrée dans le fichier de log
	entree_journal_log = '"%s","%s","%s","%s","%s","%s","%s"\n' % (date_envoi,date_reception,expediteur,id_expediteur,destinataire,id_destinataire,message)

	#Si le fichier de log n'existe pas, on le créé et on ajoute les titres des colonnes
	if os.path.exists(nomFichierLOG) == False:
		with open(nomFichierLOG,'w') as fichierLOG:
			fichierLOG.write('"Date d\'envoi","Date de réception","Expéditeur","ID expéditeur","Destinataire","ID destinataire","Message"\n')

	#Écriture de l'entrée dans le journal
	with open(nomFichierLOG,'a') as fichierLOG:
		fichierLOG.write(entree_journal_log)
