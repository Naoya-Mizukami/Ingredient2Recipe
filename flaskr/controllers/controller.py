from flaskr import app
from flask import render_template
import pandas as pd
import flaskr.services.getFromApi as getFromApi

@app.route("/")
def home():
    # ホーム画面（）
    # カテゴリーリストを取得する関数
    df_category = getFromApi.get_category_list()

    df_category2 = df_category[['category2', 'category_name']][(df_category['category2'] != '') & (df_category['category3'] == '')]
    id_name_pairs_2 = set(df_category2.itertuples(index=False, name=None))

    df_category3 = df_category[['category2','category3', 'category_name']][(df_category['category3'] != '')]
    id_name_pairs_3 = set(df_category3.itertuples(index=False, name=None))

    return render_template(
        "home.html", 
        id_name_pairs_2 = id_name_pairs_2,
        id_name_pairs_3 = id_name_pairs_3
    )

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")