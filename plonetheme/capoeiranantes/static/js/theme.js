function updateSearchBox(){
	$('#livesearch0 .searchSection').remove();
}
function equalHeight(group) {
	var tallest = 0;
	group.each(function() {
		var thisHeight = $(this).height();
		if(thisHeight > tallest) {
			tallest = thisHeight;
		}
	});
	group.height(tallest);
}
function initializeplonethemecapoeiranantes(){
    updateSearchBox();
}
jQuery(initializeplonethemecapoeiranantes);
