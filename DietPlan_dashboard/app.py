# import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

# initialise the app
app = dash.Dash(__name__)

app.layout = html.Div([
    # first row - title date picker and logo
    html.Div(
        [
            html.H1(children="Your Personalised Diet Plan",
                    className="nine columns"),

            html.Img(
                src="/assets/weight-loss-3231081_1920.jpeg",
                className="three columns",
                style={"height": "10%",
                       "width": "10%",
                       "float": "right",
                       "position": "relative",
                       "margin-top": 10,
                       "margin-right": 10
                       },
            )
        ],
        className="row",
        style={"margin-left": "2%", "margin-bottom": "1%"}),
    # second row - setting choices
    html.Div(
        [
            html.Div(
                [
                    html.P("Choose Activity"),
                    dcc.Dropdown(
                        id="activity",
                        #options=[{
                        #    "label": key,
                        #    "value": value
                        #} for key, value in release_version.items()
                        #],
                        value=[],
                        multi=True,
                        clearable=False),
                ],
                className="four columns",
                style={"margin-top": "10"}),

            html.Div(
                [
                    html.P("Choose preferred Ingredient"),
                    dcc.Dropdown(
                        id="ingredient",
                        # options=[{
                        #    "label": key,
                        #    "value": value
                        # } for key, value in release_version.items()
                        # ],
                        value=[],
                        multi=True,
                        clearable=False),
                ],
                className="four columns",
                style={"margin-top": "10"})
        ],
        className="row",
        style={"margin-left": "2%", "margin-bottom": "1%"}),

    # TABS
    dcc.Tabs(
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            # first tab
            dcc.Tab(label="Daily Summary",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[

                    ]
                    ),

            # Second tab
            dcc.Tab(label="Your Daily Exercise",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                    ]
                    ),

            # Third tab
            dcc.Tab(label="Your Daily Diet",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                    children=[
                        ]
                    )
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
