
$(document).ready(function(){
	
	// case-insensitive table search functionality
	$("#search").on("keyup", function() {
    	var value = $(this).val().toLowerCase();
    	$("#table tr").filter(function() {
      		$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    	});
  	});	
})