# core_solvers.py
from typing import Any


def solve_two_sum_core(validated_input: tuple[list[int], int]) -> Any:
    """Pure core logic - only mathematical transformation"""
    nums, target = validated_input
    # This is where the actual algorithm goes
    # For now, just a placeholder
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def solve_regex_core(validated_input: tuple[str, str]) -> Any:
    """Another core solver"""
    s, p = validated_input
    # Regex matching logic would go here
    return True  # placeholder
