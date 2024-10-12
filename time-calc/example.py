# 時間の計算を行う

from datetime import datetime, timedelta

# 現在の日時を取得
# datetime.datetime(2024, 10, 6, 21, 30, 30, 405509) のようなdatetimeオブジェクトが返る
now = datetime.now()

# timedelta
# datetimeまたはdateのインスタンスの差（経過時間）を表す
delta = timedelta(
    days=1,
    seconds=2,
    microseconds=3,
    milliseconds=4,
    minutes=5,
    hours=6,
    weeks=7
)
delta  # datetime.timedelta(days=50, seconds=21902, microseconds=4003)
