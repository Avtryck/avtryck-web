var avtryck = {
	map: null,
	dummyMarkers : [],
	initMaps : function() {
	    var latlng = new google.maps.LatLng( 62.4008043502567, 17.2977392061653);
	    var myOptions = {
	        zoom: 13,
	        center: latlng,
	        mapTypeId: google.maps.MapTypeId.ROADMAP
	    };
	    avtryck.map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	},
	addDummyMarkers: function() {
		avtryck.addDummyKsamsokMarker(62.3836481160038, 17.3333119676816, 'null', 'raa_bbr_21400000693943');
		avtryck.addDummyKsamsokMarker(62.3996202575523, 17.2618420788935, 'GRANLO KYRKA', 'raa_bbr_21400000616710');
		avtryck.addDummyKsamsokMarker(62.4190855258784, 17.3362275270045, 'BOSVEDJANS KYRKA', 'raa_bbr_21400000616740');
		avtryck.addDummyKsamsokMarker(62.4109397374185, 17.2694914938053, 'GRANLOHOLMS KYRKA', 'raa_bbr_21400000549775');
		avtryck.addDummyKsamsokMarker(62.3607875626007, 17.5297456868143, 'SPIKARÖ KAPELL', 'raa_bbr_21400000616830');
		avtryck.addDummyKsamsokMarker(62.4644256356746, 17.3882819404034, 'Stensättning', 'raa_fmi_10244800110003');
		avtryck.addDummyKsamsokMarker(62.4657588656219, 17.3964194530288, 'Fornlämningsliknande lämning', 'raa_fmi_10244800280002');
		avtryck.addDummyKsamsokMarker(62.4567809258391, 17.3999276520954, 'Hög', 'raa_fmi_10244800380001');
		avtryck.addDummyKsamsokMarker(62.4643602366912, 17.4015059301616, 'Boplats', 'raa_fmi_10244800870003');
		avtryck.addDummyKsamsokMarker(62.4641964863965, 17.4337512411666, 'Labyrint', 'raa_fmi_10244801040001');
		avtryck.addDummyKsamsokMarker(62.4293546988075, 17.4859839044074, 'Lägenhetsbebyggelse', 'raa_fmi_10244801150001');
		avtryck.addDummyKsamsokMarker(62.3163274371633, 17.0484627285143, 'Hög', 'raa_fmi_10245100120001');
		
	},
	addDummyKsamsokMarker: function(plat, plong, name, id) {
		new google.maps.Marker({
		      position: new google.maps.LatLng(plat,plong),
		      title:name,
			  map: avtryck.map,
			  icon: "images/marker_white.jpg"
		  });
	},
	addPlaceMarkers: function() {
		/*
        loc1.setLatitude(62.4007043202567);
        loc1.setLongitude(17.2577392061653);
        place1.setGeoLocation(loc1);

        Location loc2 = new Location("se.tidensavtryck");
        loc2.setLatitude(62.394369903217); 
        loc2.setLongitude(17.2816450479837);
        place2.setGeoLocation(loc2);

        Location loc3 = new Location("se.tidensavtryck");
        loc3.setLatitude(62.3897829867526); 
        loc3.setLongitude(17.2995418371631);
        place3.setGeoLocation(loc3);
        
        Location loc4 = new Location("se.tidensavtryck");
        loc4.setLatitude(62.391178326117); 
        loc4.setLongitude(17.3004228024664);
        place4.setGeoLocation(loc4);
		*/

		places = [
			{plat: 62.4007043202567, plong:17.2577392061653, name: "place1"},
			{plat: 62.394369903217, plong:17.2816450479837, name: "place2"},
			{plat: 62.3897829867526, plong:17.2995418371631, name: "place3"},
			{plat: 62.391178326117, plong:17.3004228024664, name: "place4"},
		];
		
		routeLatLongs = [];
		for (var pi=0; pi<4; pi++) {
			p = places[pi];
			seq = pi+1;
			iconColor = "FF5cA4";
			if (pi==0) {
				iconColor = "FF1c54";
			} 
			icon = "http://thydzik.com/thydzikGoogleMap/markerlink.php?color="+iconColor+"&text="+seq
			pos = new google.maps.LatLng(p.plat,p.plong),
			new google.maps.Marker({
			      position: pos,
			      title:p.name,
				  map: avtryck.map,
				  icon: icon,
			  });
			routeLatLongs.push(pos);
		}
		
	  var routePath = new google.maps.Polyline({
	    path: routeLatLongs,
	    strokeColor: "#FF0000",
	    strokeOpacity: 1.0,
	    strokeWeight: 2,
		map: avtryck.map,
	  });
	}
};

function initialize() {
}
$(document).ready(function(){
	avtryck.initMaps();
	avtryck.addDummyMarkers();
	avtryck.addPlaceMarkers();
	
});
