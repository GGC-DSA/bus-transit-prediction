# Bus Transit Prediction


<h3>Team Organization</h3>

Daniel Redder - Team Manager and Data Visualizer

Brittany Giordano - Data Modeler and Client Liaison

Turner Nalley - Data Analyzer and Project Scribe
 
<h3>Description</h3> 

Busnet is a dynamic map that shows the route and predicted bus station arrival time of a bus. Busnet aims to make good travel time predictions for both the route and segments of the route using GPS data and a neural network
 
<h3>Technologies</h3> 

Python, R, Raspberry Pi, Git

----

<details>
  <summary><strong>Data Sets</strong></summary>
  
  
  \ **Live Marta Bus Data**
  
  
  | Adherence | block_abbr | block_id | direction | last_updated | latitude | longitude | route | stop_id | timepoint | trip_id | vehicle |
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| -----------| -----------| -----------| -----------| -----------| 
| 0 |	39-7 |	341 |	Southbound |	2021-02-15 6:33:31 |	33.7837368 |	-84.267377 |	6 |	901155 |	Inman Park Station (North Loop) |	7035213 |	1530|

*figure 1*
  
  
  The data seen in *figure 1* is a sample of the live data we are collecting from marta. To do this we are using the [bus-transit](https://github.com/itsmarta/marta-python) python library to access marta's restfull api.

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **Adherence** :  ? \#TODO
  
  
  **block_abbr** : ? \#TODO
  
  
  **block_id** : An id corresponding to the "block" the current trip resides in. A block is a set of trips made with the same vehicle (may or may not be distinct to one day)
  
  
  **direction** : Appears to be a String representing the current heading of the bus
  
  **last_updated** : The time data was last reported from the bus
  
  **latitude** : a decimal degree between -90.0 and 90.0 representing the latitude of the bus
  
  
  **longitude** : a decimal degree between -180.0 and 180.0 representing the longitude of the bus
  
  
  **route** : may be related to routeID \#TODO 
  
  
  **stop_id** : Identifies a serviced stop. Unclear if next stop or last stop.
  
  
  **timepoint** : Identifies if arrival and departure times are adhered to by the vehicle or if they are aproximate  ( 0 approximate, 1 or empty times are exact)
  
  
  **trip_id** : Identifies the current trip (unclear what a trip includes)
  
  
  **vehicle** : ?  (not included in gtfs but presumably vehicle id)
  
  </details>
  <hr>
  
  **GTFS Data**
  
 MARATA DATA GUIDE : [GTFS-Reference-Data)(https://developers.google.com/transit/gtfs/reference#stop_timestxt)



<hr>
 
 **Gwinnett County Transit Feeds**
 
The data found [here](https://transitfeeds.com/p/gwinnett-county-transit/862)




</details>
