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
    $('.flexslider').flexslider({
    	directionNav: false,
    	controlNav: false,
    	keyboardNav: false
    });
    $('.container').fitVids();
    $('.section-cours-de-capoeira #content-core table td').each(function(index, value){
		var category = $(value).text().toLowerCase();
		var cssclass = null;
		if (category.match("^"+"adulte")=="adulte"){
			cssclass = "adulte";
		}
		if (category.match("^"+"enfant")=="enfant"){
			cssclass = "enfant";
		}
		if (cssclass != null){
			$(value).addClass(cssclass);
		}
	})
}
jQuery(initializeplonethemecapoeiranantes);
