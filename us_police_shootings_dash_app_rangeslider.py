import dash
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import  Output, Input
import pandas as pd

df = pd.read_csv(r'C:\Users\Alex\Documents\Python Scripts\US_shootings_with_coordinates_2015-2020.txt')
df = df.iloc[:,[8,16,17,19,21,22]]
df = df.groupby(['race','year','month','location','lat','lon']).location.agg('count').to_frame('count').reset_index()
# Ways of tried
# race = df.race.unique()
# race = race.tolist()


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("US Police Shootings"),
    html.H3("January 2015 - February 2020"),
    dcc.RangeSlider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=[2015, 2020],
        marks={i: '{}'.format(10 ** i) for i in df.year}
        #value=df['year'].min(),
        #marks={str(year): str(year) for year in df['year'].unique()},
        # marks={
        #     2015: '2015',
        #     2016: '2016',
        #     2017: '2017',
        #     2018: '2018'
        # },
        #step=None
        #included=False
    ),
    dcc.Graph(id='my-graph',
    )
])
    
    #dcc.Graph(id='my_graph',)

#Basic Callback
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input('year-slider', 'value')]
)
####Look up component property
def interactive_graphing(value_year):
    ####
    ### NEED TO UPDATE value_year to reflect Multiple  years, not just 1. Affects the callback
    ###
    dff = df[df.year==value_year]
    fig = px.histogram(data_frame=dff,x='race',y='count')
    ##print('You have selected "{}"'.format(value))
    return fig

if __name__ =='__main__':
    app.run_server()