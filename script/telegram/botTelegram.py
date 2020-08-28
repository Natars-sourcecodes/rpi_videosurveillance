import os.path
import time
import datetime
import telepot
from telepot.loop import MessageLoop

"""
After **inserting token** in the source code, run it:

```
$ python2.7 diceyclock.py
```

[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:

- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""
#Interruption dans laquelle vont etre traites les commandes recues
def handle(msg):
	chat_id = msg['chat']['id']
	commande = msg['text']
	expediteur = msg['from']['username']

	#On verifie en premier lieu si l'expediteur a le droit ou non
	#d'executer des commandes
	expediteurAutorise = verifierExpediteur(expediteur)

	#On journalise toutes les commandes recues
	journaliserMessage(expediteur, commande, expediteurAutorise)

	#Si oui, on traite alors la commande recue, sinon on l'ignore
	if expediteurAutorise == True:
		traiterCommande(chat_id, commande)

"""
		#Envoi d'une photo prise maintenant (provisoirement test.jpg)
		if commande == '/photo':
			bot.sendPhoto(chat_id, photo=open('test.jpg', 'rb'))
"""

#Permet d'enregistrer la commande recue dans un fichier de log
def journaliserMessage(expediteur, commandeRecue, utilisateurAutorise):
	nomFichierLog = "commandes.log"

	if os.path.exists(nomFichierLog) != True:
		with open(nomFichierLog, "w") as fichierLog:
			fichierLog.write('"Date et heure de l\'evenement","Utilisateur","Commande","Commande autorisee"\n')

	#On prepare ce qui sera ecrit dans le fichier de log
	texteAEcrire = '"%s","%s","%s","%s"\n' % (str(datetime.datetime.now()), expediteur, commandeRecue, utilisateurAutorise)

	#On ecrit la nouvelle entree ci-dessus
	with open(nomFichierLog, "a") as fichierLog:
		fichierLog.write(texteAEcrire)

#Permet de controller que l'expediteur est autorise a communiquer avec le bot
def verifierExpediteur(expediteurRecherche):
	nomFichierExpediteurAutorise = "whitelist.txt"
	expediteurTrouve = False

	#On recupere la liste les expediteurs autorises
	with open(nomFichierExpediteurAutorise, "r") as fichierExpediteurAutorise:
		listeExpediteur = fichierExpediteurAutorise.readlines()

	#Pour chacun des expediteurs, on supprime le "\n" et on verifie s'il s'agit
	#de l'utilisateur recherche
	for expediteur in listeExpediteur:
		expediteur = str(expediteur.rstrip())

		#Si trouve, on modifie le booleen dedie
		if expediteur == expediteurRecherche:
			expediteurTrouve = True

	return expediteurTrouve

def traiterCommande(chat_id, commande):
	global botActif

	#Modification de l'etat d'activite du bot
	if commande == '/start':
		botActif = True
		bot.sendMessage(chat_id, "Bonjour\nVous pouvez desormais m'envoyer des commandes")
		print 'Bot actif'

	elif commande == '/stop':
		botActif = False
		bot.sendMessage(chat_id, 'A bientot')
		print 'Bot inactif'

	#Commandes traites seulement si le bot est actif
	if botActif == True:
		if commande == '/test':
			bot.sendMessage(chat_id, 'Bonjour')

		if commande == '/photo':
			#Declenchement du script de prise de photo

#Declaration du bot avec sa cle API
bot = telepot.Bot('')

#Declaration de l'interruption
MessageLoop(bot, handle).run_as_thread()
print 'En attente de commandes...'



#variable botActif	==>	Booleen permettant de definir l'etat du bot

#False			==>	Ne traite aucune commande
#True			==>	Traite les commande recues
#/start et /stop	==>	Permet d'activer ou non le bot

botActif = False

while 1:
	try:
		time.sleep(10)

	except KeyboardInterrupt:
		print 'A bientot'
		exit()
