from enum import Enum
from typing import Literal
class COLOR(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

colors = Literal[COLOR.RED, COLOR.GREEN, COLOR.BLUE]

def process_color(color: colors) -> None:
    pass
# str
red = "red"

# color型
enum_red = COLOR.RED

# str
enum_red_value = COLOR.RED.value

process_color(color=red)  # Error: Argument 1 to "process_color" has incompatible type "str"; expected "Literal[COLOR.RED, COLOR.GREEN, COLOR.BLUE]"
