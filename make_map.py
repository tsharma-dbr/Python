
import pandas as pd
import folium
from folium.plugins import MarkerCluster

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv"

def build_launch_map(csv_path=None, output_html="spacex_launch_map.html"):
    geo = pd.read_csv(csv_path) if csv_path else pd.read_csv(DATA_URL)
    m = folium.Map(
        location=[geo["Latitude"].mean(), geo["Longitude"].mean()],
        zoom_start=4
    )
    cluster = MarkerCluster().add_to(m)
    for _, row in geo.iterrows():
        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            popup=str(row.get("Launch Site", "Launch Site"))
        ).add_to(cluster)
    m.save(output_html)
    return output_html

if __name__ == "__main__":
    print(build_launch_map())
