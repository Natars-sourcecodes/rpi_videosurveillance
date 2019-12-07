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

					<h1>Paramétrage de la caméra</h1>
		
					<!-- IMAGE CAMERA -->

					<form method="post" action="parametre.php">
						<table>
							<tr>
								<td>
									<label><h2>Finesse de l'image</h2></label>
									<input type="range" name="finesse" min="-100" max="100" step="1" />
								</td>
								<td>
									<label><h2>Contraste</h2></label>
									<input type="range" name="contraste" min=-100" max="100" step="1" />
								</td>
								
								<td>
									<label><h2>Luminosité</h2></label>
									<input type="range" name="luminosite" min="0" max="100" step="1" />
								</td>
								<td>
									<label><h2>Saturation</h2></label>
									<input type="range" name="contraste" min="-100" max="100" step="1" />
								</td>
							</tr>
							<tr>
								<td>
									<label><h2>ISO</h2></label>
									<input type="range" name="iso" min="100" max="800" step="1" />
								</td>
								<td>
									<label><h2>Compensation de la luminosité</h2></label>
									<input type="range" name="compensationLuminosite" min="-10" max="10" step="1" />
								</td>
								<td>
									<label><h2>Mode d'exposition</h2></label>
								</td>
								<td>
									<label><h2>Balance des blancs</h2></label>
								</td>
							</tr>
							<tr>
								<td>
									<label><h2>Effet</h2></label>
								</td>
								<td>
									<label><h2>Rotation</h2></label>
									<input type="range" name="sharpness" min="-100" max="100" step="1" />
								</td>
								<td>
									<label><h2>Retournement horizontal</h2></label>
								</td>
								<td>
									<label><h2>Retournement vertical</h2></label>
								</td>
							</tr>
						</table>
					</form>

				</div>
			</div>
			<?php include("include/footer.php") ?>
		</div>
	</div>
    </body>
</html>
