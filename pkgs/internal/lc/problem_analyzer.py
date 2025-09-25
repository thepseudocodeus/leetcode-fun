from typing import Callable

from contracts import ProblemContract
from solver_facade import create_solver


def analyze_problem_to_contract(problem_md: str) -> ProblemContract:
    """Convert problem description to mathematical contract"""
    # Simple heuristic-based analysis
    if "two numbers such that they add up to target" in problem_md:
        return ProblemContract(
            input_spec="list[int], int",
            output_spec="list[int]",
            key_invariant="complement_exists",
        )
    elif "regular expression matching" in problem_md:
        return ProblemContract(
            input_spec="str, str", output_spec="boolean", key_invariant="state_machine"
        )
    # Add more patterns as you solve more problems


def create_solver_for_problem(problem_md: str, core_logic: Callable) -> Callable:
    """One-liner to create a solver for any problem"""
    contract = analyze_problem_to_contract(problem_md)
    return create_solver(contract, core_logic)
