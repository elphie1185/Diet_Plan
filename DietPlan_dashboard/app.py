# import libraries
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

# initialise the app
app = dash.Dash(__name__)

# the data


# app layout
app.title = "Your Personalised Meal Plan"

app.layout = html.Div([
    # first row title and logo
    html.Div(
        [
            html.H1(children="Your Personalised Meal Plan",
                    classname="nine columns"
            ),
            html.Img(
                src="assets/fitness-3168246_1280.jpg",
                classname="three columns",
                style={
                    "height" : "10%",
                    "width" : "10%",
                    "float" : "right",
                    "position" : "relative",
                    "margin-top" : 10,
                    "margin-right" : 10
                },
            )
        ],
    className="row",
    style={"margin-left" : "2%", "margin-bottom" : "1%"}),

    # second row - subtitle
    html.Div([
        html.H5(children="Design meals suited to your exercising level",
                    classname="nine columns"
            ),
    ]),

    # third row - choices
    html.Div([
        html.Div([
           html.P("Choose Exercise Routine"),
                        dcc.Checklist(
                            id="workouts",
                            options=[{

                            }
                            ],
                            value=[],
                            multi=True,
                            labelStyle={"display": "inline-block"}),
                    ],
                    className="three columns",
                    style={"'margin-top': '10'"}),
            html.Div(
                    [
                        html.P("Choose Preferred Ingredients"),
                        dcc.Dropdown(
                            id="ingredients",
                            options=[{

                            }
                            ],
                            value=[],
                            multi=True,
                            clearable=False),
                    ],
                    className='three columns',
                    style={'margin-top': '10'}),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
