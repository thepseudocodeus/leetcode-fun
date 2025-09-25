6️⃣ General Statement

Graphs = universal abstraction

Nodes = elements

Edges = relationships or pointers

Most data structures can be seen as graphs with constraints:

Linked list → path

Array → path with implicit edges via indices

Tree → acyclic directed graph

HashMap → graph of keys → nodes in buckets

Constants vs Invariants vs Variables — LeetCode Cheat Sheet
Concept Definition Role in Problem-Solving Example (LeetCode) Reasoning Tip
Constant Fixed data/value that never changes Boundary conditions, fixed parameters MAX_CAPACITY = 50 in a stack problem; n = len(array) in array traversal Identify upfront: values you can rely on
Invariant Property/condition that must remain true under transformations Guides correctness, allows deductive reasoning - Linked List traversal: “Current node is never null before accessing .next”

- Sorting: “Subarray [0..i] is sorted after each insertion”
- DFS stack: “Nodes in stack have not yet been fully processed” Use to design algorithm steps safely; each operation must maintain invariants
  Variable Data that can change during execution Represents evolving state of the problem - current pointer in a linked list
- i in a for-loop
- stack content during DFS Track changes carefully; invariants constrain variable behavior
  Guiding Principles for Using Invariants

Identify invariants before coding:

Look at problem definition → what must always remain true?

Use invariants to structure algorithm:

Each step should preserve all invariants.

Derive new invariants from existing ones:

Apply logical deductions (like lemmas in math) → uncover optimization opportunities.

Check invariants at edges:

Edge cases often violate implicit invariants if overlooked.

Examples Across Problem Types
1️⃣ Linked Lists

Invariant: “All nodes before current are already processed; no node is visited twice.”

Variable: current pointer

Constant: Total number of nodes n

2️⃣ Arrays / Sequences

Invariant: “Subarray [0..i] is sorted” (Insertion sort)

Variable: Index i

Constant: Array length n

3️⃣ Stacks / Queues

Invariant: “Stack only contains nodes not yet fully explored” (DFS)

Variable: Stack content

Constant: Max stack capacity, or n total nodes

4️⃣ HashMap / LRU Cache

Invariant: “HashMap keys point to DLL nodes that are in proper order of usage”

Variable: DLL node positions, cache content

Constant: Cache capacity

5️⃣ Trees / Graphs

Invariant: “No node is visited twice” (DFS/BFS)

Variable: Visited set, recursion stack / queue content

Constant: Total number of nodes

Key Takeaways

Constants = axioms (fixed truths, boundaries)

Invariants = theorems (must remain true under operations)

Variables = evolving state (what changes as you apply transformations)

By formalizing invariants mathematically, you can discover optimal algorithms systematically, because each invariant restricts possible moves, reduces the solution space, and helps you deduce correctness before coding.
