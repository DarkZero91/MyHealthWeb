$(document).ready(function() {
	$(".measurement-tab").click(function() {
		id = $(this).attr("id");
		$(".measurement-tab.active").removeClass("active");
		$(this).addClass("active");
		get_data(id);		
	});
});

function get_data(type) {
	if(type == "pulse") {
		c = new callback(parse_pulse_table, call_error)
		measurements_get_pulses(c);
	}
}