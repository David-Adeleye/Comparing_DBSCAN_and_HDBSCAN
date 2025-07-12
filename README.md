# Comparing DBSCAN and HDBSCAN for Clustering Geospatial Data

This project explores the effectiveness of two density-based clustering algorithms — **DBSCAN** and **HDBSCAN** — for grouping points of interest (e.g., museums) based on geospatial proximity.

It includes:
- Geospatial data clustering
- Visualizations on a Canada basemap
- Comparison of DBSCAN and HDBSCAN clustering behavior
- Reproducible and modular code structure
- Git LFS integration for managing large geospatial files

---

##  Project Structure
```bash

Comparing_DBSCAN_and_HDBSCAN/
│
├── data/ # Geospatial basemap (Canada.tif) — tracked with Git LFS
├── notebooks/ # Exploratory and final notebooks
├── src/ # Modular Python codes
│ ├── data_loader.py # Data loading 
│ └── plotter.py #  plotting logic
├── requirements.txt # Project dependencies
├── .gitattributes # Git LFS tracked files
├── .gitignore
└── README.md

```


## Getting Started

### 1. Clone the Repository

Make sure Git LFS is installed: https://git-lfs.com/

bash
git clone https://github.com/David-Adeleye/Comparing_DBSCAN_and_HDBSCAN.git
cd Comparing_DBSCAN_and_HDBSCAN
git lfs pull  # Downloads the large Canada basemap file
### 2. Set Up Virtual Environment
bash
Copy
python3 -m venv venv
source venv/bin/activate          # macOS/Linux

### 3. Install Dependencies
bash
Copy
pip install -r requirements.txt
### 4. How to Run
From Notebook
Open any .ipynb in the notebooks/ folder and run all cells.

## About the Basemap
The basemap (Canada.tif) is a large file and is tracked using Git LFS. It will not appear unless you’ve pulled it with git lfs pull.

You can replace it with another .tif file if you want to use a different region.

## Algorithms Used
DBSCAN  
Density-Based Spatial Clustering of Applications with Noise

Requires eps and min_samples

Cannot determine optimal clusters automatically

HDBSCAN  
Hierarchical DBSCAN

Works well with variable density

Does not require eps

## Libraries Used
scikit-learn

hdbscan

geopandas

contextily

matplotlib

shapely

## Acknowledgements
Dataset adapted from IBM's Generative AI course on clustering

Map overlays by Contextily