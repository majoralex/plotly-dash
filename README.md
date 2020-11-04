# plotly_dash_project

My goal for this project is to create a web application that visualizes US Police shoottings (2015 to 2020) in a way tha is dynamic and interactive with Dash from Plotly.

Below are the following steps to achieve this outcome:

# Achieved Goals
1. Used data from kaggle (https://www.kaggle.com/ahsen1330/us-police-shootings?select=shootings.csv)
2. Created credentials and authenticated API key for Google Geocoding and Places API
3. Performed manipulations on the data to calculate an aggregate of count per each location within the United States
4. Used the counts as the trace to map the number of shootings across the states.
5. Styled the map with a different layout and marked each of the traces by race of the victim.

# Future Outcomes
1. Add a 2 more visualizations, with at least 1 different input from the Scatter Geomap
2. Add a callback so that the each of the visualizations, so that they're dynamic
3. Make the code modular to fit this with another dataset based on 'year' or 'date'
