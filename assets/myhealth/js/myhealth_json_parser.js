function callback(success, error) {
	this.success = success;
	this.error = error;
}

var call_error = function() { alert("De metingen konden niet worden opgevraagd. Probeer het later nogmaals."); }

var parse_pulse_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
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

var parse_ecg_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("nummer"),
			$("<th>").text("datum")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/ecg-small.png"})),
			$("<td>").text(item.id),
			$("<td>").text(item.created)
		);
		$("#measurement-table").append($tr);
	});
}

var parse_bloodpressure_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("bloeddruk"),
			$("<th>").text("datum")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/bloodpressure-small.png"})),
			$("<td>").text(item.over + "/" + item.under),
			$("<td>").text(item.created)
		);
		$("#measurement-table").append($tr);
	});
}
