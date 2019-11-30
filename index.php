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

						foreach($listeEnregistrement as $enregistrement)
						{
							if($enregistrement != '.' && $enregistrement != '..')
							{
								echo '<p>';
								echo "$enregistrement";
								echo '<\p>';
							}
						}

					?>
				</div>
			</div>
			<?php include("include/footer.php") ?>
		</div>
	</div>
    </body>
</html>
