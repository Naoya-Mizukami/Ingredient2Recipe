from flaskr import app
from flask import render_template, request, send_from_directory
import pandas as pd
import flaskr.services.getFromApi as getFromApi

@app.route("/")
def home():
    # ホーム画面（）
    # カテゴリーリストを取得する関数
    df_category = getFromApi.get_category_list()

    df_category1 = df_category[['category_id', 'category_name']][(df_category['category2'] == '') & (df_category['category3'] == '')]
    id_name_pairs_1 = set(df_category1.itertuples(index=False, name=None))

    df_category2 = df_category[['category1', 'category_id', 'category_name']][(df_category['category2'] != '') & (df_category['category3'] == '')]
    id_name_pairs_2 = set(df_category2.itertuples(index=False, name=None))

    df_category3 = df_category[['category1', 'category2', 'category_id', 'category_name']][(df_category['category3'] != '')].copy()
    df_category3['parent_category_id'] = df_category3['category1'].astype(str) + '-' + df_category3['category2'].astype(str)
    id_name_pairs_3 = set(df_category3[['parent_category_id', 'category_id', 'category_name']].itertuples(index=False, name=None))

    return render_template(
        "home.html",
        id_name_pairs_1 = id_name_pairs_1,
        id_name_pairs_2 = id_name_pairs_2,
        id_name_pairs_3 = id_name_pairs_3
    )


@app.route("/home.js")
def home_js():
    return send_from_directory(app.template_folder, "home.js")


@app.route("/style.css")
def style_css():
    return send_from_directory(app.template_folder, "style.css")

@app.route("/recipes")
def recipes():
    selected_category_id = (
        request.args.get("category3_id")
        or request.args.get("category2_id")
        or request.args.get("category1_id")
        or ""
    )
    recipe_list = []

    if selected_category_id:
        df_recipe_ranking = getFromApi.get_recipe_ranking(selected_category_id)
        recipe_list = df_recipe_ranking.to_dict(orient="records")

    return render_template(
        "recipes.html",
        selected_category_id = selected_category_id,
        recipes = recipe_list
    )