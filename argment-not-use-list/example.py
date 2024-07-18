from typing import Iterable

# IterableでもOK
# Iterable[str]でもOK
def love_messages(messages: Iterable[str]) -> None:
    for message in messages:
        print(f"I love you {message}")

love_messages(["Python", "Django", "FastAPI"])

love_messages(("Python", "Django", "FastAPI"))
