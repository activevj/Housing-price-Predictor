import os
import tarfile
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt



def fetch_housing_data(housing_url,housing_path,tgz_path):
    """Fetching Data from the website

    Args:
        housing_url (string, optional): Provide string to fetch housing data from the url. Defaults to HOUSING_URL.
        housing_path (string, optional): Provide File directory to fetch to you desired location. Defaults to HOUSING_PATH.
    """
    if not os.path.exists(housing_path):
        os.makedirs(housing_path)
    urllib.request.urlretrieve(housing_url,tgz_path)
    housing_tgz=tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path):
    """To load the housing data from the given path

    Args:
        housing_path (string): To load the housing data from given local directory path

    Returns:
        Datafram: return the data frame back to calling function after loading the data
    """
    csv_path=os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)
    


