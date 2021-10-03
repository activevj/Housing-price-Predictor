import os
from utils.all_utils import fetch_housing_data,load_housing_data
import tarfile
import urllib.request



def main(download_root,housing_path,housing_url,tgz_path):
    fetch_housing_data(housing_url,housing_path,tgz_path)
    housing=load_housing_data(housing_path)





if __name__ == '__main__':
    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
    HOUSING_PATH=os.path.join("datasets","housing")
    HOUSING_URL=DOWNLOAD_ROOT+"datasets/housing/housing.tgz"
    tgz_path=os.path.join(HOUSING_PATH,"housing.tgz")
    main(DOWNLOAD_ROOT,HOUSING_PATH,HOUSING_URL,tgz_path)



