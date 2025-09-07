from typing import List


def TwoSum(nums: List[int], target: int) -> List[int]:
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
