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
	else if(type == "pulse") {
		c = new callback(parse_pulse_table, call_error);
		measurements_get_pulses(c);
	}
}
