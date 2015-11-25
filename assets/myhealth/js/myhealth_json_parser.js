function callback(success, error) {
	this.success = success;
	this.error = error;
}

var call_error = function() { alert("De metingen konden niet worden opgevraagd. Probeer het later nogmaals."); }

var parse_pulse_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("hartslag"),
			$("<th>").text("datum")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/pulse-small.png"})),
			$("<td>").text(item.heartrate + " bpm"),
			$("<td>").text(item.created)
		);
		$("#measurement-table").append($tr);
	});
};
