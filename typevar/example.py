from typing import TypeVar, Sequence

# リファレンス
# https://docs.python.org/ja/3/library/typing.html#typing.TypeVar

# 一番シンプルな定義
# Can be anything とのことで、なんでもあり得るということ
T = TypeVar("T")

# Can be any subtype of str とのこと
S = TypeVar("S", bound=str)

# Must be exactly str or bytes とのこと
A = TypeVar("A", str, bytes)

# TypeVarは、Python3.5から追加されているみたい
# 型変数はtype checkers(例えばmypy)などの恩恵を受けることができる
# https://docs.python.org/3.5/library/typing.html#typing.TypeVar
# 関連するPEPはこの辺りの様子
# https://peps.python.org/pep-0484/
# https://peps.python.org/pep-0695/

def repeat[T](x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x.

    xへのn個の参照を含むリストを返す
    """
    return [x] * n
