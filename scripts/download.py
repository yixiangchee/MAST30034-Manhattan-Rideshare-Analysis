""" Downloads All Raw Data """

from urllib.request import urlretrieve
import zipfile
import os


# from the current `scripts` directory, go back one level to the main directory
OUTPUT_RELATIVE_DIR = './data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(OUTPUT_RELATIVE_DIR):
    os.makedirs(OUTPUT_RELATIVE_DIR)
# now, for each type of data set we will need, we will create the paths
for target_dir in ('tlc_data', 'tlc_test_data', 'rental_data'):
    if not os.path.exists(OUTPUT_RELATIVE_DIR + target_dir):
        os.makedirs(OUTPUT_RELATIVE_DIR + target_dir)

YEAR = '2021'
# adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc
MONTHS = range(1, 13)

# this is the URL template as of 07/2022
URL_TEMPLATE = \
    "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"

# tlc data output directory is `data/tlc_data/`
TLC_OUTPUT_DIR = OUTPUT_RELATIVE_DIR + 'tlc_data'

# download tlc data if folder is empty
if len(os.listdir(TLC_OUTPUT_DIR)) == 0:

    for month in MONTHS:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2)
        print(f"Begin month {month}")
        # generate url
        url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{TLC_OUTPUT_DIR}/{YEAR}-{month}.parquet"
        # download
        urlretrieve(url, output_dir)
        print(f"Completed month {month}")

# tlc test data output directory is `data/tlc_test_data/`
TLC_TEST_OUTPUT_DIR = OUTPUT_RELATIVE_DIR + 'tlc_test_data'

# download tlc prediction data if folder is empty
if len(os.listdir(TLC_TEST_OUTPUT_DIR)) == 0:

    print("Begin test data (2022-04)")
    # generate url
    url = f'{URL_TEMPLATE}2022-04.parquet'
    # generate output location and filename
    output_dir = f"{TLC_TEST_OUTPUT_DIR}/2022-04.parquet"
    # download
    urlretrieve(url, output_dir)

    print("Completed test data (2022-04)")

# rental data output directory is `data/rental_data/`
RENTAL_OUTPUT_DIR = OUTPUT_RELATIVE_DIR + 'rental_data'

URL_RENTAL = \
    "https://cdn-charts.streeteasy.com/rentals/All/medianAskingRent_All.zip"

# download rental data if folder is empty
if len(os.listdir(RENTAL_OUTPUT_DIR)) == 0:
    print("Begin rental data")

    # generate output location and filename
    output_dir = f"{RENTAL_OUTPUT_DIR}/medianAskingRent_All.zip"

    # download
    urlretrieve(URL_RENTAL, output_dir)

    with zipfile.ZipFile(output_dir, "r") as zip_ref:
        zip_ref.extractall(RENTAL_OUTPUT_DIR)

    print("Completed rental data")
