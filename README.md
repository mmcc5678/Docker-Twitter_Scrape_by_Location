# Docker Package: Scrape Twitter by Location

Developed this in 2016, have made a few minor alterations since but broadly unchanged. Takes locations in a variety of formats (can use multiple different locations in one connection), and creates a connection to Twitter, which will return tweets that match the query. Returned data is sent to a MongoDB instance, so chosen as this was my first project, and it enabled me to drop the whole tweets in and worry about processing them later.  

## Things I would change if using it for research again:
* Parse the fields and drop those unnecessary, unwanted and save space, over circa 6 months running this on the first occasion, I collected circa 1Tb of data and many millions of tweets.
* Change away from MongoDB and use PostGIS, likley with GeoServer in front to enable simple querying by a desktop GIS or even web viewer.
* Integrate some error handling/reporting, I used to have a crash every few days due to a 'data' event not being formated correctly, so my limited knoledge led me to use a 'try,' 'except,' routine. It works fine but hasn't enabled me to solve any problems.
