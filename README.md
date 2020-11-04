# plotly_dash_project

My goal for this project is to create a web application that visualizes US Police shoottings (2015 to 2020) in a way tha is dynamic and interactive with Dash from Plotly.

Below are the following steps to achieve this outcome:

# Achieved Goals
1. Used data from kaggle (https://www.kaggle.com/ahsen1330/us-police-shootings?select=shootings.csv)
2. Created credentials and authenticated API key for Google Geocoding and Places API
3. Created a function that gets the coordinates of a location, in this case I concatenated the 'city' and 'state' columns to get a more precise results from Google's API
4. Appended the latitude and longitude at the end of the dataframe. Grouped the data by Location (city and state) and took the count of number of shootings for each location
6. Used the counts as the metric to map the number of shootings across the states. Used a Scatter Geo plot 

# Future Outcomes
1. Add a 2 more visualizations, with at least 1 different input from the Scatter Geomap
2. Add a callback so that the each of the visualizations, so that they're dynamic
3. Make the code modular so that I can fit this with another dataset. 
