# MAST30034 Project 1
## Quantitative Analysis of Rideshare Services in Post-Covid Manhattan 🏙

**Score:** 29/30

**Research Goal:** Study the relationship between **rideshare pickup** and **rent** in Manhattan, then use the results to build models for demand forecasting.

**Timeline:** The timeline for the research area is the whole year of 2021.

**Models used:** [RandomForestRegressor](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.regression.RandomForestRegressor.html), [LinearRegression](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.regression.LinearRegression.html)

**Python Version:** 3.8.2

**Models used:** PySpark

[**Report**](https://www.overleaf.com/read/wcqtyychqkkw)

## Getting Started:
To run the pipeline, please visit the directories and run the files in order:

`/scripts`

1. `download.py`: This downloads the raw data into the `data/raw` directory.

`/notebooks`

2. `preprocessing_notebook_part_1.ipynb`: This notebook performs **data linkage**, **outlier removal**, **filtering**, and outputs it to the `data/curated/full_data` directory.

3. `preprocessing_notebook_part_2.ipynb`: This notebook performs **aggregation** for analysis and modelling and outputs it to the `data/curated/analysis` and `data/curated/modelling` directories.

3. `data_analysis.ipynb`: This notebook is used to conduct **analysis** and **visualisation** on the curated data.

4. `model_analysis.ipynb`: This notebook is used for **training, analysing and discussing the models**.

## Datasets:

[TLC Trip Record Data (HVFHS)](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

[NYC Rent Data](https://streeteasy.com/blog/data-dashboard/)
