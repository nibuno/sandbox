from typing import TypeVar

# リファレンス
# https://docs.python.org/ja/3/library/typing.html#typing.TypeVar

# 一番シンプルな定義
# Can be anything とのことで、なんでもあり得るということ
T = TypeVar("T")

# Can be any subtype of str とのこと
S = TypeVar("S", bound=str)

# Must be exactly str or bytes とのこと
A = TypeVar("A", str, bytes)
