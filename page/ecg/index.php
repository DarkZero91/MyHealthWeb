<!DOCTYPE html>
<html lang="en">
	<head>
		<?php include_once($_SERVER['DOCUMENT_ROOT'] . "/myhealth/assets/myhealth/widgets/head.php"); ?>
	</head>
	<body>
		<?php include_once($_SERVER['DOCUMENT_ROOT'] . "/myhealth/assets/myhealth/widgets/navigation.php"); ?>
		
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-2">
					<img src="/myhealth/assets/myhealth/img/ecg.png" /><br />
					<br />
					<table class="table table-striped">
						<tr>
							<th>nummer</th>
							<td id="id"><?php echo $_GET["id"]; ?></td>
						</tr>
						<tr>
							<th>datum</th>
							<td id="created"></td>
						</tr>
					</table>
				</div>
				<div class="col-md-9">
					<canvas id="ecg-chart"></canvas>
				</div>
			</div>
		</div>
		<script src="/myhealth/assets/myhealth/js/myhealth_ecg.js"></script>
	</body>
</html>