var map;
L.mapbox.accessToken = 'pk.eyJ1IjoiZGViYWtlbCIsImEiOiJjMWVJWEdFIn0.WtaUd8Rh0rgHRiyEZNzSjQ';

window.onload = loadMap();
function loadMap() {
    // Karte laden
    map = L.map('map').setView([48.2633321, 10.8405515], 13);
    L.mapbox.tileLayer('mapbox.comic', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'debakel.in6i4ino',
        accessToken: 'pk.eyJ1IjoiZGViYWtlbCIsImEiOiJjMWVJWEdFIn0.WtaUd8Rh0rgHRiyEZNzSjQ'
    }).addTo(map);

    L.control.locate().addTo(map);
   

    // Märkte holen
    var template_source = $("#market-template").html();
    var template = Handlebars.compile(template_source);

    function onEachFeature(feature, layer) {
        var context = feature.properties;
        var html = template(context);
        var popup = L.popup({minWidth: 333 }).setContent(html);
        layer.bindPopup(popup);
        $(html).find("button").on("click", function (event) {
            alert($(this).attr("dumpster-id"));
        });
    }

    $.ajax({
        url: "http://localhost:5001/dumpster/all",
        cache: false
    })
        .done(function (response) {
            L.geoJson(JSON.parse(response), {onEachFeature: onEachFeature}).addTo(map);
        });
}


function vote(id, voting) {
    $.ajax("http://localhost:5001/dumpster/vote/" + id + "/" + voting);
}

$(document).on('click', '.btn_vote', function () {
    vote($(this).attr('dumpster-id'), $(this).attr('voting'));
});
