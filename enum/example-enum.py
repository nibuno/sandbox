from enum import Enum
from typing import Literal
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

colors = Literal[Color.RED, Color.GREEN, Color.BLUE]

def process_color(color: colors) -> None:
    pass
# str
red = "red"

# color型
enum_red = Color.RED

# str
enum_red_value = Color.RED.value

process_color(color=red)  # Error: Argument 1 to "process_color" has incompatible type "str"; expected "Literal[COLOR.RED, COLOR.GREEN, COLOR.BLUE]"
