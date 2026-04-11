import pandas as pd
import requests
import json
import yaml
from pprint import pprint
# from flaskr.repogitories import getFromDatabase as db
from flask import request

with open('flaskr/config.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    APPLICATION_ID = config['APPLICATION_ID']
    ACCESS_KEY = config['ACCESS_KEY']
    CATEGORY_API_URL = config['CATEGORY_API_URL']

headers = {
    'accessKey': ACCESS_KEY,
    'Referer': 'example.com'
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