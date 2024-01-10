"""Marvin is (and was originally conceived as) a functional way to generate prompts
for an LLM, with type-safe outputs that can be used in traditional Python code.
"""

import json
import marvin
import time
from typing_extensions import TypedDict

@marvin.fn
def list_fruit(n: int) -> list[str]:
    """generate a list of `n` fruits"""

fruits = list_fruit(3)

assert isinstance(fruits, list)
assert len(fruits) == 3
assert all(isinstance(fruit, str) for fruit in fruits)

print(f"\nWe asked for a `list[str]` and got a `{type(fruits).__name__}` {fruits=!r}")

time.sleep(2)

class Fruit(TypedDict):
    name: str
    color: str

print(
    "\nLet's be more specific and ask for a `list[Fruit]`"
    " where `Fruit` is a `TypedDict` with `name: str` and `color: str` fields"
)

@marvin.fn
def list_fruit(n: int) -> list[Fruit]:
    """generate a list of `n` fruits"""

new_fruits = list_fruit(3)

assert isinstance(new_fruits, list)
assert len(new_fruits) == 3
assert all(isinstance(fruit, dict) for fruit in new_fruits)

print(
    f"\nWe asked for a `list[Fruit]` and got a `{type(new_fruits).__name__}`"
    f" new_fruits={json.dumps(new_fruits, indent=2)}"
)
