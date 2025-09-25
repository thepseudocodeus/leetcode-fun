from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")

"""
Examples
Input: "list[int], int"
Output:  "list[int]"
Key Invariant: "complement_exists"
"""


@dataclass(frozen=True)
class ProblemContract:
    input_spec: str
    output_spec: str
    key_invariant: str


@dataclass(frozen=True)
class Pipeline:
    steps: tuple[Callable, ...]
    description: str
