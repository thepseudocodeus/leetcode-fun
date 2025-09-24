Skip to content
geeksforgeeks
Search...
TutorialsCoursesTracks

A


Free Python 3 Tutorial
Data Types
Control Flow
Functions
List
String
Set
Tuple
Dictionary
Oops
Exception Handling
Python Programs
Python Projects
Python Interview Questions
Python MCQ
NumPy
Pandas
Python Database
Data Science With Python
Machine Learning with Python
Django
Flask
R




reduce() in Python
Last Updated : 20 Sep, 2025
reduce() function (from functools) applies a function cumulatively to an iterable, reducing it to a single value. It’s handy for concise tasks like summing, multiplying (factorial), finding max/min, concatenating strings or flattening lists. Use it for simple one-line reductions, avoid it for complex logic (loops are clearer) or when intermediate results are needed.




from functools import reduce
li = ["Geeks", "for", "Geeks"]
res = reduce(lambda x, y: x + " " + y, li)
print(res)

Output
Geeks for Geeks
Explanation:

reduce(lambda x, y: x + " " + y, words) takes two strings at a time and concatenates them with a space.
"Geeks" + "for" -> "Geeks for", then "Geeks for" + "Geeks" -> "Geeks for Geeks".
Syntax
It’s a method of functools module, so we need to import it before use:

from functools import reduce
reduce(function, iterable[, initializer])

Parameters:

function: A function that takes two arguments and returns a single value.
iterable: The sequence to be reduced (list, tuple, etc.).
initializer (optional): A starting value that is placed before first element.
Return Value: A single final value after processing all elements.

Examples
Example 1: Basic Usage with a Named Function
This code uses reduce() function to accumulate values in a list by repeatedly adding two numbers at a time.




from functools import reduce
def add(x, y):
    return x + y
​
a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)

Output
15
Explanation:

def add(x, y): return x + y - Defines a function that returns sum of two numbers.
reduce(add, a) - Applies add cumulatively to the list (((1+2)+3)+4)+5 --> 15.
Example 2: Using reduce() with a Lambda Function
This example demonstrates how a lambda function can be used with reduce() to calculate factorial of a number by multiplying all elements of a list.




from functools import reduce
a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x * y, a)
print(res)

Output
120
Explanation: reduce(lambda x, y: x * y, a) multiplies elements step by step --> (((1*2)*3)*4)*5 = 120.

Example 3: Using reduce() with operator Module
This example uses functools.reduce() with built-in functions from operator module to perform sum, product and string concatenation on lists.




import functools
import operator
a = [1, 3, 5, 6, 2]
​
print(functools.reduce(operator.add, a))
print(functools.reduce(operator.mul, a))
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

Output
17
180
geeksforgeeks
Explanation:

functools.reduce(operator.add, a): Adds all numbers in the list - 1+3+5+6+2 = 17.
functools.reduce(operator.mul, a): Multiplies all numbers in the list - 1*3*5*6*2 = 180.
functools.reduce(operator.add, ["geeks", "for", "geeks"]): Concatenates all strings in list - "geeksforgeeks"
Example 4: Using initializer
This code uses reduce() with a lambda function and an initial value to sum a list, starting from a given number.




from functools import reduce
a = [1, 2, 3]
res = reduce(lambda x, y: x + y, a, 10)
print(res)

Output
16
Explanation: reduce(lambda x, y: x + y, a, 10) starts with 10 as initial value, then adds each element in the list ((10+1)+2)+3 = 16.

Difference Between reduce() and accumulate()
The accumulate() function (from itertools) and reduce() both apply a function cumulatively to items in a sequence. However, accumulate() returns an iterator of intermediate results, while reduce() returns only final value.

Let's understand it better with an example.

Example
This code demonstrates how accumulate() from itertools module works it performs cumulative operations and returns all intermediate results instead of just a single final value.




from itertools import accumulate
from operator import add
​
a = [1, 2, 3, 4, 5]
res = accumulate(a, add)
print(list(res))

Output
[1, 3, 6, 10, 15]
Explanation: accumulate(a, add) - Adds elements cumulatively:

Step 1: 1
Step 2: 1 + 2 = 3
Step 3: 3 + 3 = 6
Step 4: 6 + 4 = 10
Step 5: 10 + 5 = 15
Let's understand difference between accumulate() and reduce() more clearly with the help of below table:

Feature	reduce()	accumulate()
Return Value	A single final value (e.g., 15).	Intermediate results (e.g., [1, 3, 6, 10, 15]).
Output Type	Returns a single value.	Returns an iterator.
Use Case	Useful when only the final result is needed.	Useful when tracking cumulative steps.
Import	From functools.	From itertools.
Suggested Quiz
6 Questions
What is the primary purpose of the reduce() function in Python?

A
To reduce the size of a list

B
To apply a function to items in a list and return a single cumulative result

C
To remove duplicates from a list

D
To filter elements from a list based on a condition

Which module must be imported to use reduce() in Python 3?

A
math

B
operator

C
functools

D
itertools

What is the output of the following code?



from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, nums)

print(result)

A
10

B
24

C
1234

D
Error

How does the reduce function differ from the map function in Python?

A
Reduce returns a single cumulative value, while map returns an iterable of results

B
Reduce can only work with numeric types, while map can work with any type

C
Reduce applies the function to each element independently, while map combines them

D
Reduce requires an initializer, while map does not

What will this code return?



from functools import reduce



nums = [2, 3, 4]

result = reduce(lambda x, y: x * y, nums)

print(result)

A
24

B
9

C
Error

D
6

Which of the following is not true about reduce()?

A
It can only be used with numeric data types

B
It stops execution if the iterable is empty and no initializer is provided

C
It returns a single value after processing all elements

D
It accepts an optional initializer argument


Quiz Completed Successfully
Your Score :
2
/6
Accuracy :
0%
View Explanation
1/6
< Previous Next >


Comment

More info
Explore
Python Fundamentals
Python Data Structures
Advanced Python
Data Science with Python
Web Development with Python
Python Practice

