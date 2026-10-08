
"""
SpaceX Falcon 9 Interactive Dashboard
IBM Applied Data Science Capstone

Run:
    python spacex_dash_app.py

Then open the local Dash URL shown in the terminal.
"""

from pathlib import Path
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
LOCAL_FILE = Path("spacex_launch_dash.csv")

if LOCAL_FILE.exists():
    spacex_df = pd.read_csv(LOCAL_FILE)
else:
    spacex_df = pd.read_csv(DATA_URL)

max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

app = dash.Dash(__name__)

launch_sites = sorted(spacex_df["Launch Site"].dropna().unique().tolist())
dropdown_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": s, "value": s} for s in launch_sites
]

app.layout = html.Div([
    html.H1(
        "SpaceX Falcon 9 Launch Dashboard",
        style={"textAlign": "center"}
    ),
    html.Div([
        html.Label("Select Launch Site:"),
        dcc.Dropdown(
            id="site-dropdown",
            options=dropdown_options,
            value="ALL",
            clearable=False
        )
    ]),
    html.Br(),
    html.Div([
        html.Label("Payload Mass (kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=min_payload,
            max=max_payload,
            value=[min_payload, max_payload],
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ]),
    html.Br(),
    dcc.Graph(id="success-pie-chart"),
    dcc.Graph(id="payload-scatter")
])

@app.callback(
    Output("success-pie-chart", "figure"),
    Output("payload-scatter", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value")
)
def update_dashboard(selected_site, payload_range):
    low, high = payload_range
    filtered = spacex_df[
        spacex_df["Payload Mass (kg)"].between(low, high, inclusive="both")
    ].copy()

    if selected_site != "ALL":
        filtered = filtered[filtered["Launch Site"] == selected_site]

    if filtered.empty:
        pie = px.pie(title="No records match the selected filters")
        scatter = px.scatter(title="No records match the selected filters")
        return pie, scatter

    counts = filtered["class"].value_counts().rename_axis("class").reset_index(name="count")
    pie = px.pie(
        counts,
        names="class",
        values="count",
        title="Launch Success Outcome"
    )

    scatter = px.scatter(
        filtered,
        x="Flight Number",
        y="Payload Mass (kg)",
        color="class",
        title="Flight Number vs Payload Mass"
    )
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)
