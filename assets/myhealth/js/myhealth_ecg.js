$(document).ready(function() {
	c = new callback(
		function(data) { parse_data(data); },
		call_error
	);
	measurements_get_ecg($("#id").text(), c);	
});

function parse_data(response) {
	response = $.parseJSON(response);
	$("#created").text(response.created);

	values = response.data.split(",");
	labels = [];
	
	for(i = 0; i < values.length; i++) { labels.push(""); }
	
	datasets = [];
	datasets[0] = {
		label: "ECG Measurement",
		fillColor: "rgba(151,187,205,0.2)",
		strokeColor: "rgba(151,187,205,1)",
		pointColor: "rgba(151,187,205,1)",
		pointStrokeColor: "#fff",
		pointHighlightFill: "#fff",
		pointHighlightStroke: "rgba(151,187,205,1)",
		data: values
		};

	build_chart({labels: labels, datasets: datasets});
}

function build_chart(data) {
	var options = {
		responsive: true,
		maintainAspectRatio: true
	}
	
	var ctx = $("#ecg-chart").get(0).getContext("2d");
	var myLineChart = new Chart(ctx).Line(data, options);
}