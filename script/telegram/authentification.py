#coding: utf-8

import os.path
from datetime import datetime, timezone

#Récupération de la clé API
def cle_api_bot():
	with open('cleAPI.txt', 'r') as fichierCleAPI:
		cleAPI = fichierCleAPI.read()

	return cleAPI

#Permet de rechercher un utilisateur parmis ceux autorisés à dialoguer avec le bot
def utilisateur_autorise(utilisateurRecherche):
	nomFichierWhitelist = "whitelist.txt"

	#On récupère la liste des utilisateurs autorisés
	with open(nomFichierWhitelist,'r') as fichierWhitelist:
		listeUtilisateur = fichierWhitelist.readlines()

	#On supprime le '\n' au bout de chaque lignes
	for utilisateur in listeUtilisateur:
		utilisateur = utilisateur.rstrip()

	#S'il sagit de l'utilisateur recherché, on renvoie True
	if str(utilisateur) == str(utilisateurRecherche):
		return True

	#Sinon, on renvoie False
	return False
