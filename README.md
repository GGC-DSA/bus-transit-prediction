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


**agency**:

  | agency_id | agency_name | agency_url | agency_timezone | agency_lang | agency_phone | agency_email | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------|
| MARTA |	Metropolitan Atlanta Rapid Transit Authority |	http://www.itsmarta.com |	America/New_York |	en |	(404)848-5000 |	custserv@itsmarta.com  |	

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **agency_id** :  Identifies a transit brandwhich is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies. This field is required when the dataset contains data for multiple transit agencies, otherwise it is optional.

**agency_name** : Full name of the transit agency.

**agency_url** : URL of the transit agency.

**agency_timezone** : Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone.
   
**agency_lang** :Primary language used by this transit agency. This field helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset.

**agency_phone** : A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's 503-238-RIDE) is permitted, but the field must not contain any other descriptive text.


**agency_email** : Email address actively monitored by the agency’s customer service department. This email address should be a direct contact point where transit riders can reach a customer service representative at the agency.

  
  </details>


**calendar**:

  | service_id | monday | tuesday | wednesday | thursday | friday | saturday | sunday | start-date | end-date |
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| -------| ---------| ---------|
| 2 |	0 |	0 |	0 |	0 |	0 | 0 |	0 | 20201205 | 20210423 |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **service_id** : Uniquely identifies a set of dates when service is available for one or more routes. Each service_id value can appear at most once in a calendar.txt file.

  **monday** : Indicates whether the service operates on all Mondays in the date range specified by the start_date and end_date fields. Note that exceptions for particular dates    may be listed in calendar_dates.txt. Valid options are:

   1 - Service is available for all Mondays in the date range.
   0 - Service is not available for Mondays in the date range.
  **tuesday** : Functions in the same way as monday except applies to Tuesdays

  **wednesday** : Functions in the same way as monday except applies to Wednesdays

  **thursday** : Functions in the same way as monday except applies to Thursdays

  **friday** : Functions in the same way as monday except applies to Fridays

  **saturday** : Functions in the same way as monday except applies to Saturdays.

  **sunday** : Functions in the same way as monday except applies to Sundays.

  **start-date** : Start service day for the service interval.

  **end-date** : End service day for the service interval. This service day is included in the interval.

   
  
  </details>
  
**calendar_dates**:

  | service_id | date | exception_type | 
| --- | ----------- | -------- | 
| 20 |	20201224 |	1 |	

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **service_id** : Identifies a set of dates when a service exception occurs for one or more routes. Each (service_id, date) pair can only appear once in calendar_dates.txt if using calendar.txt and calendar_dates.txt in conjunction. If a service_id value appears in both calendar.txt and calendar_dates.txt, the information in calendar_dates.txt modifies the service information specified in calendar.txt.

  **date** :Date when service exception occurs.

  **exception_type** : Indicates whether service is available on the date specified in the date field. Valid options are:

1 - Service has been added for the specified date.
2 - Service has been removed for the specified date.
  
  </details>
  
**routes**:

 | route_id | route_short_name | route_long_name | route_desc | route_type | route_url | route_text_color | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| 
| 14901 |	2 |	Ponce de Leon Avenue / Druid Hills |	 |	3 |	 | 00FF00 |	

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **route_id** :  Identifies a route.

  **route_short_name** :  Short name of a route. This will often be a short, abstract identifier like "32", "100X", or "Green" that riders use to identify a route, but which doesn't give any indication of what places the route serves. Either route_short_name or route_long_name must be specified, or potentially both if appropriate.

  **route_long_name** :  Full name of a route. This name is generally more descriptive than the route_short_name and often includes the route's destination or stop. Either route_short_name or route_long_name must be specified, or potentially both if appropriate.

  **route_desc** :  Description of a route that provides useful, quality information. Do not simply duplicate the name of the route.
  **route_type** :  Indicates the type of transportation used on a route. Valid options are:

0 - Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area.
1 - Subway, Metro. Any underground rail system within a metropolitan area.
2 - Rail. Used for intercity or long-distance travel.
3 - Bus. Used for short- and long-distance bus routes.
4 - Ferry. Used for short- and long-distance boat service.
5 - Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle, e.g., cable car in San Francisco.
6 - Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables.
7 - Funicular. Any rail system designed for steep inclines.
11 - Trolleybus. Electric buses that draw power from overhead wires using poles.
12 - Monorail. Railway in which the track consists of a single rail or a beam.

  **route_url** :  URL of a web page about the particular route. Should be different from the agency.agency_url value.

  **route_text_color** :  Legible color to use for text drawn against a background of route_color. Defaults to black (000000) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen.

   
  
  </details>
  
**shapes**:

 | shape_id | shape_pt_lat | shape_pt_lon | shape_pt_sequence | 
| --- | ----------- | -------- | ------------ | 
| 117337 | 33.569089999999996 |	-84.40324|	1 |	

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **shape_id** : Identifies a shape.

  **shape_pt_lat** : Latitude of a shape point. Each record in shapes.txt represents a shape point used to define the shape.

  **shape_pt_lon** : Longitude of a shape point.

  **shape_pt_sequence** : Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive.
  
  </details>
  
**stop_times**:

 | trip_id | arrival_time | departure_time | stop_id | stop_sequence |
 | --------- | -------- | ------------- | ----- | ------- |
 | 6190019 | 25:20:00 | 25:20:00 | 907960 | 1 |
 
 <details><summary><strong>Field Definitions</strong></summary>
  
  \
  **trip_id** :  Identifies a trip.

  **arrival_id** : Arrival time at a specific stop for a specific trip on a route. If there are not separate times for arrival and departure at a stop, enter the same value for arrival_time and departure_time. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins.

Scheduled stops where the vehicle strictly adheres to the specified arrival and departure times are timepoints. If this stop is not a timepoint, it is recommended to provide an estimated or interpolated time. If this is not available, arrival_time can be left empty. Further, indicate that interpolated times are provided with timepoint=0. If interpolated times are indicated with timepoint=0, then time points must be indicated with timepoint=1. Provide arrival times for all stops that are time points. An arrival time must be specified for the first and the last stop in a trip.

  **departure_time** : Departure time from a specific stop for a specific trip on a route. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. If there are not separate times for arrival and departure at a stop, enter the same value for arrival_time and departure_time. See the arrival_time description for more details about using timepoints correctly.

The departure_time field should specify time values whenever possible, including non-binding estimated or interpolated times between timepoints.

  **stop_id** : Identifies the serviced stop. All stops serviced during a trip must have a record in stop_times.txt. Referenced locations must be stops, not stations or station entrances. A stop may be serviced multiple times in the same trip, and multiple trips and routes may service the same stop.

  **stop_sequence** : Order of stops for a particular trip. The values must increase along the trip but do not need to be consecutive.
  
  </details>
  
**stops**:

 | stop_id | stop_code | stop_name | stop_lat | stop_lon |
 | --------- | -------- | ------------- | ----- | ------ |
 | 900142 | 99330 | CASCADE AVE SW @ ORLANDO ST SW| 33.727827 | -84.443085 |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **stop_id** :  Identifies a stop, station, or station entrance.

The term "station entrance" refers to both station entrances and station exits. Stops, stations or station entrances are collectively referred to as locations. Multiple routes may use the same stop.

  **stop_code** : Short text or a number that identifies the location for riders. These codes are often used in phone-based transit information systems or printed on signage to make it easier for riders to get information for a particular location. The stop_code can be the same as stop_id if it is public facing. This field should be left empty for locations without a code presented to riders.

  **stop_name** : Name of the location. Use a name that people will understand in the local and tourist vernacular.

When the location is a boarding area (location_type=4), the stop_name should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).

  **stop_lat** : Latitude of the location.

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).

  **stop_lon** : Longitude of the location.

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).
  
  </details>
  
**trips**:

| route_id | service_id | trip_id | trip_headsign | direction_id | block_id | shape_id |
| --------- | -------- | ------- | -------------- | --------- | ------- | ------ |
| 14974 | 3 | 6181301 | AUBURN AVE-PEACHTREE CTR-OLYMPIC PARK | 0 | 1031187 | 87791 |
 
 <details><summary><strong>Field Definitions</strong></summary>
  
  \
  **route_id** :  Identifies a route.

  **service_id** :  Identifies a set of dates when service is available for one or more routes.

  **trip_id** :  Identifies a trip.

  **trip_headsign** :  Text that appears on signage identifying the trip's destination to riders. Use this field to distinguish between different patterns of service on the same route. If the headsign changes during a trip, trip_headsign can be overridden by specifying values for the stop_times.stop_headsign.

  **direction_id** :  Indicates the direction of travel for a trip. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:

0 - Travel in one direction (e.g. outbound travel).
1 - Travel in the opposite direction (e.g. inbound travel).

  **block_id** :  Identifies the block to which the trip belongs. A block consists of a single trip or many sequential trips made using the same vehicle, defined by shared service days and block_id. A block_id can have trips with different service days, making distinct blocks. See the example below
  
  **shape_id** :  Identifies a geospatial shape that describes the vehicle travel path for a trip.

Conditionally required:
This field is required if the trip has continuous behavior defined, either at the route level or at the stop time level.
Otherwise, it's optional.
  
  </details>
  
 <h2>Gwinnett County Transit Feeds</h2>
 
The data found [here](https://transitfeeds.com/p/gwinnett-county-transit/862)


</details>

----


<details><summary><strong>Initial Visualizations</strong></summary>
 
 
 
 
 
 
 
 </details>










