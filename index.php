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
						<label for="intervalle">Intervalle d'affichage des enregistrements: <label>
						<select name="intervalle" id="intervalle">
							<option value=24>1 jour</option>
							<option value=12>12 heures</option>
							<option value=4>4 heures</option>
							<option value=2>2 heures</option>
							<option value=1 selected>1 heure</option>
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
								case 24:
									$intervalle = "1j";
								break;

								case 12:
									$intervalle = "12h";
								break;

								case 4:
									$intervalle = "4h";
								break;

								case 2:
									$intervalle = "2h";
								break;

								case 1:
									$intervalle = "1h";
								break;

								case 0.5:
									$intervalle = "30min";
								break;

								case 0.25:
									$intervalle = "15min";
								break;

								default:
									$intervalle = "1h";
							}
						}
					?>

					<!-- SCRIPT D'AFFICHAGE DES ENREGISTREMENTS -->
					<?php
						//Listing des fichiers présents dans le dossier "camera"
						$listeEnregistrement = scandir('./camera');

						//Affichage de la liste des enregistrements dans un tableau
						echo '<table><tr>';
						$nombreColonneTableau = 2;

						$nombreElementTableau = count($listeEnregistrement); //On compte le nombre d'éléments du tableau
						$nombreElementTableau -= 2; //On décompte le '.' et le '..' de la liste des éléments

						$nombreLigneTableau = intdiv($nombreElementTableau, $nombreColonneTableau);
						if(($nombreElementTableau % $nombreColonneTableau) > 0) //On détermine le nombre de ligne du tableau
						{
							$nombreLigneTableau++; //Si besoin, on rajoute une ligne pour mettre les éléments restants
						}

						$numeroColonne = 0; //Numéro de colonne où va être positionné l'élément
						foreach($listeEnregistrement as $enregistrement)
						{
							if($enregistrement != '.' && $enregistrement != '..')
							{
								if($numeroColonne >= $nombreColonneTableau)
								{ //Si toutes les colonnes d'une ligne sont remplies, on passe à la suivante
									echo "</tr><tr>";
									$numeroColonne = 0;
								}
									echo '<td>';
								echo '<h2>'.date("d/m/Y H:i:s", filemtime('./camera/'.$enregistrement)).'</h2>';
								echo '<video src="camera/'.$enregistrement.'" controls width=440>Erreur de lecture de la vidéo</video><br />';
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
