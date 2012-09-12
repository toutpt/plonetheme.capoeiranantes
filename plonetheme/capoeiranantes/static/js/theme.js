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
		console.log(category)
		var cssclass = null;
		if (category.match("adultes")=="adultes"){
			cssclass = "adulte";
		}
		if (category.match("jeunes")=="jeunes"){
			cssclass = "jeune";
		}
		if (category.match("enfants")=="enfants"){
			cssclass = "enfant"
		}
		if (category.match("ados")=="ados"){
			cssclass = "ado"
		}
		if (cssclass != null){
			$(value).addClass(cssclass);
		}
	})
	$('#myDiv1>p')
	$('.template-folder_full_view .addthis_toolbox:last').detach().prependTo('#content-core');
}
jQuery(initializeplonethemecapoeiranantes);
