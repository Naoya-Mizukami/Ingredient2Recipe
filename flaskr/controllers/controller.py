from flaskr import app
from flask import render_template
import pandas as pd
import services.getFromApi as getFromApi

@app.route("/")
def home():
    df_category = getFromApi.get_category_list()
    return render_template(
            "home.html", 
            category_id = df_category['category_id'],
            category_name = df_category['category_name']
        )

@app.route("/mylist")
def mylist():
    return render_template("mylist.html")