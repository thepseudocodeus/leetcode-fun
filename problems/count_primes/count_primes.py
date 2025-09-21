#!/usr/bin/env python3
from typing import Dict, Tuple


"""
Hypothesis:
1. Brute force =
- starting at 2, set count = 1
- set end in range = N
- for each n in N check if current n divisible by any of our past primes:
    - if it is then move to next number
    - if not, add this number as a prime to our prime cache


- decompose the problem using recusrion
- use rules of divisibility to shortcut work
"""


class Solution:

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        return self.run(n)

    def run(self, n: int) -> int:
        PRIMES = {
            2: 1,
            3: 1,
            5: 1,
            7: 1,
            11: 1,
            13: 1,
            17: 1,
            19: 1,
            23: 1,
        }

        PRIME_COUNTS = {
            0: 0,
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
            6: 3,
            7: 3,
            8: 4,
            9: 4,
            10: 4,
            11: 4,
            12: 5,
        }
        count = 0
        try:
            # [x] TODO: is number in existing counts?

            if PRIME_COUNTS[n]:
                return PRIME_COUNTS[n]

        except Exception:
            pass

        for n in range(2, n):
            result, PRIMES = self.maybe_prime(n, PRIMES)
            if result:
                count += 1

        return count

    def maybe_prime(self, n: int, prime_map: Dict[int, int]) -> Tuple[bool, Dict[int, int]]:

        result, prime_map = self.is_known_prime(n, prime_map)
        if result:
            return True, prime_map

        # [ ] TODO: is it divisible by a known prime?
        # [ ] TODO: starting from + 1 from the last counted number
        for k, _ in prime_map.items():
            if k > n:
                continue
            if n % k == 0:
                return True, prime_map

        return False, prime_map

    def is_known_prime(self, n: int, prime_map: dict) -> bool:
        """"""
        # [ ] TODO: how to check if a number is prime?
        # [ ] TODO: is this a known prime? (in prime map)
        try:
            if prime_map[n]:
                return True
        except Exception:
            return False

        return False
