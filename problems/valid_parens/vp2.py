class Solution:
    match_map = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            if char not in self.match_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != self.match_map[char]:
                    return False
        return not stack


def main():
    # t1 = "()[]"
    t2 = "{(])}"
    s = Solution()
    result = s.is_valid(t2)
    print(f"Input: {t2} Output: {result}")


if __name__ == "__main__":
    main()
