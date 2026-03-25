import zipfile
import os

zip_path = "data.zip"
extract_to = "data"

if not os.path.exists(zip_path):
    raise FileNotFoundError("data.zip not found in project folder")

os.makedirs(extract_to, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Dataset extracted successfully to 'data/' folder")