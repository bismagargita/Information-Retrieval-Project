<!DOCTYPE html>
<html lang="en">
<head>
	<title>Table V01</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
	<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="css/search.css">
	<!--===============================================================================================-->
</head>
<body>
	<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "scraps1";

	$koneksi = new mysqli($servername, $username, $password, $dbname);
	if ($koneksi->connect_error) {
		die("Koneksi Gagal : " . $koneksi->connect_error);
	} 

	$query = "SELECT id_barang, judul, harga, deskripsi FROM produk";
	$result = mysqli_query($koneksi, $query);

	if ($result) {

		?>

		<div class="limiter">
			<div class="container-table100">
				<form class="example" action="action_page.php" style="margin-left: 850px">
					<input type="text" placeholder="Search.." name="search">
					<button type="submit"><i class="fa fa-search"></i></button>
				</form>
				<div class="wrap-table100">
					<div class="table100">
						<table>
							<thead>
								<tr class="table100-head">
									<th class="column1">ID Barang</th>
									<th class="column2">Judul</th>
									<th class="column3">Harga</th>
									<th class="column4" style="text-align: left;">Deskrips</th>
								</tr>
								<?php while ($row = mysqli_fetch_row($result)) { ?>
							</thead>
							<tbody>
								<tr>
									<?php
									$idbarang = $row[0];
									$judul = $row[1];
									$harga = $row[2];
									$deskripsi = $row[3];
									?>
									<td><?php echo $idbarang;?></td>
									<td><?php echo $judul;?></td>
									<td><?php echo $harga;?></td>
									<td><?php echo $deskripsi;?></td>
								</tr>
								<?php } ?>
							</tbody>
						</table>
					</div>
				</div>

				<div class="pagination">
					<a href="#">&laquo;</a>
					<a href="#">1</a>
					<a href="#" class="active">2</a>
					<a href="#">3</a>
					<a href="#">4</a>
					<a href="#">5</a>
					<a href="#">6</a>
					<a href="#">&raquo;</a>
				</div>
			</div>
		</div>




		<!--===============================================================================================-->	
		<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
		<!--===============================================================================================-->
		<script src="vendor/bootstrap/js/popper.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<!--===============================================================================================-->
		<script src="vendor/select2/select2.min.js"></script>
		<!--===============================================================================================-->
		<script src="js/main.js"></script>
		<?php

		mysqli_free_result($result);
	}
	mysqli_close($koneksi);
	?>
</body>
</html>