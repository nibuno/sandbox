"""公式リファレンスのコードを写経
https://docs.python.org/ja/3/library/typing.html#typing.Literal
"""

from typing import Any, Literal, TypeAlias

def validate_simple(data: Any) -> Literal[True]:  # always returns True
    return True

# Python3.12で追加された書き方
# ただし、mypy側では未対応な様子
# https://stackoverflow.com/questions/78311150/mypy-error-pep-695-type-aliases-are-not-yet-supported
type Mode = Literal['r', 'rb', 'w', 'wb']

# mypy1.10.1で対応するための書き方その1
# Mode = Literal['r', 'rb', 'w', 'wb']

# mypy1.10.1で対応するための書き方その2
# TypeAliasでもOK
# NOTE: ただし、Python3.12では非推奨になっており
# type文が推奨されている様子
# https://docs.python.org/ja/3/library/typing.html#typing.TypeAlias
# Mode: TypeAlias = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: Mode) -> str:
    return "True"

open_helper('/some/path', 'r')      # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker

# Literalには以下の値が定義できる
# * 文字列
# * 数値
# * bool
# * None
# * Enum
# * その他のリテラル型

Literal['r', 'rb', 'w', 'wb']
Literal[1, 2, 3]
Literal[True, False]
Literal[None]

# floatは使えない
Literal[1.0, 2.0, 3.0]
