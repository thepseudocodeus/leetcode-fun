# solver_facade.py
from typing import Callable

import core_solvers

from .contracts import ProblemContract
from .pipelines import build_input_pipe, build_output_pipe, compose


def create_solver(contract: ProblemContract, core_solver: Callable) -> Callable:
    """Methodology: build pipelines of pipelines"""
    input_pipe = build_input_pipe(contract)
    output_pipe = build_output_pipe(contract)

    # Compose: input -> core -> output
    return compose(output_pipe, core_solver, input_pipe)


two_sum_contract = ProblemContract(
    input_spec="list[int], int",
    output_spec="list[int]",
    key_invariant="complement_exists",
)

two_sum_solver = create_solver(two_sum_contract, core_solvers.solve_two_sum_core)


def main():
    result = two_sum_solver(([2, 7, 11, 15], 9))
    print(result)  # [0, 1]
