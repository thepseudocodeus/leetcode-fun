class Solution:
    match_map = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        return self.process(s)

    def is_even(self, x):
        return x % 2 == 0

    def is_odd(self, x):
        return not self.is_even(x)

    def str_len(self, astring):
        return len(astring)

    def is_match(self, left, right):
        print(f"Left: {left}")
        print(f"right: {right}")
        print(f"compare: {left} vs {self.match_map[right]}")
        return left == self.match_map[right]

    def get_right_index(self, astring):
        return int(self.str_len(astring) // 2)

    def get_left_index(self, astring):
        return self.get_right_index(astring) - 1

    def get_centers(self, astring: str) -> tuple[int, int]:
        return (self.get_left_index(astring), self.get_right_index(astring))

    def step(self, end: int):
        half_len = int(end // 2)
        for i in range(0, half_len - 1):
            yield i

    def process(self, param: str) -> bool:
        if param == "":
            return False

        slen = self.str_len(param)
        # print(f"length: {slen}")

        if slen < 2:
            return False

        if self.is_odd(slen):
            return False

        if slen == 2:
            return param[0] == self.match_map[param[1]]

        left_index, right_index = self.get_centers(param)
        print(f"l index: {left_index} | r index: {right_index}")
        count_generator = self.step(slen)
        for count in count_generator:
            left_value = param[left_index]
            right_value = param[right_index]
            if not self.is_match(left_value, right_value):
                return False
            left_index -= count
            right_index += count
        return True


def main():
    # t1 = "{([])}"
    # t2 = "([{]}])"
    t3 = "(]"
    solve = Solution()
    result = solve.process(t3)
    print(f"{t3} result {result}")
    # assert result, "Expect everything to close in this example."
    assert not result, "Don't expect everything to close in this example."


if __name__ == "__main__":
    main()
