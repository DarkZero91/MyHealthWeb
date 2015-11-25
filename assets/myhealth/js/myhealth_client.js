var URL = "http://jeroenhoekstra.no-ip.org/myhealth/assets/myhealth/dynamic/myhealth_api.php";

function measurements_get_pulses(callback) {
	$.ajax({
		url: URL + "?route=/measurement/pulses",
		success: callback.success,
		error: callback.error,
		method: "GET"
	});
}

