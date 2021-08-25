// custom delay function
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

$(document).ready(function(){
	$("#search_by_university").click(function(){
		$("#navbardrop").html("Search by Univesity");

		$("#search_by_country_form").hide();
		$("#search_by_university_form").show();
	});

	$("#search_by_country").click(function(){
		$("#navbardrop").html("Search by Country");

		$("#search_by_university_form").hide();
		$("#search_by_country_form").show();
	});
})