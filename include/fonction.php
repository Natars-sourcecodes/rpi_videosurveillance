<?php
	function requeteSQL($utilisateur, $motDePasse, $requeteSQL)
	{
		//Connexion à la base de données
		try {
			$bdd = new PDO('mysql:host=localhost;dbname=videosurveillance;charset=utf8', $utilisateur, $motDePasse);
		}
		catch (Exception $e) {
			return $e;
		}

		//Transmission de la requête SQL et récupération des résultats
		$reponseSQL = $bdd->query($requeteSQL);
		$donneeReponseSQL = $reponseSQL->fetchAll();
		$reponseSQL->closeCursor();

		return $donneeReponseSQL;
	}
?>
