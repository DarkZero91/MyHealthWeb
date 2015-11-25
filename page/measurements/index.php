<!DOCTYPE html>
<html lang="en">
	<head>
		<?php include_once($_SERVER['DOCUMENT_ROOT'] . "/myhealth/assets/myhealth/widgets/head.php"); ?>
	</head>
	<body>
		<?php include_once($_SERVER['DOCUMENT_ROOT'] . "/myhealth/assets/myhealth/widgets/navigation.php"); ?>
		
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12">
					<ul class="nav nav-tabs">
						<li id="ecg" class="measurement-tab active"><a href="#">Ecg</a></li>
						<li id="bloodpressure" class="measurement-tab"><a href="#">Bloeddruk</a></li>
						<li id="pulse" class="measurement-tab"><a href="#">Hartslag</a></li>
					</ul>
					<table id="measurement-table" class="table"></table>
				</div>
			</div>
		</div>
	</body>
</html>