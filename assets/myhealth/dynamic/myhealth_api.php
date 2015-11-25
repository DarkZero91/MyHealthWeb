<?php
	$url = "http://jeroenhoekstra.no-ip.org:5000" . $_GET['route'];
	
	if($_SERVER["REQUEST_METHOD"] == "GET") {
		echo file_get_contents($url);
	}
	else if($_SERVER["REQUEST_METHOD"] == "DELETE") {
		$opts =  array("http" => array("method" => "delete"));
		$context = stream_context_create($opts);
		echo file_get_contents($url, false, $context);
	}
?>