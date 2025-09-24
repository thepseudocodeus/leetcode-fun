1. Core Abstractions (The Singularities)
These are the fundamental models that every problem reduces to. They are the "singularities" from which all solutions emerge.

Search and Traversal: This is the most universal abstraction. The problem is a search for an optimal path or state within a defined space. Key invariants include state transitions and goal conditions. This category includes everything from simple pathfinding to complex game theory.

Optimization: The problem involves finding the "best" possible solution from a set of valid ones, often defined by minimizing or maximizing a specific value. The key invariant is a monotonic property, where moving closer to the solution state improves a specific metric.

Decision: The problem requires a simple yes/no answer. The core invariant is a proof of existence or non-existence of a specific state. This is often solved by reframing it as an optimization or search problem (e.g., "can a path with a length of X be found?").

Construction: The problem requires building a specific structure that satisfies certain rules. The key invariant is a set of rules that must be followed at all times. This can often be solved with a greedy approach or dynamic programming.

2. Algorithmic Models (The Navigational Tools)
Once you've identified the core abstraction, you select the appropriate "tool" or algorithmic model to navigate the problem space.

Graphs & Trees: The problem can be modeled as a network of nodes and edges.

Invariants: Connectivity, cycles, path length, and node relationships.

Algorithms: BFS, DFS, Dijkstra's, A* Search, Minimum Spanning Tree (MST).

Dynamic Programming (DP): The problem has optimal substructure and overlapping subproblems.

Invariants: The solution to a larger problem depends on the solutions to smaller, identical subproblems. A common invariant is a "state" that can be computed from a set of previous states.

Algorithms: Memoization, tabulation.

Mathematical & Number Theory: The problem's solution relies on properties of numbers.

Invariants: Prime factorization, modular arithmetic, divisibility rules.

Algorithms: Sieve of Eratosthenes, Euclidean Algorithm, modular exponentiation.

Greedy Algorithms: The problem can be solved by making a locally optimal choice at each step, which guarantees a globally optimal solution.

Invariants: A "greedy choice property," meaning the first choice made is always part of a larger optimal solution.

Data Structures: The problem is best solved by organizing data in a specific way to facilitate efficient operations.

Invariants: The data structure maintains a specific property, like a balanced binary search tree always remaining balanced.

Algorithms: Hash maps, heaps, Tries, Fenwick trees.

3. The Multidimensional Subspace (Constraints & Context)
The "constraints" in a problem define its specific "subspace" within the larger domain. A top problem-solver learns to quickly identify these constraints to refine their choice of a solution.

Time & Space Complexity: The most common constraints. A tight time limit might force you to abandon an O(n^2) solution for an O(n log n) or O(n) one.

Data Type: The nature of the input (e.g., integers, strings, floating-point numbers) can point to specific algorithms (e.g., number theory for integers, string matching algorithms).

Input Size: A small input size might allow a brute-force approach, while a large one necessitates an optimized solution.

Behavior: The required output might be a single number, a list of all solutions, or a specific data structure. This guides the final implementation.

The key to mastery is to rapidly move from the surface-level problem description to its core abstraction and then select the right algorithmic model, all while being guided by the constraints of its specific subspace.
