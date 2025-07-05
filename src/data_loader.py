import os
import io
import zipfile
import requests
import pandas as pd
import chardet
from io import StringIO

def download_and_extract_tif(zip_file_url, output_dir=None):
    """
    Downloads and extracts a .tif file from a zip archive.

    Parameters:
    - zip_file_url: str, URL to the ZIP file containing the .tif
    - output_dir: str or None, directory to extract the .tif file to.
                  If None, it defaults to ../data relative to the current working directory.

    Returns:
    - Full path to the extracted .tif file if found, else None
    """
    if output_dir is None:
        # Resolve output_dir dynamically at call time
        output_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'data'))

    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(zip_file_url)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.tif'):
                zip_ref.extract(file_name, output_dir)
                print(f"Downloaded and extracted: {file_name}")
                return os.path.join(output_dir, file_name)

    print("No .tif file found in the ZIP.")
    return None


def load_museum_data(csv_url):
    """
    Loads the museum dataset from a given CSV URL with auto-detected encoding.

    Parameters:
    - csv_url: str, URL of the CSV file

    Returns:
    - DataFrame containing the loaded data
    """
    response = requests.get(csv_url)
    response.raise_for_status()

    encoding = chardet.detect(response.content)['encoding']
    print(f"Detected encoding: {encoding}")

    decoded_csv = StringIO(response.content.decode(encoding))
    df = pd.read_csv(decoded_csv)

    return df
