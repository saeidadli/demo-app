import dash                     # pip install dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"G:\My Drive\Company\SE0078_HotelManagement\sample_hotel_data.csv")
df[['Month','year']] = df["Month"].str.split("-",expand=True)
df["year"]="20"+df["year"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1("Analytics Dashboard of a sample hotel data", style={"textAlign":"center"}),
    html.Hr(),
    html.P("Choose year:"),
    html.Div(html.Div([
        dcc.Dropdown(id='year', clearable=False,
                     value="2018",
                     options=[{'label': x, 'value': x} for x in
                              df["year"].unique()]),
    ],className="two columns"),className="row"),

    html.Div(id="output-div", children=[]),
])


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="year", component_property="value"),
)
def make_graphs(hotel_year):
    df_line = df[df["year"]==hotel_year].copy()
    fig_line = px.line(df_line, x="Month", y="Guest night % of January guest nights")
#
    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_line)], className="six columns"),
            # html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)