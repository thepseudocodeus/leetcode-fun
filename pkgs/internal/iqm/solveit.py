import os
import datetime
import json


def get_user_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def solve_problem_session():
    """
    Guides the user through the problem-solving process and stores the output.
    """
    problem_name = input("Enter the problem name: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    session_data = {"problem_name": problem_name, "timestamp": timestamp, "steps": []}

    steps_prompts = [
        "1. Deconstruct the problem. (Type 'END' on a new line when done):",
        "2. Define key terms and variants:",
        "3. Add additional knowns from the definitions:",
        "4. Decompose into abstract objects:",
        "5. Identify Invariants and Constraints:",
        "6. Analyze the Solution Space (e.g., Brute Force, DP, etc.):",
        "7. Create Problem & Solution State data structures:",
        "8. Declare the facade function signature:",
        "9. Deconstruct into Turing Machine components (input -> process -> output):",
        "10. Analyze Time & Space Complexity for each approach:",
        "11. Refine and select the optimal approach:",
        "12. Codify the optimal algorithm (paste the code, or write 'CODE'):",
        "13. Write a formal proof of correctness:",
        "14. Document Edge Cases and Failures:",
        "15. Generalize the solution (classify it):",
        "16. What is the final, runnable code? (paste the code, or write 'CODE'):",
    ]

    for i, prompt in enumerate(steps_prompts, 1):
        response = get_user_input(f"Step {i}: {prompt}")
        session_data["steps"].append(
            {"step_number": i, "prompt": prompt, "response": response}
        )

    output_filename = (
        f"{problem_name.replace(' ', '_').lower()}_{timestamp}_session.json"
    )
    with open(output_filename, "w") as f:
        json.dump(session_data, f, indent=4)
        print(f"\nSession saved to {output_filename}")


if __name__ == "__main__":
    solve_problem_session()
