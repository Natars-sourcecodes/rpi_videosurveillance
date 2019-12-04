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
								echo '<video src="camera/'.$enregistrement.'" controls width=320>Erreur de lecture de la vidéo</video><br />';
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
