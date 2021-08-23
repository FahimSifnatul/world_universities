
$(document).ready(function(){
	
	$("#search_by_university").click(function(){
		$("#search_by_country_form").hide();
		$("#search_by_university_form").show();

		$("#navbardrop").html("Search by University <span class='fas fa-caret-down'></span>");
	});

	$("#search_by_country").click(function(){
		$("#search_by_university_form").hide();
		$("#search_by_country_form").show();

		$("#navbardrop").html("Search by Country <span class='fas fa-caret-down'></span>");
	});
})