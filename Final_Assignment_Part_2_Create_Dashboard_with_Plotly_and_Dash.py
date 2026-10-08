#!/usr/bin/env python
# coding: utf-8
"""
IBM Data Visualization with Python
Final Assignment: Part 2 - Create Dashboard with Plotly and Dash

Rubric-focused submission for Tasks 2.1-2.6.
The yearly statistics callback explicitly filters by input_year before
constructing the yearly report charts.
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

# Match field naming used across versions of the course material.
if "Unemployment_Rate" not in data.columns and "unemployment_rate" in data.columns:
    data["Unemployment_Rate"] = data["unemployment_rate"]
if "unemployment_rate" not in data.columns and "Unemployment_Rate" in data.columns:
    data["unemployment_rate"] = data["Unemployment_Rate"]

app = dash.Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"

# TASK 2.1 / 2.2
# Create the dropdown menu options.
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

year_list = [i for i in range(1980, 2024, 1)]

app.layout = html.Div([
    # TASK 2.1: Meaningful dashboard title
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 24}
    ),

    # TASK 2.2: Select Statistics dropdown
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Statistics',
            placeholder='Select Statistics'
        )
    ]),

    # TASK 2.2: Select Year dropdown
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=2020
        )
    ]),

    # TASK 2.3: Output container
    html.Div(
        id='output-container',
        className='chart-grid',
        style={'display': 'flex', 'flexDirection': 'column'}
    )
])

# TASK 2.4: Enable the year dropdown only for Yearly Statistics.
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    return True

# TASK 2.4 / 2.5 / 2.6: Update dashboard graphs.
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [
        Input(component_id='dropdown-statistics', component_property='value'),
        Input(component_id='select-year', component_property='value')
    ]
)
def update_output_container(selected_statistics, input_year):

    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # TASK 2.5 - Graph 1
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(figure=px.line(
            yearly_rec,
            x='Year',
            y='Automobile_Sales',
            title='Average Automobile Sales fluctuation over Recession Period'
        ))

        # TASK 2.5 - Graph 2
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(figure=px.bar(
            average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title='Average Number of Vehicles Sold by Vehicle Type'
        ))

        # TASK 2.5 - Graph 3
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(figure=px.pie(
            exp_rec,
            names='Vehicle_Type',
            values='Advertising_Expenditure',
            title='Total Expenditure Share by Vehicle Type During Recession'
        ))

        # TASK 2.5 - Graph 4
        unemp_rec = recession_data.groupby('Vehicle_Type')['Unemployment_Rate'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(
            unemp_rec,
            x='Vehicle_Type',
            y='Unemployment_Rate',
            title='Effect of Unemployment Rate on Vehicle Type and Sales'
        ))

        return [
            html.Div([R_chart1, R_chart2], style={'display': 'flex', 'flexWrap': 'wrap'}),
            html.Div([R_chart3, R_chart4], style={'display': 'flex', 'flexWrap': 'wrap'})
        ]

    if selected_statistics == 'Yearly Statistics' and input_year is not None:
        # IMPORTANT TASK 2.6 REQUIREMENT:
        # Filter the data by the selected input_year before creating yearly graphs.
        yearly_data = data[data['Year'] == input_year]

        # TASK 2.6 - Graph 1: yearly statistics for the selected year
        yas = yearly_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(
            yas,
            x='Year',
            y='Automobile_Sales',
            title=f'Automobile Sales in {input_year}'
        ))

        # TASK 2.6 - Graph 2
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(
            mas,
            x='Month',
            y='Automobile_Sales',
            title=f'Monthly Automobile Sales in {input_year}'
        ))

        # TASK 2.6 - Graph 3
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(
            avr_vdata,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title=f'Average Vehicles Sold by Vehicle Type in {input_year}'
        ))

        # TASK 2.6 - Graph 4
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(
            exp_data,
            names='Vehicle_Type',
            values='Advertising_Expenditure',
            title=f'Total Advertisement Expenditure per Vehicle Type in {input_year}'
        ))

        return [
            html.Div([Y_chart1, Y_chart2], style={'display': 'flex', 'flexWrap': 'wrap'}),
            html.Div([Y_chart3, Y_chart4], style={'display': 'flex', 'flexWrap': 'wrap'})
        ]

    return html.Div('Select a report type and year to display statistics.')


if __name__ == '__main__':
    app.run(debug=True)
