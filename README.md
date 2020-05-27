⛤ Traffic Visualizer ⛤

A university project designed by: 

<a href="https://github.com/malties"> <img src="https://avatars1.githubusercontent.com/u/43722564?s=460&v=4" width="17" height="17"> Hannah Maltkvist</a> <br/>
<a href="https://github.com/nafenk"> <img src="https://avatars0.githubusercontent.com/u/44115545?s=460&v=4" width="17" height="17"> Nafen Haj Ahmad</a> <br/>
<a href="https://github.com/Gusmuaha"> <img src="https://avatars2.githubusercontent.com/u/43820542?s=460&v=4" width="17" height="17"> Hassan Mualla</a> <br/>
<a href="https://github.com/Shab98"> <img src="https://avatars2.githubusercontent.com/u/45070337?s=460&v=4" width="17" height="17"> Shab Pompeiano</a>



 Stanko Janković, Adelric Wong, 

Features:
*  Easy to use Traffic Visualizer Interface
*  View walking routes, bus routes and bottlenecks in the Gothenburg area 
*  Navigation control: Zoom in/out on map, switch map view
*  pasue and unpause lines showing up in the map


Purpose:
*  Enables Västtrafik staff to:
* 	⭒Determine routes that are frequently used and routes that do not exist
* 	⭒View insights on bus stop placements
*  Enables City Planner to:
* 	⭒View road usage and frequency of use
* 	⭒View route statistics and crowd levels


Technologies Involved:
*  HTML
*  CSS
*  Javascript
*  Python
*  MQTT


References:
* Show and hide layers:https://docs.mapbox.com/mapbox-gl-js/example/toggle-layers/
* Display a popup on hover: https://docs.mapbox.com/mapbox-gl-js/example/popup-on-hover/
* Create interactive hover effects with Mapbox GL JS: https://docs.mapbox.com/help/tutorials/create-interactive-hover-effects-with-mapbox-gl-js/
* Learn about websockets: http://www.steves-internet-guide.com/using-javascript-mqtt-client-websockets/


The Visualiser works by taking the information relayed from the broker once it 
has gone through the next component, which filters that data. The visualiser presents that data by a line on
the map. From here you can see how the density of requests to and from certain
areas builds over time.
