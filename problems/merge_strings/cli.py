# import inquirerpy

from typing import Generator

PROBLEM_SETS = {
    1: {"input": ["abc", "pqr"], "expect": "apbqcr"},
    2: {"input": ["ab", "pqrs"], "expect": "apbprs"},
    3: {
        "input": ["abcd", "pq"],
        "expect": "apbqcd",
    },
}


def show(input: any) -> None:
    print(f"{input}")


def _process_problem(input: tuple) -> bool:
    w1, w2, exp = input
    result = w1 + w2
    return result == exp


def _get_words(L: list) -> tuple:
    return (L[0], L[1])


def _process_dict(adict: dict) -> any:
    output = []
    for k, v in adict.items():
        w1, w2 = _get_words(v)
        exp = adict[k]["expect"]
        output.append(_process_problem((w1, w2, exp)))
    return output


def process_all(adict: dict) -> bool:
    output = False
    for k, v in adict.items():
        w1, w2 = v["input"]
        exp = v["expect"]
        print(f"{w1 + w2}")
    return output


def main():
    _ = process_all(PROBLEM_SETS)


if __name__ == "__main__":
    main()
