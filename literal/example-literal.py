"""公式リファレンスのコードを写経
https://docs.python.org/ja/3/library/typing.html#typing.Literal
"""

from typing import Any, Literal

def validate_simple(data: Any) -> Literal[True]:  # always returns True
    ...

type Mode = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: Mode) -> str:
    ...

open_helper('/some/path', 'r')      # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker
