import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os
from pprint import pprint
# from flaskr.repogitories import getFromDatabase as db
from flask import request

# 環境変数の読み込み
load_dotenv()

APPLICATION_ID = os.getenv('APPLICATION_ID')
ACCESS_KEY = os.getenv('ACCESS_KEY')
CATEGORY_API_URL = os.getenv('CATEGORY_API_URL')
BASE_URL = os.getenv('BASE_URL')

# リクエストパラメータの設定
headers = {
    'Origin': BASE_URL,
    'Referer': BASE_URL + '/'
}

params = {
    'applicationId': APPLICATION_ID,   
    'accessKey': ACCESS_KEY,
    'format': 'json'
}


def get_category_list() -> pd.DataFrame:
    res = requests.get(
            CATEGORY_API_URL, 
            headers=headers,
            params=params,
        )

    json_data = res.json()
    return json_data

def convert_name_to_id(category_name: str) -> int:
    pass

def get_recipe_ranking(category_id: int) -> pd.DataFrame:
    pass

def filter_by_ingredient(ingredient_name: str) -> pd.DataFrame:
    pass

pprint(get_category_list())