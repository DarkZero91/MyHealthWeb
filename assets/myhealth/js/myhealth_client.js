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

function measurement_delete_ecg(id, callback) {
	$.ajax({
		url: URL + "?route=/measurement/ecg/" + id,
		success: callback.success,
		error: callback.error,
		method: "DELETE"
	});
}

function measurement_delete_pulse(id, callback) {
	$.ajax({
		url: URL + "?route=/measurement/pulse/" + id,
		success: callback.success,
		error: callback.error,
		method: "DELETE"
	});
}

function measurement_delete_bloodpressure(id, callback) {
	$.ajax({
		url: URL + "?route=/measurement/bloodpressure/" + id,
		success: callback.success,
		error: callback.error,
		method: "DELETE"
	});
}
