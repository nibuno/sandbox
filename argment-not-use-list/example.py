# NOTE: typing.IterableはPython3.9から非推奨のようだった
# https://docs.python.org/ja/3/library/typing.html#typing.Iterable
# from typing import Iterable

# 代わりに、collections.abc.Iterableを使えば良いようだった
from collections.abc import Iterable

# IterableでもOK
# Iterable[str]でもOK
def love_messages(messages: Iterable[str]) -> None:
    for message in messages:
        print(f"I love you {message}")

love_messages(["Python", "Django", "FastAPI"])

love_messages(("Python", "Django", "FastAPI"))
