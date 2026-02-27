import os

folders = [
    "Data-Analytics-Portfolio/Excel-Projects",
    "Data-Analytics-Portfolio/SQL-Projects",
    "Data-Analytics-Portfolio/Python-Projects",
    "Data-Analytics-Portfolio/PowerBI-Dashboards",
    "Data-Analytics-Portfolio/Tableau-Dashboards",
    "Data-Analytics-Portfolio/Datasets"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folder structure created successfully!")

