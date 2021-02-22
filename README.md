# Bus Transit Prediction


**Team Organization**

Daniel Redder - Team Manager and Data Visualizer

Brittany Giordano - Data Modeler and Client Liaison

Turner Nalley - Data Analyzer and Project Scribe

---- 
**Description** 

Busnet is a dynamic map that shows the route and predicted bus station arrival time of a bus. Busnet aims to make good travel time predictions for both the route and segments of the route using GPS data and a neural network

---- 
**Technologies** 

Python, R, Raspberry Pi, Git

----

<details>
  <summary><strong>Data Sets</strong></summary>
  
  
  **Live Marta Bus Data**
  
  
  | Adherence | block_abbr | block_id | direction | last_updated | latitude | longitude | route | stop_id | timepoint | trip_id | vehicle |
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| -----------| -----------| -----------| -----------| -----------| 
| 0 |	39-7 |	341 |	Southbound |	2021-02-15 6:33:31 |	33.7837368 |	-84.267377 |	6 |	901155 |	Inman Park Station (North Loop) |	7035213 |	1530|
*figure 1*
  
  
  The data seen in *figure 1* is a sample of the live data we are collecting from marta. To do this we are using the [bus-transit](https://github.com/itsmarta/marta-python) python library to access marta's restfull api
  
  ----
  
  **GTFS Data**
  
  [GTFS-Reference-Data)(https://developers.google.com/transit/gtfs/reference#stop_timestxt)
</details>
