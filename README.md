# Bus Transit Prediction
Team: BusNet
<br>Website: http://busnetcloud.com
<h3>Team Structure</h3>

Daniel Redder - Team Manager and Data Visualizer

![brittany_picture](https://imgur.com/a/Q2K3vRU)
Brittany Giordano - Data Modeler and Client Liaison

Turner Nalley - Data Analyzer and Project Scribe
 
<h3>Description</h3> 

Busnet is a dynamic map that shows the route and predicted bus station arrival time of a bus. Busnet aims to make good travel time predictions for both the route and segments of the route using GPS data and a neural network
 
<h3>Technologies</h3> 

Python, R, ~~Raspberry Pi~~, Git, AWS, Colab, Jupyter Notebooks, Tableau

Python Packages : numpy, statsmodels, pandas, matplotlib, seaborn, keras, tensorflow, marta-python, flask, boto3, pickle, tensorboard

Other tools : uwsgi, nginx, tmux, cron, notepad++, AWS CLI


<h2>Data Sets</h2>
  
 <details><summary>Expand</summary>
 
 
  <h2>Live Marta Bus Data</h2>
 
 Description and things
 
<details><summary><strong>Input Data Structure</strong></summary>
  
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
  
  </details></details>

  
  <h2>GTFS Data</h2>
  
  GTFS or General Transit Feed Specification is a standard data format used for transportation data. This data provides all the organizational information that links feed data to specific buses, routes, and stops. The documentation for this data including field specifications can be found here "[GTFS-Reference-Data](https://developers.google.com/transit/gtfs/reference#stop_timestxt)". MARTA's 2020 implementation of GTFS can be found [here](https://www.itsmarta.com/app-developer-resources.aspx) in the form of a zip folder with the following files inside. 

<details><summary><strong>Input Data Structure</strong></summary>

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
  
  </details></details>
  
 <h2>Gwinnett County Transit Feeds</h2>
 
The data found [here](https://transitfeeds.com/p/gwinnett-county-transit/862) contains historical GTFS data for Gwinnett County Transit system. This data includes information containing stops, stop times, and timetables. This data is a branch of GTFS data, and similarly the information including field specifications can be found here [GTFS-Reference-Data](https://developers.google.com/transit/gtfs/reference#stop_timestxt).

<details><summary><strong>Input Data Structure</strong></summary>

**agency**:

| agency_id | agency_url | agency_lang | agency_name | agency_phone | agency_timezone | agency_fare_url | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------|
| 669 |http://www.gctransit.com |	en |	Gwinnett County Transit |	770-822-5010 |	America/New_York |	https://www.gwinnettcounty.com/portal/gwinnett/Departments/Transportation/GwinnettCountyTransit/PassesandTickets  |	

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **agency_id** :  Identifies a transit brandwhich is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies. This field is required when the dataset contains data for multiple transit agencies, otherwise it is optional.
  **agency_name** : Full name of the transit agency.

**agency_url** : URL of the transit agency.

**agency_timezone** : Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone.
   
**agency_lang** :Primary language used by this transit agency. This field helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset.

**agency_phone** : A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's 503-238-RIDE) is permitted, but the field must not contain any other descriptive text.

**agency_fare_url** : URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online.



</details>

**calendar**:

  | service_id | service_name | monday | tuesday | wednesday | thursday | friday | saturday | sunday | start-date | end-date |
| --- | ----- | ----------- | -------- | ------------ | -----------| -----------| -----------| -------| ---------| ---------|
| c_20334_b_27144_d_32 |	Year Round (Reduced Service) NEW (Saturday only)  | 0 |	0 |	0 |	0 |	0 | 1 |	0 | 20200601 | 20210101 |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **service_id** : Uniquely identifies a set of dates when service is available for one or more routes. Each service_id value can appear at most once in a calendar.txt file.

 **service_name** : long form name of the service for a bus.
 
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

  | service_id | date | holiday_name |exception_type | 
| --- | ----------- | --------- | -------- | 
| c_4392_b_none_d_31 |	20201127 |	Day After Thanksgiving |	1 |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **service_id** : Identifies a set of dates when a service exception occurs for one or more routes. Each (service_id, date) pair can only appear once in calendar_dates.txt if using calendar.txt and calendar_dates.txt in conjunction. If a service_id value appears in both calendar.txt and calendar_dates.txt, the information in calendar_dates.txt modifies the service information specified in calendar.txt.

  **date** :Date when service exception occurs.
  
  **holiday_name** : name of the holiday.

  **exception_type** : Indicates whether service is available on the date specified in the date field. Valid options are:

1 - Service has been added for the specified date.
2 - Service has been removed for the specified date.
  
  </details>
  
   **directions**:

  | route_id | direction_id | direction | 
| --- | ----------- | --------- |  
| 15635 |	1 |	Outbound |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **route_id** : Identifies a route associated with the fare class. If several routes with the same fare attributes exist, create a record in fare_rules.txt for each route.
Example: If fare class "b" is valid on route "TSW" and "TSE", the fare_rules.txt file would contain these records for the fare class:
fare_id,route_id
b,TSW
b,TSE
  
  **direction_id** : Indicates the direction of travel for a trip. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:

0 - Travel in one direction (e.g. outbound travel).
1 - Travel in the opposite direction (e.g. inbound travel).
Example: The trip_headsign and direction_id fields could be used together to assign a name to travel in each direction for a set of trips. A trips.txt file could contain these records for use in time tables:
trip_id,...,trip_headsign,direction_id
1234,...,Airport,0
1505,...,Downtown,1
  
  **direction** : Indicates Outbound or Inboud

  </details>
  
   **fare_attributes** :

  | agency_id | fare_id | price | currency_type | payment_method | transfers | transfer_duration |
| --- | ----------- | --------- |  ------------ | -------------- | --------- | ----------------- |
| 669 |	1951 |	2.50 | USD | 0 | 0 | 0 |

<details><summary><strong>Field Definitions</strong></summary>
  
  \
  **agency_id** :Identifies the relevant agency for a fare. This field is required for datasets with multiple agencies defined in agency.txt, otherwise it is optional.

  **fare_id** : Identifies a fare class.
  **price** : Fare price, in the unit specified by currency_type.
  **currency_type** : Currency used to pay the fare.

  **payment_method** : Indicates when the fare must be paid. Valid options are:

0 - Fare is paid on board.
1 - Fare must be paid before boarding.
  
  **transfers** : Indicates the number of transfers permitted on this fare. The fact that this field can be left empty is an exception to the requirement that a Required field must not be empty. Valid options are:

0 - No transfers permitted on this fare.
1 - Riders may transfer once.
2 - Riders may transfer twice.
empty - Unlimited transfers are permitted.
  **transfer_duration** :Length of time in seconds before a transfer expires. When transfers=0 this field can be used to indicate how long a ticket is valid for or it can can be left empty.


</details>

**routes**:

 | route_id | route_short_name | route_long_name | route_desc | route_type | route_url | route_text_color | 
| --- | ----------- | -------- | ------------ | -----------| -----------| -----------| 
| 669 |	6292 |	Doraville via Satellite |	 |	3 |	 | FFFFFF |	

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

**stops**:

 | stop_id | stop_code | stop_name | stop_lat | stop_lon |
 | --------- | -------- | ------------- | ----- | ------ |
 | 2334737 | 32 | Arts Center Marta Station | 33.727827 | -84.443085 |

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
  
  **transfers**:

| from_stop_id | to_stop_id | transfer_type | min_transfer_time |
| --------- | -------- | ------- | -------------- | 
| 2334746 | 2334746 | 1 | 0 |
 
 <details><summary><strong>Field Definitions</strong></summary>
  
  \
  **from_stop_id** : Identifies a stop or station where a connection between routes begins. If this field refers to a station, the transfer rule applies to all its child stops.

  
  **to_stop_id** : Identifies a stop or station where a connection between routes ends. If this field refers to a station, the transfer rule applies to all child stops.

  
  **transfer_type** : Indicates the type of connection for the specified (from_stop_id, to_stop_id) pair. Valid options are:

0 or empty - Recommended transfer point between routes.
1 - Timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one and leave sufficient time for a rider to transfer between routes.
2 - Transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by min_transfer_time.
3 - Transfers are not possible between routes at the location.
  
  **min_transfer_time** : Amount of time, in seconds, that must be available to permit a transfer between routes at the specified stops. The min_transfer_time should be sufficient to permit a typical rider to move between the two stops, including buffer time to allow for schedule variance on each route.

  
  
  
</details>
  
  **trips**:

| route_id | service_id | trip_id | trip_headsign | direction_id | block_id | shape_id |
| --------- | -------- | ------- | -------------- | --------- | ------- | ------ |
| 11089 | c_16096_b | t_518615 | Georgia Gwinnett Collede | 0 | p_178664 | 87791 |
 
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
  
  </details></details></details>


<h2>Data Exploration & Analysis</h2>



<strong>Initial Visualizations</strong>
 
 - <strong>Gwinnett County:</strong> [Colab_Notebook](https://rpubs.com/blgiordano/744665)
 
 - <strong>GTFS:</strong>  [Colab_Notebook](https://colab.research.google.com/drive/1Ii7fnipjdU13v7k4cybNDOAv-2EHDBET?usp=sharing)
 
- <strong>Live Data:</strong> [Colab_Notebook](https://colab.research.google.com/drive/1U6bQ-Ys3x8siNMl-zr0SpZKuEu_uifQ9?usp=sharing)
 

**Analysis**

[Colab Notebook](https://colab.research.google.com/drive/1gzzbi2RumkQ-HN2GJkvz-k8B5H0zaiGB)


<h2>Modeling</h2>

<details><summary><strong>ARIMA</strong></summary>
<br>
ARIMA is a special statistical regression model we use to predict trending Adherence values during the day. It is more accurate at predicting values then our RNN model when predicting generally across a day (no specific vehicle or route). 


<br>ARIMA Training Code: [Colab_Notebook](https://colab.research.google.com/drive/12OrOdpib8wiKRPiagumg_dmkC0eZ8S61?usp=sharing)
 
 </details>


<details><summary><strong>Long Short Term Memory RNN</strong></summary>**
 
 The LSTM model is a keras package based neural network using the LSTM layer. This is what we use to predict specific adherence values live on our webpage. 
 
 <br>LSTM Training Code: [Colab_Notebook](https://colab.research.google.com/drive/1So4MRw1zTesMEswODRvcPVnY70oJdJpO?usp=sharing)
 
 </details>





