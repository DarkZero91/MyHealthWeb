var URL = "http://jeroenhoekstra.no-ip.org/myhealth/assets/myhealth/dynamic/myhealth_api.php";

function measurements_get_ecgs(callback) {
	$.ajax({
		url: URL + "?route=/measurement/ecgs",
		success: callback.success,
		error: callback.error,
		method: "GET"
	});
}

function measurements_get_pulses(callback) {
	$.ajax({
		url: URL + "?route=/measurement/pulses",
		success: callback.success,
		error: callback.error,
		method: "GET"
	});
}

function measurements_get_bloodpressures(callback) {
	$.ajax({
		url: URL + "?route=/measurement/bloodpressures",
		success: callback.success,
		error: callback.error,
		method: "GET"
	});
}
