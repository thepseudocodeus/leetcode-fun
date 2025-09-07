import dataclasses
import os
from dataclasses import dataclass


# [] TODO: learn more about dataclasses and how to use them
# [] TODO: learn more about the frozen attribute
@dataclass(frozen=True)
class Env:
    my_name: str
    my_age: int
