<?php error_reporting(E_ALL); ini_set("display_errors", 1); #A supprimer dès que la page fonctionne ?>
<?php date_default_timezone_set('Europe/Paris'); ?>
<!DOCTYPE html>
<html>
    <?php include("include/header.php"); ?>
    <?php include("include/fonction.php"); ?>
    <body>
	<div class="main">
		<div class="container">
			<div class="gfx"><a href="index.php"><span></span></a></div>
			<?php include("include/menu.php"); ?>

			<div class="content">
				<div class="item">
					<h1>Liste des enregistrements<br /></h1>

					<!-- FORMULAIRE DE FILTRAGE DES ENREGISTREMENT PAR DATE -->
					<form method="post" action="index.php">
						<label for="intervalle">Afficher les enregistrements depuis: <label>
						<select name="intervalle" id="intervalle">
							<?php
//Connexion à la base de données et récupération des choix disponibles
								$reponseSQL = requeteSQL('', '', 'SELECT choix, nomChoix AS "titre" FROM choixMenuDeroulant WHERE menu = "intervalle"', array());
								foreach($reponseSQL as $optionMenu)
								{ //Pour chaque résultat, on génère une option dans le menu déroulant
									echo "<option value=".$optionMenu['choix'].">".$optionMenu['titre']."</option>";
								}
							?>
						</select>
						<input type="submit" value="Filtrer" />
					</form>

					<!-- SCRIPT D'ANALYSE DU FORMULAIRE DE FILTRAGE -->
					<?php
						if(isset($_POST['intervalle']))
						{
							//On compte le nombre de fois que où le choix de l'utilisateur apparaît
							//La table ne contenant aucun doublon, la valeur 1 est retournée si le choix est référencé, 0 dans le cas contraire

							$requeteSQL = 'SELECT count(choix) AS "resultat", nomChoix AS "titre" FROM choixMenuDeroulant WHERE menu = "intervalle" AND choix = :intervalle';
							$reponseSQL = requeteSQL('', '', $requeteSQL, array('intervalle' => $_POST['intervalle']));

							foreach($reponseSQL as $occurence){
								if($occurence['resultat'] == 1) { //En cas de validation du choix de l'utilisateur, on complète les variables avec les paramètres correspondants
									$intervalleMax = $_POST['intervalle'];
									$filtrage = $occurence['titre'];
								}
								else { //Si aucune occurence est trouvé, on applique le filtrage par défaut (càd aucun)
									$intervalleMax = -1;
									$filtrage = "Aucun";
								}	
							}
						}
						else
						{
							$intervalleMax = -1; //Par défaut, aucun filtrage
							$filtrage = 'Aucun';
						}

								echo '<br />Filtrage actuel: '.$filtrage;

						//Listing des fichiers présents dans le dossier "camera"
						$listeEnregistrement = scandir('./camera');

						//Listing des fichiers restants une fois le fitrage fait
						$listeEnregistrementFiltre = array();

						foreach($listeEnregistrement as $fichier)
						{ //On calcule l'intervalle de temps entre la dernière modification de chaque fichier et maintenant
							if($fichier != '.' && $fichier != '..')
							{
								$dateDerniereModification = filemtime('./camera/'.$fichier);
								$intervalleDerniereModification = time() - $dateDerniereModification;

								if($intervalleDerniereModification <= $intervalleMax OR $intervalleMax == -1)
								{ //Les fichiers valides sont mis dans un tableau spécifique
									array_unshift($listeEnregistrementFiltre, $fichier);
								}
							}
							sort($listeEnregistrementFiltre);
						}
						
						//Affichage de la liste des enregistrements dans un tableau
						echo '<table><tr class="enregistrement">';
						$nombreColonneTableau = 2;

						$numeroColonne = 0; //Numéro de colonne où va être positionné l'élément
						foreach($listeEnregistrementFiltre as $enregistrement)
						{
							if($enregistrement != '.' && $enregistrement != '..')
							{
								if($numeroColonne >= $nombreColonneTableau)
								{ //Si toutes les colonnes d'une ligne sont remplies, on passe à la suivante
									echo '</tr><tr class="enregistrement">';
									$numeroColonne = 0;
								}
									echo '<td>';
								echo '<h2>'.date("d/m/Y H:i:s", filemtime('./camera/'.$enregistrement)).'</h2>';
								echo '<video src="camera/'.$enregistrement.'" controls preload=none width=440>Erreur de lecture de la vidéo</video></br >';
								echo '<a href="camera/'.$enregistrement.'">Télécharger la vidéo</a>';
								echo '</td>';
								$numeroColonne++; //On passe à la colonne suivante
							}
						}
						echo '</tr></table>';
						?>
				</div>
			</div>
			<?php include("include/footer.php") ?>
		</div>
	</div>
    </body>
</html>
