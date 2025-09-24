# simple_solver.py

import json
import subprocess

import typer
from rich.console import Console

console = Console()

app = typer.Typer(help="The minimalist problem-solving tool.")


def call_haskell_backend(command, data):
    """Communicates with the Haskell backend."""
    try:
        # In a real system, a more robust API call would be used.
        result = subprocess.run(
            ["haskell-solver", command, json.dumps(data)],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error from backend:[/bold red] {e.stderr}")
        return None


@app.command(name="solve")
def solve_problem(problem_name: str, topic: str):
    """
    Begins a minimalist problem-solving session.
    """
    console.print(f"[bold blue]Solving problem: {problem_name}[/bold blue]")

    # Step 1: Discover the Equation To Solve (Invariant)
    invariant = console.input(
        "[yellow]What is the invariant that drives the problem?[/yellow] "
    )

    # [] TODO: Step 2: Declare Transformations
    transformation = console.input("[yellow]Declare the core transformation:[/yellow] ")

    # [] TODO: Step 3: Create Code Pipelines
    code = console.input("[yellow]Provide the elegant solution code:[/yellow] ")

    # [] TODO: Build precise Haskell backend for complex analysis and scoring
    response = call_haskell_backend(
        "score_and_analyze",
        {"invariant": invariant, "transformation": transformation, "code": code},
    )

    if response:
        console.print("\n[bold green]Analysis Complete![/bold green]")
        console.print(f"**Elegance Score:** {response.get('elegance_score', 0):.2f}")
        console.print(
            f"**Invariant Precision:** {response.get('invariant_precision', 0):.2f}"
        )
        console.print(f"**Overall Score:** {response.get('total_score', 0):.2f}")
        console.print(
            f"**Feedback:** {response.get('feedback', 'No feedback provided.')}"
        )


if __name__ == "__main__":
    app()
