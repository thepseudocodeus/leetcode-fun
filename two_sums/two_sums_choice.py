import time
from typing import List, Optional
from enum import Enum
import timeit

class Choice(Enum):
    BRUTE = 0
    MAP = 1


def brute_force(nums: List[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []


def map_solution(nums: List[int], target: int) -> list[int]:
    seen = {}
    print(f"List: {nums}")
    print(f"Target: {target}")
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[num] = index
    return []


def process(nums: List[int], target: int, choice: Enum) -> Optional[List[int]]:
    match choice:
        case Choice.BRUTE:
            t1 = timeit.default_timer()
            result = brute_force(nums, target)
            t2 = timeit.default_timer()
            print(f"Brute force took {t2-t1} seconds")
            return result
        case Choice.MAP:
            t1 = timeit.default_timer()
            result = map_solution(nums, target)
            t2 = timeit.default_timer()
            print(f"Map solution took {t2-t1} seconds")
            return result
        case _:
            raise ValueError("Invalid choice")


def TwoSum(nums: List[int], target: int) -> List[int]:
    choice = input("Enter your choice (BRUTE/MAP): ").upper()
    match choice:
        case "BRUTE":
            choice = Choice.BRUTE
        case "MAP":
            choice = Choice.MAP
        case _:
            raise ValueError("Invalid choice")
    result = process(nums, target, choice) or []
    if result is None:
        raise ValueError("No solution found")
    return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(TwoSum(nums, target))
