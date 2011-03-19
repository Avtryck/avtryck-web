var avtryck = {
	initMaps : function() {
	    var latlng = new google.maps.LatLng( 62.4007043202567, 17.2577392061653);
	    var myOptions = {
	        zoom: 13,
	        center: latlng,
	        mapTypeId: google.maps.MapTypeId.ROADMAP
	    };
	    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	},
};

function initialize() {
}
$(document).ready(function(){
	avtryck.initMaps();
});
