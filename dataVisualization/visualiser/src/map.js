import ('https://api.mapbox.com/mapbox-gl-js/v1.4.1/mapbox-gl.js');
mapboxgl.accessToken = 'pk.eyJ1IjoiaGFzc2Fuc2VuanUiLCJhIjoiY2szN2JtNzk4MDl5cTNjamx4cmQ5eXN5OCJ9.YwEZ5rUmNDEmJy3bCCcDPg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v9',
    center: [57.7, 11.9],
    zoom: 10
});
document.getElementById("fly").addEventListener("click", function() {
    map.flyTo({
        center: [57.7089, 11.9746]
    })
});