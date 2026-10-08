#!/usr/bin/env python
# coding: utf-8

"""
IBM Data Visualization with Python
Final Assignment: Part 2 - Create Dashboard with Plotly and Dash

The application attempts the official IBM Skills Network dataset first and
falls back to a local historical_automobile_sales.csv if necessary.
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/"
    "historical_automobile_sales.csv"
)

try:
    data = pd.read_csv(DATA_URL)
except Exception:
    data = pd.read_csv("historical_automobile_sales.csv")

# Normalize naming variants found in some versions of the exercise.
if "unemployment_rate" not in data.columns and "Unemployment_Rate" in data.columns:
    data["unemployment_rate"] = data["Unemployment_Rate"]
if "Vehicle_Type" not in data.columns and "Vehicle" in data.columns:
    data["Vehicle_Type"] = data["Vehicle"]
if "Advertising_Expenditure" not in data.columns and "Advertisement_Expenditure" in data.columns:
    data["Advertising_Expenditure"] = data["Advertisement_Expenditure"]

app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"

dropdown_options = [
    {"label": "Yearly Statistics", "value": "Yearly Statistics"},
    {"label": "Recession Period Statistics", "value": "Recession Period Statistics"},
]

year_list = sorted(data["Year"].dropna().astype(int).unique().tolist())

app.layout = html.Div([
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={"textAlign": "center", "color": "#503D36", "fontSize": 26}
    ),

    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id="dropdown-statistics",
            options=dropdown_options,
            value=None,
            placeholder="Select a report type"
        )
    ]),

    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id="select-year",
            options=[{"label": year, "value": year} for year in year_list],
            value=None
        )
    ]),

    html.Div(
        id="output-container",
        className="chart-grid",
        style={"display": "flex", "flexDirection": "column"}
    )
])

# TASK 2.4: Enable the year dropdown only for Yearly Statistics.
@app.callback(
    Output("select-year", "disabled"),
    Input("dropdown-statistics", "value")
)
def update_input_container(selected_statistics):
    return selected_statistics != "Yearly Statistics"

# TASK 2.4 / 2.5 / 2.6: Generate dashboard graphs.
@app.callback(
    Output("output-container", "children"),
    [
        Input("dropdown-statistics", "value"),
        Input("select-year", "value")
    ]
)
def update_output_container(selected_statistics, input_year):

    if selected_statistics == "Recession Period Statistics":
        recession_data = data[data["Recession"] == 1]

        # TASK 2.5 — Plot 1
        yearly_rec = (
            recession_data.groupby("Year")["Automobile_Sales"]
            .mean().reset_index()
        )
        R_chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x="Year", y="Automobile_Sales",
                title="Average Automobile Sales fluctuation over Recession Period"
            )
        )

        # TASK 2.5 — Plot 2
        average_sales = (
            recession_data.groupby("Vehicle_Type")["Automobile_Sales"]
            .mean().reset_index()
        )
        R_chart2 = dcc.Graph(
            figure=px.bar(
                average_sales,
                x="Vehicle_Type", y="Automobile_Sales",
                title="Average Number of Vehicles Sold by Vehicle Type"
            )
        )

        # TASK 2.5 — Plot 3
        exp_rec = (
            recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
            .sum().reset_index()
        )
        R_chart3 = dcc.Graph(
            figure=px.pie(
                exp_rec,
                names="Vehicle_Type",
                values="Advertising_Expenditure",
                title="Total Expenditure Share by Vehicle Type During Recession"
            )
        )

        # TASK 2.5 — Plot 4
        unemp_rec = (
            recession_data.groupby("Vehicle_Type")["unemployment_rate"]
            .mean().reset_index()
        )
        R_chart4 = dcc.Graph(
            figure=px.bar(
                unemp_rec,
                x="Vehicle_Type",
                y="unemployment_rate",
                title="Effect of Unemployment Rate on Vehicle Type and Sales"
            )
        )

        return [
            html.Div([R_chart1, R_chart2], style={"display": "flex", "flexWrap": "wrap"}),
            html.Div([R_chart3, R_chart4], style={"display": "flex", "flexWrap": "wrap"})
        ]

    elif selected_statistics == "Yearly Statistics" and input_year:
        yearly_data = data[data["Year"] == input_year]

        # TASK 2.6 — Plot 1
        yas = data.groupby("Year")["Automobile_Sales"].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(
                yas,
                x="Year", y="Automobile_Sales",
                title="Yearly Automobile Sales"
            )
        )

        # TASK 2.6 — Plot 2
        mas = (
            yearly_data.groupby("Month")["Automobile_Sales"]
            .sum().reset_index()
        )
        Y_chart2 = dcc.Graph(
            figure=px.line(
                mas,
                x="Month", y="Automobile_Sales",
                title=f"Monthly Automobile Sales in {input_year}"
            )
        )

        # TASK 2.6 — Plot 3
        avr_vdata = (
            yearly_data.groupby("Vehicle_Type")["Automobile_Sales"]
            .mean().reset_index()
        )
        Y_chart3 = dcc.Graph(
            figure=px.bar(
                avr_vdata,
                x="Vehicle_Type", y="Automobile_Sales",
                title=f"Average Vehicles Sold by Vehicle Type in {input_year}"
            )
        )

        # TASK 2.6 — Plot 4
        exp_data = (
            yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
            .sum().reset_index()
        )
        Y_chart4 = dcc.Graph(
            figure=px.pie(
                exp_data,
                names="Vehicle_Type",
                values="Advertising_Expenditure",
                title="Total Advertisement Expenditure per Vehicle Type"
            )
        )

        return [
            html.Div([Y_chart1, Y_chart2], style={"display": "flex", "flexWrap": "wrap"}),
            html.Div([Y_chart3, Y_chart4], style={"display": "flex", "flexWrap": "wrap"})
        ]

    return None


if __name__ == "__main__":
    app.run(debug=True)
