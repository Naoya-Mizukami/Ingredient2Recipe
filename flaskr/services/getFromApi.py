import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os
from pprint import pprint
from flask import request

# 環境変数の読み込み
load_dotenv()

APPLICATION_ID = os.getenv('APPLICATION_ID')
ACCESS_KEY = os.getenv('ACCESS_KEY')
CATEGORY_URL = os.getenv('CATEGORY_URL')
RECIPE_RANKING_URL = os.getenv('RECIPE_RANKING_URL')
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
    '''
    カテゴリーリストを取得する関数
    '''

    # カテゴリーリストをAPIから取得
    res = requests.get(
            CATEGORY_URL, 
            headers=headers,
            params=params,
        )
    json_data = res.json()

    # 大カテゴリ
    list_large = []
    for category in json_data['result']['large']:
        list_large.append([
                category['categoryId'], 
                "", 
                "", 
                category['categoryId'], 
                category['categoryName']
            ])

    # 中カテゴリ
    list_medium = []
    for category in json_data['result']['medium']:
        list_medium.append([
                category['parentCategoryId'], 
                category['categoryId'], 
                "", 
                str(category['parentCategoryId'])+"-"+str(category['categoryId']), 
                category['categoryName']
            ])

    # 小カテゴリ
    list_small = []
    for category in json_data['result']['small']:
        list_small.append([
                category['parentCategoryId'], 
                category['categoryId'], 
                "", 
                str(category['parentCategoryId'])+"-"+str(category['categoryId']), 
                category['categoryName']
            ])

    # DataFrameに変換
    columns = ['category1','category2','category3','category_id','category_name']
    df_large = pd.DataFrame(data=list_large, columns=columns)
    df_medium = pd.DataFrame(data=list_medium, columns=columns)
    df_small = pd.DataFrame(data=list_small, columns=columns)

    # すべてのカテゴリを結合
    df_category_list = pd.concat([df_large, df_medium, df_small], ignore_index=True)

    return df_category_list


def convert_name_to_id(category_name: str) -> int:
    pass


def get_recipe_ranking(category_id: int) -> pd.DataFrame:
    '''
    レシピランキングを取得する関数
    '''

    # カテゴリーIDをリクエストパラメータに追加
    params['categoryId'] = category_id

    # レシピランキングをAPIから取得
    res = requests.get(
            RECIPE_RANKING_URL, 
            headers=headers,
            params=params,
        )

    json_data = res.json()

    # レシピランキングのリストを作成
    list = []
    for item in json_data['result']:
        list.append([
                item['recipeId'], 
                item['recipeTitle'], 
                item['recipeUrl'], 
                item['foodImageUrl'],
                item['mediumImageUrl'],
                item['smallImageUrl'], 
                item['recipeMaterial'],
                item['recipeIndication'],
                item['recipeCost'],
                item['rank']
            ])

    # DataFrameに変換
    columns = [
            'recipe_id',
            'recipe_title',
            'recipe_url',
            'food_image_url',
            'medium_image_url',
            'small_image_url',
            'recipe_material',
            'recipe_indication',
            'recipe_cost',
            'rank'
        ]
    df_recipe_ranking = pd.DataFrame(data=list, columns=columns)

    return df_recipe_ranking

def filter_by_ingredient(ingredient_name: str) -> pd.DataFrame:
    pass

pprint(get_recipe_ranking(10))