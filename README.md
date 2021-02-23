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
  **Adherence** :  Identifies if arrival and departure times are adhered to by the vehicle or if they are aproximate  ( 0 approximate, 1 or empty times are exact)
  
  
  **block_abbr** : ? \#TODO
  
  
  **block_id** : An id corresponding to the "block" the current trip resides in. A block is a set of trips made with the same vehicle (may or may not be distinct to one day)
  
  
  **direction** : Appears to be a String representing the current heading of the bus
  
  **last_updated** : The time data was last reported from the bus
  
  **latitude** : a decimal degree between -90.0 and 90.0 representing the latitude of the bus
  
  
  **longitude** : a decimal degree between -180.0 and 180.0 representing the longitude of the bus
  
  
  **route** : may be related to routeID \#TODO 
  
  
  **stop_id** : Identifies a serviced stop. Unclear if next stop or last stop.
  
  
  **timepoint** : Current Street of bus
  
  
  **trip_id** : Identifies the current trip (unclear what a trip includes)
  
  
  **vehicle** : ?  (not included in gtfs but presumably vehicle id)
  
  </details>

  
  <h2>GTFS Data</h2>
  
  GTFS or General Transit Feed Specification is a standard data format used for transportation data. This data provides all the organizational information that links feed data to specific buses, routes, and stops. The documentation for this data including field specifications can be found here "[GTFS-Reference-Data](https://developers.google.com/transit/gtfs/reference#stop_timestxt)". MARTA's 2020 implementation of GTFS can be found [here](https://www.itsmarta.com/app-developer-resources.aspx) in the form of a zip folder with the following files inside. 


**Agency**:

  | agency_id | agency_name | agency_url | agency_timezone | agency_lang | agency_phone | agency_email | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------|
| MARTA |	Metropolitan Atlanta Rapid Transit Authority |	http://www.itsmarta.com |	America/New_York |	en |	(404)848-5000 |	custserv@itsmarta.com  |	


**calendar**:

  | service_id | monday | tuesday | wednesday | thursday | friday | saturday | sunday | start-date | end-date |
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| -------| ---------| ---------|
| 2 |	0 |	0 |	0 |	0 |	0 | 0 |	0 | 20201205 | 20210423 |

**calendar_dates**:

  | service_id | date | exception_type | 
| --- | ----------- | -------- | 
| 20 |	20201224 |	1 |	

**routes**:

 | route_id | route_short_name | route_long_name | route_desc | route_type | route_url | route_text_color | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| 
| 14901 |	2 |	Ponce de Leon Avenue / Druid Hills |	 |	3 |	 | 00FF00 |	

**shapes**:

 | shape_id | shape_pt_lat | shape_pt_lon | shape_pt_sequence | 
| --- | ----------- | -------- | ------------ | 
| 117337 | 33.569089999999996 |	-84.40324|	1 |	

**stop_times**:

 | trip_id | arrival_time | departure_time | stop_id | stop_sequence |
 | --------- | -------- | ------------- | ----- | ------- |
 | 6190019 | 25:20:00 | 25:20:00 | 907960 | 1 |
 
**stops**:

 | stop_id | stop_code | stop_name | stop_lat | stop_lon |
 | --------- | -------- | ------------- | ----- | ------ |
 | 900142 | 99330 | CASCADE AVE SW @ ORLANDO ST SW| 33.727827 | -84.443085 |

**trips**:

| route_id | service_id | trip_id | trip_headsign | direction_id | block_id | shape_id |
| --------- | -------- | ------- | -------------- | --------- | ------- | ------ |
| 14974 | 3 | 6181301 | AUBURN AVE-PEACHTREE CTR-OLYMPIC PARK | 0 | 1031187 | 87791 |
 
 <h2>Gwinnett County Transit Feeds</h2>
 
The data found [here](https://transitfeeds.com/p/gwinnett-county-transit/862)


</details>

----


<details><summary><strong>Initial Visualizations</strong></summary>
 
 
 
 
 
 
 
 </details>










