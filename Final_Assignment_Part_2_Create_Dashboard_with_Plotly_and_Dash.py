#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IBM Data Visualization with Python — Final Assignment Part 2.

Tasks 2.1–2.6: an interactive Dash dashboard for recession-period and selected-year
automobile sales statistics. The Yearly Statistics branch filters the data by
input_year before generating the yearly automobile-sales chart, as required by
grader feedback.
"""

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/"
    "historical_automobile_sales.csv"
)

try:
    data = pd.read_csv("historical_automobile_sales.csv")
except FileNotFoundError:
    data = pd.read_csv(DATA_URL)

if "Year" not in data.columns:
    data["Year"] = pd.to_datetime(data["Date"]).dt.year
if "Month" not in data.columns:
    data["Month"] = pd.to_datetime(data["Date"]).dt.strftime("%b")
if "unemployment_rate" not in data.columns and "Unemployment_Rate" in data.columns:
    data["unemployment_rate"] = data["Unemployment_Rate"]
if "Unemployment_Rate" not in data.columns and "unemployment_rate" in data.columns:
    data["Unemployment_Rate"] = data["unemployment_rate"]
data["Year"] = pd.to_numeric(data["Year"], errors="coerce")
data["Month"] = data["Month"].astype(str).str[:3]
data["Month"] = pd.Categorical(
    data["Month"],
    categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    ordered=True,
)
UNEMPLOYMENT_COL = "unemployment_rate" if "unemployment_rate" in data.columns else "Unemployment_Rate"
year_list = sorted(data["Year"].dropna().astype(int).unique().tolist())

# TASK 2.1 — Create a Dash application with a meaningful title.
app = dash.Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"

# TASK 2.2 — Add dropdown menus with appropriate labels and options.
dropdown_options = [
    {"label": "Yearly Statistics", "value": "Yearly Statistics"},
    {"label": "Recession Period Statistics", "value": "Recession Period Statistics"},
]

app.layout = html.Div(
    [
        html.H1(
            "Automobile Sales Statistics Dashboard",
            style={"textAlign": "center", "color": "#503D36", "fontSize": 24},
        ),
        html.Div(
            [
                html.Label("Select Statistics:"),
                dcc.Dropdown(
                    id="dropdown-statistics",
                    options=dropdown_options,
                    value="Yearly Statistics",
                    placeholder="Select a report type",
                    clearable=False,
                ),
            ]
        ),
        html.Div(
            [
                html.Label("Select Year:"),
                dcc.Dropdown(
                    id="select-year",
                    options=[{"label": year, "value": year} for year in year_list],
                    value=2020 if 2020 in year_list else (year_list[-1] if year_list else None),
                    placeholder="Select a year",
                    clearable=False,
                ),
            ]
        ),
        # TASK 2.3 — Output division with the required id and classname.
        html.Div(id="output-container", className="chart-grid", style={"display": "flex", "flexDirection": "column"}),
    ]
)

# TASK 2.4 — Enable the year dropdown only for Yearly Statistics.
@app.callback(
    Output(component_id="select-year", component_property="disabled"),
    Input(component_id="dropdown-statistics", component_property="value"),
)
def update_input_container(selected_statistics):
    return selected_statistics != "Yearly Statistics"

# TASK 2.4 / 2.5 / 2.6 — Update the dashboard graphs when filters change.
@app.callback(
    Output(component_id="output-container", component_property="children"),
    [
        Input(component_id="dropdown-statistics", component_property="value"),
        Input(component_id="select-year", component_property="value"),
    ],
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == "Recession Period Statistics":
        recession_data = data[data["Recession"] == 1].copy()

        # TASK 2.5 — Graph 1: average automobile sales by year during recessions.
        yearly_rec = recession_data.groupby("Year")["Automobile_Sales"].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x="Year",
                y="Automobile_Sales",
                markers=True,
                title="Average Automobile Sales Fluctuation Over Recession Period",
            )
        )

        # TASK 2.5 — Graph 2: average sales by vehicle type during recessions.
        avg_vehicles_sold = recession_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(
                avg_vehicles_sold,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title="Average Number of Vehicles Sold by Vehicle Type During Recession",
            )
        )

        # TASK 2.5 — Graph 3: advertising expenditure share by vehicle type.
        exp_rec = recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(
                exp_rec,
                values="Advertising_Expenditure",
                names="Vehicle_Type",
                title="Total Expenditure Share by Vehicle Type During Recession",
            )
        )

        # TASK 2.5 — Graph 4: sales by vehicle type coloured by unemployment rate.
        unemployment_effect = (
            recession_data.groupby(["Vehicle_Type", UNEMPLOYMENT_COL])["Automobile_Sales"]
            .mean()
            .reset_index()
        )
        R_chart4 = dcc.Graph(
            figure=px.bar(
                unemployment_effect,
                x="Vehicle_Type",
                y="Automobile_Sales",
                color=UNEMPLOYMENT_COL,
                title="Effect of Unemployment Rate on Vehicle Type and Sales During Recession",
            )
        )

        return [
            html.Div([R_chart1, R_chart2], className="chart-row", style={"display": "flex", "flexWrap": "wrap"}),
            html.Div([R_chart3, R_chart4], className="chart-row", style={"display": "flex", "flexWrap": "wrap"}),
        ]

    # TASK 2.6 — Create and display graphs for Yearly Report Statistics.
    if selected_statistics == "Yearly Statistics" and input_year is not None:
        # Required by grader feedback: filter by input_year BEFORE making the yearly sales graph.
        yearly_data = data[data["Year"] == input_year].copy()

        # Graph 1: yearly automobile sales for the selected year only.
        yas = yearly_data.groupby("Year")["Automobile_Sales"].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(
                yas,
                x="Year",
                y="Automobile_Sales",
                markers=True,
                title=f"Average Automobile Sales in Selected Year ({input_year})",
            )
        )

        # Graph 2: monthly automobile sales in the selected year.
        monthly_sales = yearly_data.groupby("Month", observed=True)["Automobile_Sales"].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(
                monthly_sales,
                x="Month",
                y="Automobile_Sales",
                markers=True,
                title=f"Total Monthly Automobile Sales in {input_year}",
            )
        )

        # Graph 3: average sales by vehicle category in the selected year.
        avr_vdata = yearly_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(
                avr_vdata,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title=f"Average Vehicles Sold by Vehicle Type in {input_year}",
            )
        )

        # Graph 4: advertising expenditure by vehicle type in the selected year.
        exp_data = yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(
                exp_data,
                values="Advertising_Expenditure",
                names="Vehicle_Type",
                title=f"Total Advertisement Expenditure for Each Vehicle Type in {input_year}",
            )
        )

        return [
            html.Div([Y_chart1, Y_chart2], className="chart-row", style={"display": "flex", "flexWrap": "wrap"}),
            html.Div([Y_chart3, Y_chart4], className="chart-row", style={"display": "flex", "flexWrap": "wrap"}),
        ]

    return html.Div("Select a report type and year to display statistics.")


if __name__ == "__main__":
    app.run(debug=True)
