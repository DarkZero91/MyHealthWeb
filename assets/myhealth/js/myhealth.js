$(document).ready(function() {
	get_data("ecg");

	$(".measurement-tab").click(function() {
		id = $(this).attr("id");
		$(".measurement-tab.active").removeClass("active");
		$(this).addClass("active");
		get_data(id);		
	});
});

function get_data(type) {
	if(type == "ecg") {
		c = new callback(parse_ecg_table, call_error);
		measurements_get_ecgs(c);
	}
	else if(type == "bloodpressure") {
		c = new callback(parse_bloodpressure_table, call_error);
		measurements_get_bloodpressures(c);
	}
	else if(type == "pulse") {
		c = new callback(parse_pulse_table, call_error);
		measurements_get_pulses(c);
	}
}

function remove(id, type) {
	if(type == "ecg") {
		c = new callback(function(data) { get_data("ecg"); }, call_error);
		measurement_delete_ecg(id, c);
	}
	else if(type == "bloodpressure") {
		c = new callback(function(data) { get_data("bloodpressure"); }, call_error);
		measurement_delete_bloodpressure(id, c);
	}
	else if(type == "pulse") {
		c = new callback(function(data) { get_data("pulse"); }, call_error);
		measurement_delete_pulse(id, c);
	}
}
