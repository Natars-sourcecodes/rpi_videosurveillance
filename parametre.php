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

					<h1>Paramétrage de la caméra</h1>
		
					<!-- IMAGE CAMERA -->

					<form method="post" action="parametre.php">
						<table>
							<tr>
								<td>
									<label><h2>Mode d'exposition</h2></label>
										<select name="exposition" id="exposition">
										<?php
											$requeteSQL = 'SELECT choix, nomChoix AS "titre" FROM choixMenuDeroulant WHERE menu = "parametreCameraExposition"';
											$resultat = requeteSQL('', '', $requeteSQL, array());
											
											foreach ($resultat as $optionMenuDeroulant) {
												echo "<option value=".$optionMenuDeroulant['choix'].">".$optionMenuDeroulant['titre']."</option>";
											}
										?>
									</select>

								</td>
								<td>
<label><h2>Balance des blancs</h2></label>
									<select name="balanceBlanc" id="balanceBlanc">
										<?php
											$requeteSQL = 'SELECT choix, nomChoix AS "titre" FROM choixMenuDeroulant WHERE menu = "parametreCameraBalanceBlanc"';
											$resultat = requeteSQL('', '', $requeteSQL, array());
											
											foreach ($resultat as $optionMenuDeroulant) {
												echo "<option value=".$optionMenuDeroulant['choix'].">".$optionMenuDeroulant['titre']."</option>";
											}
										?>
									</select>

								</td>
								<td>
									<label><h2>Effet</h2></label>
									<select name="effet" id="effet">
										<?php
											$requeteSQL = 'SELECT choix, nomChoix AS "titre" FROM choixMenuDeroulant WHERE menu = "parametreCameraEffet"';
											$resultat = requeteSQL('', '', $requeteSQL, array());
											
											foreach ($resultat as $optionMenuDeroulant) {
												echo "<option value=".$optionMenuDeroulant['choix'].">".$optionMenuDeroulant['titre']."</option>";
											}
										?>
									</select>
								</td>
								<?php
									//On récupère la liste des curseurs à générer
									$requeteSQL = 'SELECT nomCurseur AS nom, titreCurseur AS titre, minimum, maximum, pas, valeurParDefaut FROM curseurFormulaire WHERE formulaire = "parametreCamera"';
									$resultat = requeteSQL('', '', $requeteSQL, array());

									$numeroColonne = 3; //Le nombre d'éléments déjà présents dans le tableau de paramétrages

									//Pour chaque entrée du tableau, on génère un curseur
									foreach ($resultat as $curseur) {
										//On limite le tableau à quatre élément par ligne: dès que cette limite est atteinte, on change de ligne
										if ($numeroColonne == 4) {
											echo '</tr><tr>'; 
											$numeroColonne = 0;
										}	
										$numeroColonne++;

										echo "<td>";
										echo "<label><h2>".$curseur['titre']."</h2></label>";
										echo '<input type="range" name='.$curseur['nom'].' min='.$curseur['minimum'].' max='.$curseur['maximum'].' step='.$curseur['pas'].' value='.$curseur['valeurParDefaut'].' />';
										echo "</td>";
									}
									$requeteSQL = 'SELECT nom, titre, valeurParDefaut FROM caseACocher WHERE formulaire = "parametreCamera"';
									$resultat = requeteSQL('', '', $requeteSQL, array());

									foreach ($resultat as $caseACocher) {
										echo '<td>';
										echo '<label><h2>'.$caseACocher['titre'].'</h2></label><br />';
										if ($caseACocher['valeurParDefaut']) {
											echo '<span class="long"><input type="checkbox" name='.$caseACocher['nom'].' id='.$caseACocher['nom'].' checked /></span>';
										}
										else {
											echo '<span class="long"><input type="checkbox" name='.$caseACocher['nom'].' id='.$caseACocher['nom'].' /></span>';
										}
										echo '</td>';
									}
								?>
							</tr>
						</table>
						<input type="submit" value = "Valider les réglages">
						<input type="reset" value = "Réinitialiser les réglages">
					</form>

				</div>
			</div>
			<?php include("include/footer.php") ?>
		</div>
	</div>
    </body>
</html>
