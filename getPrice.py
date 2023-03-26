import csv
from datetime import datetime, timedelta
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

# Read the price data from the file
with open('price.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    data = list(reader)

date = data[0][0]
time = data[0][1]
price =data[0][4]

highest = data[2][0]
lowest = data[1][0]

def toPrice(price):
    price = price[1:]
    res = ''
    for i in range(len(price)):
        if price[i] != ',':
            res += price[i]
    return float(res)

highest = toPrice(highest)
lowest = toPrice(lowest)
price = toPrice(price)

#erase the content of the file

# Create the Dash app
app = dash.Dash(__name__)

#add a graph that shows the current comparison between the highest and lowest price with dash


# Define the app layout
app.layout = html.Div([
    html.H1('Bitcoin Price Dashboard'),
    html.H2('Bitcoin Price today is: ' + str(price) + ' USD '),
    html.P('Date: ' + time + ' ' + date),
    # html.H2('Highest price today is: ' + highest[0]),
    # html.H2('Lowest price today is: ' +lowest[0]),
    dcc.Graph(
    figure={
        'data': [
            {'x': ['lowest', 'actual', 'highest'], 'y': [lowest , price, highest], 'type': 'line', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Price Comparison'
        }
    }
    )
])


# Run the app
if __name__ == '__main__':
    app.run_server(host = "0.0.0.0", port = 8050, debug=True)
