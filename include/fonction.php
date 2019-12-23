<?php
	function requeteSQL($utilisateur, $motDePasse, $requeteSQL, $listeParametreRequeteSQL)
	{
		//Connexion à la base de données
		try {
			$bdd = new PDO('mysql:host=localhost;dbname=videosurveillance;charset=utf8', $utilisateur, $motDePasse);
		}
		catch (Exception $e) {
			return $e;
		}

		//Préparation de la requête SQL (plus sécurisé face aux risque d'injection SQL) et transmission du tableau de variable passé en argument
		$reponseSQL = $bdd->prepare($requeteSQL);
		$reponseSQL->execute($listeParametreRequeteSQL);


		$donneeReponseSQL = $reponseSQL->fetchAll();
		$reponseSQL->closeCursor();

		return $donneeReponseSQL;
	}
?>
