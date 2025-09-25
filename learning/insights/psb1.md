1️⃣ Problem Definition Phase

Goal: Precisely define what the problem is, not how to solve it yet.

Steps:

Restate the problem in formal mathematical language (sets, sequences, graphs, functions, etc.).

Identify domain and codomain of inputs/outputs.

Determine constraints and assumptions (non-decreasing, uniqueness, monotonicity, etc.).

Highlight edge cases implied by the axioms (empty lists, duplicates, negative numbers, max/min bounds).

2️⃣ Invariant & Structure Analysis

Goal: Extract the rules that must always hold true during the solution.

Steps:

Identify invariants (conditions that hold at every step of any valid transformation).

Understand the effect of operations on these invariants.

Think about auxiliary structures (arrays, hash maps, linked lists, stacks, heaps) that maintain these invariants efficiently.

3️⃣ Brute Force Exploration

Goal: Start simple to understand the problem space.

Steps:

Write the simplest possible solution (even O(n²) or O(n³) if needed).

Analyze its time and space complexity.

Observe where inefficiencies or redundancies appear.

Use this as a baseline for improvements.

4️⃣ Iterative Refinement & Optimization

Goal: Improve incrementally using precise reasoning.

Steps:

Hypothesize which data structures or algorithms could exploit identified invariants.

Implement and test small experiments to validate these ideas.

Refine problem definition if edge cases or new invariants emerge.

Repeat: Discover → Refine → Exploit.

5️⃣ Invariant-Centric Optimal Solution

Goal: Identify the key invariant that unlocks an O(1) or near-optimal solution.

Steps:

Leverage data structures that maintain invariants in constant or logarithmic time.

Apply the algorithmic pattern that uses the invariant fully (merge, two-pointer, sliding window, monotonic stack, DP, etc.).

Validate with all edge cases; ensure invariants are never violated.

Only now, finalize coding — the implementation is mostly mechanical.

Key Takeaways

Focus on the problem definition first: 80% of difficulty is understanding the space, constraints, and invariants.

Use brute force as an exploratory tool, not the goal.

Rapid iteration of discovery → refinement → exploitation allows you to identify patterns, invariants, and optimal structures without wasted effort.

Invariant-driven thinking = shortcut to optimal solutions.
