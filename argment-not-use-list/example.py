from typing import Iterable

def love_messages(messages: Iterable) -> None:
    for message in messages:
        print(f"I love you {message}")

love_messages(["Python", "Django", "FastAPI"])

love_messages(("Python", "Django", "FastAPI"))
