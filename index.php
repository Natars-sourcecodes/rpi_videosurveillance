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
					
					<form method="post" action="index.php">
						<label for="temps">Intervalle d'affichage des enregistrements: <label>
						<select name="temps" id="temps">
							<option value="1j">1 jour</option>
							<option value="4h">4 heures</option>
							<option value="2h">2 heures</option>
							<option value="1h">1 heure</option>
							<option value="30min">30 minutes</option>
							<option value="15min">15 minutes</option>
						</select>
					</form>

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
