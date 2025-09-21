---
id: 7zlsntp0v9hfj8proafapp7
title: Cheatsheet_ideas
desc: ''
updated: 1758489076499
created: 1758489074356
---
The Declarative Programmer's Cheatsheet

1. The Core Philosophy
Your Goal: For any problem, find the rule or transformation that defines the solution. Your code should be a direct expression of that rule, built by composing the tools below.

2. The Essential Toolkit
collections Module: The Rule-Based Data Structures
Counter(iterable): Your go-to for frequency analysis. The rule is often "the answer is based on counts."

Rule: "The character that appears once..." -> [char for char, count in Counter(s).items() if count == 1][0]

Rule: "The most common element..." -> Counter(nums).most_common[1](0)[0]

defaultdict(type): For building groupings or graphs without worrying about key errors. The rule is "group items by a key."

Rule: "Group anagrams..." -> groups = defaultdict(list); for word in words: key = tuple(sorted(word)); groups[key].append(word)

deque(): For BFS or FIFO/LIFO problems. The rule is "process nodes in the order they were discovered."

itertools Module: The Rule-Based Iteration Tools
chain(*iterables): The rule is "treat these separate sequences as one continuous sequence."

groupby(iterable, key=None): The rule is "process consecutive groups of identical items." Sort first if groups aren't consecutive.

Rule: "Run-length encoding..." -> [(k, len(list(g))) for k, g in groupby('aaabbc')] -> [('a',3), ('b',2), ('c',1)]

combinations(p, r) / permutations(p, r): The rule is "try all possible pairs/arrangements."

accumulate(iterable, func=operator.add): The rule is "the solution is the cumulative result of an operation" (running sum, product, etc.).

takewhile(predicate, iterable) / dropwhile(...): The rule is "process items until a condition fails."

functools Module: The Rule-Based Function Tools
reduce(func, iterable, initializer=None): The most important tool. The rule is "the solution is the reduction of the list under some operation."

Rule: "Find the product..." -> reduce(operator.mul, [1, 2, 3, 4]) -> 24

Rule: "Find the maximum..." -> reduce(lambda a, b: a if a > b else b, [1, 5, 2, 8, 3]) -> 8

@lru_cache(maxsize=None): The rule is "the solution can be found by recursion with overlapping subproblems" (e.g., Fibonacci, DP). Memoization is a declarative concept.

operator Module: The Rule-Based Function Shortcuts
Use these to make map, reduce, and sort key functions cleaner.

operator.add, .mul, .sub, .truediv

operator.itemgetter(i) (cleaner than lambda x: x[i] for sorting)

operator.attrgetter('attr') (for sorting objects)

heapq Module: The Rule-Based Priority Queue
The rule is "I always need the smallest/largest element next." -> heapq.heappush(heap, item), heapq.heappop(heap)

bisect Module: The Rule-Based Binary Search
The rule is "the list is sorted, so I can find the answer in O(log n) time." -> bisect.bisect_left(arr, target)

3. The Mental Framework: From Problem to Declarative Solution
State the Rule: Verbalize the mathematical rule that solves the problem.

Problem (#136): "The number that appears only once is the one that doesn't get canceled out."

Rule: "The solution is the XOR sum of all numbers."

Find the Tool: Map the rule to a tool.

Rule requires a "sum" with cancellation -> reduce and operator.xor.

Compose the Expression: Write the code as a direct translation of the rule.

return reduce(xor, nums)

Another Example:

Problem (#242 Valid Anagram): "Two strings are anagrams if they have the same character frequency distribution."

Rule: "The solution is the equality of the frequency counters of each string."

Tool: Counter

Expression: return Counter(s) == Counter(t)

4. Advanced Pattern: Building Your Own Abstractions
When you see a pattern, abstract it. This is the pinnacle of declarative thinking.

See this pattern often?

python
result = []
for item in list:
    if condition(item):
        result.append(transform(item))
Abstract it! You've just rediscovered map and filter. But if your transformation is complex, build a helper.

python

# Instead of a loop, declare the pipeline

result = list(map(transform, filter(condition, list)))
This cheatsheet is your key. Don't write loops; declare rules. Your code will be shorter, more robust, and will truly represent your mathematical understanding of the solution.
