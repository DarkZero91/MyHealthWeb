function callback(success, error) {
	this.success = success;
	this.error = error;
}


function add_delete_click_listener() {
	$(".delete").click(function() {
		id = $(this).data("id");
		type = $(".measurement-tab.active").attr("id");
		if(confirm("Weet u zeker dat u de meting wilt verwijderen?")) {
			remove(id, type);
		}
	});
}

var call_error = function() { alert("De metingen konden niet worden opgevraagd. Probeer het later nogmaals."); }

var parse_pulse_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("hartslag"),
			$("<th>").text("datum"),
			$("<th>")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/pulse-small.png"})),
			$("<td>").text(item.heartrate + " bpm"),
			$("<td>").text(item.created),
			$("<td>").append($("<a>").data("id", item.id).attr({class: "delete"}).append($("<span>").attr({class: "glyphicon glyphicon-trash"})))
		);
		$("#measurement-table").append($tr);
	});
	add_delete_click_listener();
};

var parse_ecg_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("nummer"),
			$("<th>").text("datum"),
			$("<th>")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/ecg-small.png"})),
			$("<td>").text(item.id),
			$("<td>").text(item.created),
			$("<td>").append($("<a>").data("id", item.id).attr({class: "delete"}).append($("<span>").attr({class: "glyphicon glyphicon-trash"})))
		);
		$("#measurement-table").append($tr);
	});
	add_delete_click_listener();
}

var parse_bloodpressure_table = function(data) {
	response = $.parseJSON(data);
	$("#measurement-table").empty().append(
		$("<tr>").append(
			$("<th>").width(24),
			$("<th>").text("bloeddruk"),
			$("<th>").text("datum"),
			$("<th>")
		)
	);
	$.each(response, function(i, item) {
		var $tr = $("<tr>").append(
			$("<td>").append($("<img>").attr({src: "/myhealth/assets/myhealth/img/bloodpressure-small.png"})),
			$("<td>").text(item.over + "/" + item.under),
			$("<td>").text(item.created),
			$("<td>").append($("<a>").data("id", item.id).attr({class: "delete"}).append($("<span>").attr({class: "glyphicon glyphicon-trash"})))
		);
		$("#measurement-table").append($tr);
	});
	add_delete_click_listener();
}
