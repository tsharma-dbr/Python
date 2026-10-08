# SpaceX Falcon 9 Data Science Capstone — Completed Project Files

## Project title
**SpaceX Falcon 9 Launch Analytics: Predicting First-Stage Landing Success**

## Included files
- `01_spacex_data_collection_api.ipynb`
- `02_spacex_webscraping.ipynb`
- `03_spacex_data_wrangling.ipynb`
- `04_eda_sql.ipynb`
- `05_eda_visualization.ipynb`
- `06_launch_site_location_folium.ipynb`
- `07_machine_learning_prediction.ipynb`
- `spacex_dash_app.py`
- `make_map.py`
- `make_sql.py`
- `requirements.txt`

## Official course datasets
The notebooks default to the IBM Skills Network SpaceX course datasets:

- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv
- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv
- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv
- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv
- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv

## Verified capstone checkpoints incorporated
- Falcon 9 analytical records: **90**
- CCAFS SLC 40 launches: **55**
- Landing success rate: **67%**
- Missing LandingPad values: **26**
- GEO launches: **1**
- Successful drone-ship landing outcomes: **41**
- One-hot encoded feature columns: **80**
- Test sample: **18**
- SVM validation kernel: **linear**
- Tuned Decision Tree test accuracy: **83.33%**

## Dashboard
Run:

```bash
python -m pip install -r requirements.txt
python spacex_dash_app.py
```

## Reproducibility note
The live SpaceX API can evolve. For course grading, the notebooks also point to the stable IBM Skills Network course datasets used by the capstone. The predictive results reported in the notebooks are the verified course-task results from the work completed for this capstone.
