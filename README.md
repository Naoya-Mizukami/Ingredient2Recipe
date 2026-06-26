# Ingredient2Recipe

Ingredient2Recipe は、楽天レシピAPIを利用してカテゴリ別のレシピランキングを表示する Flask アプリケーションです。

トップページで「大分類」「中分類」「小分類」を選択し、選択したカテゴリに応じたレシピランキングを確認できます。最低限、大分類だけ選択すればランキングを表示できます。

サイトURL: https://ingredient2recipe.onrender.com/

## 主な機能

- 楽天レシピカテゴリ一覧APIからカテゴリを取得
- 大分類・中分類・小分類の3段階カテゴリ選択
- 選択カテゴリに対応したレシピランキング表示
- レシピ画像、順位、調理時間、費用、材料、レシピURLの表示
- スマートフォンでも選択肢が正しく絞り込まれるカテゴリ選択UI

## 使用技術

- Python 3.12
- Flask
- Jinja2
- pandas
- requests
- python-dotenv
- gunicorn

依存関係は `pyproject.toml` で管理しています。

## ディレクトリ構成

```text
Ingredient2Recipe/
├── main.py
├── flaskr/
│   ├── __init__.py
│   ├── controllers/
│   │   └── controller.py
│   ├── services/
│   │   └── getFromApi.py
│   └── templates/
│       ├── home.html
│       ├── home.js
│       ├── recipes.html
│       └── style.css
├── README.md
├── 仕様書.md
└── pyproject.toml
```

## 画面

### カテゴリ選択画面

URL: `/`

楽天レシピAPIから取得したカテゴリを、大分類・中分類・小分類の3段階で選択します。

### レシピランキング画面

URL: `/recipes`

選択したカテゴリIDをもとに、楽天レシピカテゴリ別ランキングAPIからレシピ一覧を取得して表示します。

## 環境変数

`.env` に以下の値を設定します。

| 変数名 | 説明 |
| --- | --- |
| `APPLICATION_ID` | 楽天APIのアプリケーションID |
| `ACCESS_KEY` | 楽天APIのアクセスキー |
| `CATEGORY_URL` | 楽天レシピカテゴリ一覧APIのURL |
| `RECIPE_RANKING_URL` | 楽天レシピカテゴリ別ランキングAPIのURL |
| `BASE_URL` | アプリケーションのベースURL |

## 起動方法

依存関係をインストールしたうえで、以下を実行します。

```bash
python main.py
```

Flaskの開発サーバーが起動し、ローカル環境でアプリを確認できます。

## 仕様書

詳細な画面仕様、ルーティング仕様、API連携仕様は [仕様書.md](./仕様書.md) を参照してください。

## 補足

現在、以下の関数は未実装です。

- `convert_name_to_id()`
- `filter_by_ingredient()`

また、API通信失敗時の例外処理やカテゴリ一覧のキャッシュは今後の改善候補です。