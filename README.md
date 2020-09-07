# plotly_dash_project

My goal for this project is to create a web application that visualizes US Police shoottings (2015 to 2020) in a way tha is dynamic and interactive.

Below are the following steps to achieve this outcome:

1. Used data from kaggle (https://www.kaggle.com/ahsen1330/us-police-shootings?select=shootings.csv)
2. Created credentials and authenticated API key for Google Geocoding and Places API
3. Created a function that gets the coordinates of a location, in this case I concatenated the 'city' and 'state' columns to get a more specific language. 
4. appended the latitude and longitude at the end of the dataframe
5. Grouped the data by Location (city and state) and took the count of number of shootings for each location
6. Used the counts as the metric to map the number of shootings across the states.

