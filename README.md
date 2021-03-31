# Bus Transit Prediction

<h3>Team Organization</h3>

Daniel Redder - Team Manager and Data Visualizer

Brittany Giordano - Data Modeler and Client Liaison

Turner Nalley - Data Analyzer and Project Scribe
 
<h3>Description</h3> 

Busnet is a dynamic map that shows the route and predicted bus station arrival time of a bus. Busnet aims to make good travel time predictions for both the route and segments of the route using GPS data and a neural network
 
<h3>Technologies</h3> 

Python, R, ~~Raspberry Pi~~, Git, AWS, Flask, Colab, Jupyter Notebooks, Tableau




<h2>Data Collection & Exploration</h2>



<details>
 <summary><strong>Data Sets</strong></summary>
  
  
  <h2>Live Marta Bus Data</h2>
 
  
  | Adherence | block_abbr | block_id | direction | last_updated | latitude | longitude | route | stop_id | timepoint | trip_id | vehicle |
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| -----------| -----------| -----------| -----------| -----------| 
| 0 |	39-7 |	341 |	Southbound |	2021-02-15 6:33:31 |	33.7837368 |	-84.267377 |	6 |	901155 |	Inman Park Station (North Loop) |	7035213 |	1530|

*figure 1*
  
  
  The data seen in *figure 1* is a sample of the live data we are collecting from marta. To do this we are using the [bus-transit](https://github.com/itsmarta/marta-python) python library to access marta's restfull api. The fields generated from this api vary slightly from the posted GTFS. \#TODO look into this

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **Adherence** :  The time either early (+) or late (-) a bus is to meeting its specificed arrival time at a stop
  
  
  **block_abbr** :  --unclear doesn't seem to match GTFS data--
  
  
  **block_id** : An id corresponding to the "block" the current trip resides in. A block is a set of trips made with the same vehicle (may or may not be distinct to one day)
  
  
  **direction** : Appears to be a String representing the current heading of the bus (cardinal Direction)
  
  **last_updated** : The time data was last reported from the bus
  
  **latitude** : a decimal degree between -90.0 and 90.0 representing the latitude of the bus
  
  
  **longitude** : a decimal degree between -180.0 and 180.0 representing the longitude of the bus
  
  
  **route** : The routeID the bus is currently servicing
  
  
  **stop_id** : Identifies the current next stop destination for the bus
  
  
  **timepoint** : Current Street of bus
  
  
  **trip_id** : Identifies the current trip --doesn't seem to match with GTFS trip data--
  
  
  **vehicle** : The unique ID identifying a specific bus
  
  </details>

  
  <h2>GTFS Data</h2>
  
  GTFS or General Transit Feed Specification is a standard data format used for transportation data. This data provides all the organizational information that links feed data to specific buses, routes, and stops. The documentation for this data including field specifications can be found here "[GTFS-Reference-Data](https://developers.google.com/transit/gtfs/reference#stop_timestxt)". MARTA's 2020 implementation of GTFS can be found [here](https://www.itsmarta.com/app-developer-resources.aspx) in the form of a zip folder with the following files inside. 


**Agency**:


**calendar**:


**calendar_dates**:


**routes**:


**shapes**:


**stop_times**:


**stops**:


**trips**:

 
 <h2>Gwinnett County Transit Feeds</h2>
 
The data found [here](https://transitfeeds.com/p/gwinnett-county-transit/862)


</details>

----


<details><summary><strong>Initial Visualizations</strong></summary>
 
 
 
 
 
 
 
 </details>










