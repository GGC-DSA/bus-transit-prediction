# TODO List

**ToDo**

d3.js graph webpage inclusion: The d3.js code needs to be reworked to be a scatter instead of a line chart before it is put on the page because of the live data error with the ARIMA model

ARIMA prediction failure : When live data is sent to the ARIMA model for prediction it has a variety of data structure errors. This is not the case while training the data, and after extensive research we bypassed this by using a bulk ammount of  live data as testing data to get a output


Tutorial :  Create a walkthrough on how we configured AWS, processed our data, and how we made the interactive map for our repo

LSTM Optimize : Currently our RNN only has one 128 neuron layer. Its accuracy would likely be increased by adding additional layers and modifying the optimization algorithim (specifically for encouraging outlier detection)


**Waiting on Dependent Task**

Migration : Migrate our webhosting, storage, and gathering off of AWS. It is a good tool, but very costly when used academically


Data & About Us Page inclusion : Currently the Data & About Us pages are mostly completed, however they cannot be included until HTML template bug is fixed.



**Working On**

live-data-error :  presumably due to marta reopening stops it seems they changed the format they send data through their REST Api. This is causing their python package marta-python to throw error 30% of the time when collecting data. This is causing our webpage to have incorrect location data at times, but correct time data because the time file still transfers


HTML Templates Error:  HTML pages on our Nginx server do not seem to be updating. This is confirmed NOT to be a caching issue. Any further page development or inclusion is impossible until this is fixed.
