# pipelines.py
from functools import reduce
from typing import Any, Callable


def compose(*functions: Callable) -> Callable:
    """Haskell-style function composition: f(g(x))"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def build_output_pipe(contract: ProblemContract) -> Callable:
    """Working backward: final output formatting"""
    if contract.output_spec == "list[int]":
        return ensure_list_int
    elif contract.output_spec == "boolean":
        return ensure_boolean
    elif contract.output_spec == "ListNode":
        return format_linked_list
    return identity


def build_input_pipe(contract: ProblemContract) -> Callable:
    """Working forward: input parsing and validation"""
    if contract.input_spec == "list[int], int":
        return validate_two_sum_input
    elif contract.input_spec == "list[ListNode]":
        return validate_merge_k_lists_input
    return identity


# Simple, pure transformer functions
def ensure_list_int(result: Any) -> list[int]:
    return list(map(int, result)) if hasattr(result, "__iter__") else [int(result)]


def ensure_boolean(result: Any) -> bool:
    return bool(result)


def identity(x: Any) -> Any:
    return x


def validate_two_sum_input(raw_input: tuple[list[int], int]) -> tuple[list[int], int]:
    nums, target = raw_input
    return (list(nums), int(target))
