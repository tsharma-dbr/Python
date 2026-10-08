
import sqlite3
import pandas as pd

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"

def run_sql_analysis(csv_path=None):
    df = pd.read_csv(csv_path) if csv_path else pd.read_csv(DATA_URL)
    conn = sqlite3.connect(":memory:")
    df.to_sql("SPACEXTBL", conn, index=False, if_exists="replace")
    queries = {
        "top_20": "SELECT * FROM SPACEXTBL LIMIT 20",
        "minimum_payload": "SELECT MIN(PayloadMass) AS Minimum_Payload_Mass FROM SPACEXTBL",
        "total_payload": "SELECT SUM(PayloadMass) AS Total_Payload_Mass FROM SPACEXTBL",
        "launch_site_counts": """
            SELECT LaunchSite, COUNT(*) AS launch_count
            FROM SPACEXTBL
            GROUP BY LaunchSite
            ORDER BY launch_count DESC
        """
    }
    return {name: pd.read_sql(q, conn) for name, q in queries.items()}

if __name__ == "__main__":
    for name, result in run_sql_analysis().items():
        print(f"\n{name}\n")
        print(result.to_string(index=False))
