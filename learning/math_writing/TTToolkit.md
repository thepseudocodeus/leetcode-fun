Tao's Toolkit: The Art of Precise Problem Definition
This is a personal toolkit designed to help master the process of mathematically defining problems. The system is built on a few core principles:

Terrence Tao's Invariant-Based Thinking: The practice focuses on identifying the things that don't change in a problem (the "invariants"), which provides a powerful foundation for building a solution.

Spaced Repetition: Concepts and problems are presented in short, focused bursts to build a new habit and reinforce learning over time.

Low-Friction Design: The user interface is intentionally simple and clear, built with tools like typer, rich, and inquirerpy to minimize cognitive load and make each session feel like a quick win.

Extensible and Declarative: New concepts and problems can be added simply by creating new Markdown files in the content directory. The application's core logic is separated from its presentation layer via a simple facade, ensuring the system is easy to maintain and extend without refactoring.

Project Structure
main.py: The application's entry point. It's a simple script that calls the core facade, serving as a test and demonstration of how the toolkit can be used.

tao_toolkit_facade.py: The single-source-of-truth blackbox. This higher-order function encapsulates all core application logic. Any future projects or modules would simply import and call this facade.

content_parser.py: Handles the declarative aspect of the system. This script reads and parses the Markdown files from the content/ directory, converting them into a usable data structure.

datastore.py: Manages all persistent data using TinyDB, including user progress and practice sessions.

content/: A directory containing all the learning content in Markdown format. This is where you'll add new lessons and problems.
