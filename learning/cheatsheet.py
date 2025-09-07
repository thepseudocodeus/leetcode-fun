Mathematical Problem-Definition Cheat Sheet
How to define a problem precisely before writing code.

Core Concepts
Invariant: A property of a system that remains unchanged under a set of operations. The solution must satisfy this invariant.

Example: In a sorted array, the invariant is a[i] ≤ a[i+1] for all valid i.

Primitive Operation: A fundamental operation assumed to take constant time O(1) (e.g., arithmetic, comparison, memory access, hash table insertion/lookup).

State: The current configuration of all data being processed.

Data Structures & Their Properties
Structure	Mathematical Concept	Key Properties (TSC)
Array / List	Finite Sequence (S = [s₀, s₁, ..., sₙ₋₁]).	Access by index: O(1). Search: O(n).
String	A sequence of Characters (from an Alphabet Σ).	Treated as a list.
Set	An unordered collection of distinct elements. {x₁, x₂, ..., xₙ}.	Membership test (x ∈ S): O(1) (hash-based).
Dictionary / Map	A finite Function f: Keys -> Values.	Insertion, lookup, update: O(1) (hash-based).
Stack	A Sequence with LIFO (Last-In, First-Out) order.	Push/Pop: O(1).
Queue	A Sequence with FIFO (First-In, First-Out) order.	Enqueue/Dequeue: O(1) (amortized, with a good impl.).
Graph	A pair G = (V, E) where V is a set of vertices and E is a set of edges (pairs of vertices).	Stored as an Adjacency List (space: O(|V| + |E|)).
Tree	A connected, acyclic graph. Often has a root.	Often implies a recursive structure.
Heap / Priority Queue	A structure that maintains elements such that the min (or max) element is always at the root.	Insertion, extraction: O(log n).
Logical Quantifiers & Operators
Universal Quantifier (∀ - "For all"): A condition must hold true for every element in a set.

Code: all(...), a loop that must not break early.

Example (Palindrome): ∀ i ∈ [0, n//2), s[i] == s[n-1-i]

Existential Quantifier (∃ - "There exists"): A condition must hold true for at least one element in a set.

Code: any(...), a loop that can break early (return when found).

Example (Two Sum): ∃ i, j such that i != j and nums[i] + nums[j] == target

Negation (¬ - "Not"): The opposite of a condition.

Implication (→ - "Implies"): If condition A is true, then condition B must be true.

Equivalence (↔ - "If and only if"): Condition A is true if and only if condition B is true. Used for precise definitions.

Key Relations & Properties
Reflexivity: a == a. (e.g., equality)

Symmetry: If a == b, then b == a. (e.g., equality, adjacency in an undirected graph)

Transitivity: If a == b and b == c, then a == c. (e.g., equality, "is an ancestor of" in a tree)

Totality: For any two elements a and b, either a ≤ b or b ≤ a is true. (Crucial for sorting)

Anti-symmetry: If a ≤ b and b ≤ a, then a == b. (Crucial for sorting)

Common Problem Types & Their Definitions
Problem Type	Surface Definition	Mathematical Definition (The "Good" One)
Palindrome	"Reads the same forwards and backwards."	∀ i ∈ {0, 1, ..., floor((n-1)/2)}, s[i] = s[n-1-i]
Two Sum	"Find two numbers that add to target."	∃ i, j (i ≠ j) such that nums[i] + nums[j] = target
Or better: ∀ x ∈ nums, let y = target - x. If y exists in nums (at a different index), return True.
Contains Duplicate	"Find if any value appears twice."	The multiset of numbers has at least one element with frequency > 1.
Or: ∃ i, j (i ≠ j) such that nums[i] = nums[j]
Or: |set(nums)| < len(nums)
Binary Search	"Find a target in a sorted array."	Find the index i such that nums[i] = target. <br> **Invariant:** If it exists, target must be in the interval [low, high].
BFS/Shortest Path	"Find the shortest path in a graph."	Find the minimal k such that there exists a path v₀ → v₁ → ... → vₖ from source to target.
Topological Sort	"Order vertices so all edges point forward."	Find a linear ordering of V such that for every directed edge (u → v), u comes before v in the ordering.
Useful Verbs for "Definition #2"
Find / Determine: ∃ (There exists...)

Verify / Check / Validate: ∀ (For all... this must hold)

Count: \|{x ∈ S \| condition(x)}\| (The cardinality of the set of elements that satisfy the condition)

Enumerate: Generate all elements of the set {x ∈ S \| condition(x)}.

Maximize/Minimize: Find the element x in set S that has the maximum/minimum value of f(x).

Transform: Apply a function f to every element of a sequence, producing a new sequence map(f, S).

How to Use This Sheet
Read the Problem.

Write "Definition #1": The surface-level description.

Open this sheet and write "Definition #2": Force yourself to define the problem using the terms above.

Start with: "This is true if and only if..."

Or: "The solution is found when..."

Use: ∀, ∃, set, sequence, graph, invariant.

Let Definition #2 dictate the algorithm and data structures you choose. The code will almost write itself.
