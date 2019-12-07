<?php error_reporting(E_ALL); ini_set("display_errors", 1); #A supprimer dès que la page fonctionne ?>
<?php date_default_timezone_set('Europe/Paris'); ?>
<!DOCTYPE html>
<html>
    <?php include("include/header.php"); ?>

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
							<option value=-1 selected>------</option>
							<option value=24>1 jour</option>
							<option value=12>12 heures</option>
							<option value=4>4 heures</option>
							<option value=2>2 heures</option>
							<option value=1>1 heure</option>
							<option value=0.5>30 minutes</option>
							<option value=0.25>15 minutes</option>
						</select>
						<input type="submit" value="Filtrer" />
					</form>

					<!-- SCRIPT D'ANALYSE DU FORMULAIRE DE FILTRAGE -->
					<?php
						if(isset($_POST['intervalle']))
						{
							switch ($_POST['intervalle'])
							{
								case -1:
									$intervalleMax = -1;
									$filtrage = 'Aucun';
								break;

								case 24:
									$intervalleMax = 86400;
									$filtrage = '1 jour';
								break;

								case 12:
									$intervalleMax = 43200;
									$filtrage = '12 heures';
								break;

								case 4:
									$intervalleMax = 14400;
									$filtrage = '4 heures';
								break;

								case 2:
									$intervalleMax = 7200;
									$filtrage = '2 heures';
								break;

								case 1:
									$intervalleMax = 3600;
									$filtrage = '1 heure';
								break;

								case 0.5:
									$intervalleMax = 1800;
									$filtrage = '30 minutes';
								break;

								case 0.25:
									$intervalleMax = 900;
									$filtrage = '15 minutes';
								break;

								default:
									$intervalleMax = -1; //filtrage 1h si choix non-valide
									$filtrage = 'aucun';
							}
						}
						else
						{
							$intervalleMax = -1; //Par défaut, aucun filtrage
							$filtrage = 'aucun';
						}

						echo '<br />Filtrage actuel: '.$filtrage;

						//Listing des fichiers présents dans le dossier "camera"
						$listeEnregistrement = scandir('./camera');

						//Listing des fichiers restants une fois le fitrage fait
						$listeEnregistrementFiltre = array();

						foreach($listeEnregistrement as $fichier)
						{ //On calcule l'intervalle de temps entre la dernièrem modification de chaque fichier et maintenant
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
