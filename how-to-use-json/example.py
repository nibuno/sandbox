import json

from pathlib import Path

def load_survey_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# JSONファイルのパスを指定
# 同じディレクトリ上にあるexample.jsonを指定
file_path = Path(__file__).parent / "example.json"

# データを読み込み
survey_data = load_survey_data(file_path)

# アンケートの質問と回答を表示
import pprint
pprint.pprint(survey_data)

# 以下のような出力結果になる
"""
{'survey': {'questions': [{'id': 1, 'text': 'あなたがこのイベントに来たきっかけはなんですか？'},
                          {'id': 2, 'text': 'あなたは今日はどこから来ましたか？'}],
            'responses': [{'answers': {'1': '公式SNSで知ったから', '2': '愛知県'},
                           'user_id': 'user_001'},
                          {'answers': {'1': '近くでやっていたから', '2': '和歌山県'},
                           'user_id': 'user_002'}]}}

"""

# dictになる
print(type(survey_data))
