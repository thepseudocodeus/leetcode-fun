— FREE Email Series —

🐍 Python Tricks 💌

Python Tricks Dictionary Merge

Email…
🔒 No spam. Unsubscribe any time.

Browse Topics Guided Learning Paths
Basics Intermediate Advanced
ai api best-practices career community databases data-science data-structures data-viz devops django docker editors flask front-end gamedev gui machine-learning news numpy projects python testing tools web-dev web-scraping

Table of Contents

Creating Python Inner Functions
Using Inner Functions: The Basics
Retaining State With Inner Functions: Closures
Adding Behavior With Inner Functions: Decorators
Conclusion
Recommended Video Course
Python Inner Functions

Python Inner Functions
Python Inner Functions: What Are They Good For?
by Leodanis Pozo Ramos Publication date Feb 08, 2021 Reading time estimate 17m 33 Comments
intermediate python
Table of Contents

Creating Python Inner Functions
Using Inner Functions: The Basics
Providing Encapsulation
Building Helper Inner Functions
Using Inner vs Private Helper Functions
Retaining State With Inner Functions: Closures
Retaining State in a Closure
Modifying the Closure State
Adding Behavior With Inner Functions: Decorators
Conclusion

Remove ads
Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: Python Inner Functions

Inner functions, also known as nested functions, are functions that you define inside other functions. In Python, this kind of function has direct access to variables and names defined in the enclosing function. Inner functions have many uses, most notably as closure factories and decorator functions.

In this tutorial, you’ll learn how to:

Provide encapsulation and hide your functions from external access
Write helper functions to facilitate code reuse
Create closure factory functions that retain state between calls
Code decorator functions to add behavior to existing functions
Free Bonus: Click here to get a Python Cheat Sheet and learn the basics of Python 3, like working with data types, dictionaries, lists, and Python functions.

Creating Python Inner Functions
A function defined inside another function is known as an inner function or a nested function. In Python, this kind of function can access names in the enclosing function. Here’s an example of how to create an inner function in Python:

> > > def outer_func():
> > > ... def inner_func():
> > > ... print("Hello, World!")
> > > ... inner_func()
> > > ...

> > > outer_func()
> > > Hello, World!
> > > In this code, you define inner_func() inside outer_func() to print the Hello, World! message to the screen. To do that, you call inner_func() on the last line of outer_func(). This is the quickest way to write an inner function in Python. However, inner functions provide a lot of interesting possibilities beyond what you see in this example.

The core feature of inner functions is their ability to access variables and objects from their enclosing function even after this function has returned. The enclosing function provides a namespace that is accessible to the inner function:

> > > def outer_func(who):
> > > ... def inner_func():
> > > ... print(f"Hello, {who}")
> > > ... inner_func()
> > > ...

> > > outer_func("World!")
> > > Hello, World!
> > > Now you can pass a string as an argument to outer_func(), and inner_func() will access that argument through the name who. This name, however, is defined in the local scope of outer_func(). The names that you define in the local scope of an outer function are known as nonlocal names. They are nonlocal from the inner_func() point of view.

Here’s an example of how to create and use a more elaborate inner function:

> > > def factorial(number):
> > > ... # Validate input
> > > ... if not isinstance(number, int):
> > > ... raise TypeError("Sorry. 'number' must be an integer.")
> > > ... if number < 0:
> > > ... raise ValueError("Sorry. 'number' must be zero or positive.")
> > > ... # Calculate the factorial of number
> > > ... def inner_factorial(number):
> > > ... if number <= 1:
> > > ... return 1
> > > ... return number \* inner_factorial(number - 1)
> > > ... return inner_factorial(number)
> > > ...

> > > factorial(4)
> > > 24
> > > In factorial(), you first validate the input data to make sure that your user is providing an integer that is equal to or greater than zero. Then you define a recursive inner function called inner_factorial() that performs the factorial calculation and returns the result. The final step is to call inner_factorial().

Note: For a more detailed discussion on recursion and recursive functions, check out Thinking Recursively in Python and Recursion in Python: An Introduction.

The main advantage of using this pattern is that, by performing all the argument checking in the outer function, you can safely skip error checking in the inner function and focus on the computation at hand.

Remove ads
Using Inner Functions: The Basics
The use cases of Python inner functions are varied. You can use them to provide encapsulation and hide your functions from external access, you can write helper inner functions, and you can also create closures and decorators. In this section, you’ll learn about the former two use cases of inner functions, and in later sections, you’ll learn how to create closure factory functions and decorators.

Providing Encapsulation
A common use case of inner functions arises when you need to protect, or hide, a given function from everything happening outside of it so that the function is totally hidden from the global scope. This kind of behavior is commonly known as encapsulation.

Here’s an example that highlights that concept:

> > > def increment(number):
> > > ... def inner_increment():
> > > ... return number + 1
> > > ... return inner_increment()
> > > ...

> > > increment(10)
> > > 11

> > > # Call inner_increment()
> > >
> > > inner_increment()
> > > Traceback (most recent call last):
> > > File "<input>", line 1, in <module>

    inner_increment()

NameError: name 'inner_increment' is not defined
In this example, you can’t access inner_increment() directly. If you try to do it, then you get a NameError. That’s because increment() totally hides inner_increment(), preventing you from accessing it from the global scope.

Building Helper Inner Functions
Sometimes you have a function that performs the same chunk of code in several places within its body. For example, say you want to write a function to process a CSV file containing information about the Wi-Fi hotspots in New York City. To find the total number of hotspots in New York as well as the company that provides most of them, you create the following script:

# hotspots.py

import csv
from collections import Counter

def process_hotspots(file):
def most_common_provider(file_obj):
hotspots = []
with file_obj as csv_file:
content = csv.DictReader(csv_file)

            for row in content:
                hotspots.append(row["Provider"])

        counter = Counter(hotspots)
        print(
            f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
            f"{counter.most_common(1)[0][0]} has the most with "
            f"{counter.most_common(1)[0][1]}."
        )

    if isinstance(file, str):
        # Got a string-based filepath
        file_obj = open(file, "r")
        most_common_provider(file_obj)
    else:
        # Got a file object
        most_common_provider(file)

Here, process_hotspots() takes file as an argument. The function checks if file is a string-based path to a physical file or a file object. Then it calls the helper inner function most_common_provider(), which takes a file object and performs the following operations:

Read the file content into a generator that yields dictionaries using csv.DictReader.
Create a list of Wi-Fi providers.
Count the number of Wi-Fi hotspots per provider using a collections.Counter object.
Print a message with the retrieved information.
If you run the function, then you get the following output:

> > > from hotspots import process_hotspots

> > > file_obj = open("./NYC_Wi-Fi_Hotspot_Locations.csv", "r")
> > > process_hotspots(file_obj)
> > > There are 3319 Wi-Fi hotspots in NYC.
> > > LinkNYC - Citybridge has the most with 1868.

> > > process_hotspots("./NYC_Wi-Fi_Hotspot_Locations.csv")
> > > There are 3319 Wi-Fi hotspots in NYC.
> > > LinkNYC - Citybridge has the most with 1868.
> > > Whether you call process_hotspots() with a string-based file path or with a file object, you get the same result.

Using Inner vs Private Helper Functions
Typically, you create helper inner functions like most_common_provider() when you want to provide encapsulation. You can also create inner functions if you think you’re not going to call them anywhere else apart from the containing function.

Although writing your helper functions as inner functions achieves the desired result, you’ll probably be better served by extracting them as top-level functions. In this case, you could use a leading underscore (\_) in the name of the function to indicate that it’s private to the current module or class. This will allow you to access your helper functions from anywhere else in the current module or class and reuse them as needed.

Extracting inner functions into top-level private functions can make your code cleaner and more readable. This practice can produce functions that consequently apply the single-responsibility principle.

Retaining State With Inner Functions: Closures
In Python, functions are first-class citizens. This means that they’re on par with any other object, such as numbers, strings, lists, tuples, modules, and so on. You can dynamically create or destroy them, store them in data structures, pass them as arguments to other functions, use them as return values, and so forth.

You can also create higher-order functions in Python. Higher-order functions are functions that operate on other functions by taking them as arguments, returning them, or both.

All examples of inner functions that you’ve seen so far have been ordinary functions that just happen to be nested inside other functions. Unless you need to hide your functions from the outside world, there’s no specific reason for them to be nested. You could define those functions as private top-level functions, and you’d be good to go.

In this section, you’ll learn about closure factory functions. Closures are dynamically created functions that are returned by other functions. Their main feature is that they have full access to the variables and names defined in the local namespace where the closure was created, even though the enclosing function has returned and finished executing.

In Python, when you return an inner function object, the interpreter packs the function along with its containing environment or closure. The function object keeps a snapshot of all the variables and names defined in its containing scope. To define a closure, you need to take three steps:

Create an inner function.
Reference variables from the enclosing function.
Return the inner function.
With this basic knowledge, you can start creating your closures right away and take advantage of their main feature: retaining state between function calls.

Remove ads
Retaining State in a Closure
A closure causes the inner function to retain the state of its environment when called. The closure isn’t the inner function itself but the inner function along with its enclosing environment. The closure captures the local variables and name in the containing function and keeps them around.

Consider the following example:

# powers.py

def generate_power(exponent):
def power(base):
return base \*\* exponent
return power
Here’s what’s happening in this function:

Line 3 creates generate_power(), which is a closure factory function. This means that it creates a new closure each time it’s called and then returns it to the caller.
Line 4 defines power(), which is an inner function that takes a single argument, base, and returns the result of the expression base \*\* exponent.
Line 6 returns power as a function object, without calling it.
Where does power() get the value of exponent from? This is where the closure comes into play. In this example, power() gets the value of exponent from the outer function, generate_power(). Here’s what Python does when you call generate_power():

Define a new instance of power(), which takes a single argument base.
Take a snapshot of the surrounding state of power(), which includes exponent with its current value.
Return power() along with its whole surrounding state.
This way, when you call the instance of power() returned by generate_power(), you’ll see that the function remembers the value of exponent:

> > > from powers import generate_power

> > > raise_two = generate_power(2)
> > > raise_three = generate_power(3)

> > > raise_two(4)
> > > 16
> > > raise_two(5)
> > > 25

> > > raise_three(4)
> > > 64
> > > raise_three(5)
> > > 125
> > > In these examples, raise_two() remembers that exponent=2, and raise_three() remembers that exponent=3. Note that both closures remember their respective exponent between calls.

Now consider another example:

> > > def has_permission(page):
> > > ... def permission(username):
> > > ... if username.lower() == "admin":
> > > ... return f"'{username}' has access to {page}."
> > > ... else:
> > > ... return f"'{username}' doesn't have access to {page}."
> > > ... return permission
> > > ...

> > > check_admin_page_permision = has_permission("Admin Page")

> > > check_admin_page_permision("admin")
> > > "'admin' has access to Admin Page."

> > > check_admin_page_permision("john")
> > > "'john' doesn't have access to Admin Page."
> > > The inner function checks if a given user has the correct permissions to access a given page. You could quickly modify this to grab the user in session to check if they have the correct credentials to access a certain route.

Instead of checking if the user is equal to "admin", you could query an SQL database to check the permission and then return the correct view depending on whether the credentials are correct.

You’ll commonly create closures that don’t modify their enclosing state, or closures with a static enclosing state, as you saw in the above examples. However, you can also create closures that modify their enclosing state by using mutable objects, such as dictionaries, sets, or lists.

Suppose you need to calculate the mean of a dataset. The data come in a stream of successive measurements of the parameter under analysis, and you need your function to retain the previous measurements between calls. In this case, you can code a closure factory function like this:

> > > def mean():
> > > ... sample = []
> > > ... def inner_mean(number):
> > > ... sample.append(number)
> > > ... return sum(sample) / len(sample)
> > > ... return inner_mean
> > > ...

> > > sample_mean = mean()
> > > sample_mean(100)
> > > 100.0
> > > sample_mean(105)
> > > 102.5
> > > sample_mean(101)
> > > 102.0
> > > sample_mean(98)
> > > 101.0
> > > The closure assigned to sample_mean retains the state of sample between successive calls. Even though you define sample in mean(), it’s still available in the closure, so you can modify it. In this case, sample works as kind of dynamic enclosing state.

Modifying the Closure State
Normally, closure variables are completely hidden from the outside world. However, you can provide getter and setter inner functions for them:

> > > def make_point(x, y):
> > > ... def point():
> > > ... print(f"Point({x}, {y})")
> > > ... def get_x():
> > > ... return x
> > > ... def get_y():
> > > ... return y
> > > ... def set_x(value):
> > > ... nonlocal x
> > > ... x = value
> > > ... def set_y(value):
> > > ... nonlocal y
> > > ... y = value
> > > ... # Attach getters and setters
> > > ... point.get_x = get_x
> > > ... point.set_x = set_x
> > > ... point.get_y = get_y
> > > ... point.set_y = set_y
> > > ... return point
> > > ...

> > > point = make_point(1, 2)
> > > point.get_x()
> > > 1
> > > point.get_y()
> > > 2
> > > point()
> > > Point(1, 2)

> > > point.set_x(42)
> > > point.set_y(7)
> > > point()
> > > Point(42, 7)
> > > Here, make_point() returns a closure that represents a point object. This object has getter and setter functions attached. You can use those functions to get read and write access to the variables x and y, which are defined in the enclosing scope and ship with the closure.

Even though this function creates closures that might work faster than an equivalent class, you need to be aware that this technique doesn’t provide major features, including inheritance, properties, descriptors, and class and static methods. If you want to dive deeper into this technique, then check out Simple Tool for Simulating Classes Using Closures and Nested Scopes (Python Recipe).

Remove ads
Adding Behavior With Inner Functions: Decorators
Python decorators are another popular and convenient use case for inner functions, especially for closures. Decorators are higher-order functions that take a callable (function, method, class) as an argument and return another callable.

You can use decorator functions to add responsibilities to an existing callable dynamically and extend its behavior transparently without affecting or modifying the original callable.

Note: For more details about Python callable objects, check out The standard type hierarchy in the Python documentation and scroll down to “Callable types.”

To create a decorator, you just need to define a callable (a function, method, or class) that accepts a function object as an argument, processes it, and return another function object with added behavior.

Once you have your decorator function in place, you can apply it to any callable. To do so, you need to use the at symbol (@) in front of the decorator name and then place it on its own line immediately before the decorated callable:

@decorator
def decorated_func(): # Function body...
pass
This syntax makes decorator() automatically take decorated_func() as an argument and processes it in its body. This operation is a shorthand for the following assignment:

decorated_func = decorator(decorated_func)
Here’s an example of how to build a decorator function to add new functionality to an existing function:

> > > def add_messages(func):
> > > ... def \_add_messages():
> > > ... print("This is my first decorator")
> > > ... func()
> > > ... print("Bye!")
> > > ... return \_add_messages
> > > ...

> > > @add_messages
> > > ... def greet():
> > > ... print("Hello, World!")
> > > ...

> > > greet()
> > > This is my first decorator
> > > Hello, World!
> > > Bye!
> > > In this case, you use @add_messages to decorate greet(). This adds new functionality to the decorated function. Now when you call greet(), instead of just printing Hello, World!, your function prints two new messages.

The use cases for Python decorators are varied. Here are some of them:

Debugging
Caching
Logging
Timing
A common practice for debugging Python code is to insert calls to print() to check the values of variables, to confirm that a code block gets executed, and so on. Adding and removing calls to print() can be annoying, and you run the risk of forgetting some of them. To prevent this situation, you can write a decorator like this:

> > > def debug(func):
> > > ... def \_debug(*args, \*\*kwargs):
> > > ... result = func(*args, \*\*kwargs)
> > > ... print(
> > > ... f"{func.**name**}(args: {args}, kwargs: {kwargs}) -> {result}"
> > > ... )
> > > ... return result
> > > ... return \_debug
> > > ...

> > > @debug
> > > ... def add(a, b):
> > > ... return a + b
> > > ...

> > > add(5, 6)
> > > add(args: (5, 6), kwargs: {}) -> 11
> > > 11
> > > This example provides debug(), which is a decorator that takes a function as an argument and prints its signature with the current value of each argument and its corresponding return value. You can use this decorator to debug your functions. Once you get the desired result, you can remove the decorator call @debug, and your function will ready for the next step.

Note: If you’re interested in diving deeper into how \*args and \*\*kwargs work in Python, then check out Python args and kwargs: Demystified.

Here’s a final example of how to create a decorator. This time, you’ll reimplement generate_power() as a decorator function:

> > > def generate_power(exponent):
> > > ... def power(func):
> > > ... def inner_power(*args):
> > > ... base = func(*args)
> > > ... return base \*\* exponent
> > > ... return inner_power
> > > ... return power
> > > ...

> > > @generate_power(2)
> > > ... def raise_two(n):
> > > ... return n
> > > ...
> > > raise_two(7)
> > > 49

> > > @generate_power(3)
> > > ... def raise_three(n):
> > > ... return n
> > > ...
> > > raise_three(5)
> > > 125
> > > This version of generate_power() produces the same results you got in the original implementation. In this case, you use both a closure to remember exponent and a decorator that returns a modified version of the input function, func().

Here, the decorator needs to take an argument (exponent), so you need to have two nested levels of inner functions. The first level is represented by power(), which takes the decorated function as an argument. The second level is represented by inner_power(), which packs the argument exponent in args, makes the final calculation of the power, and returns the result.

Remove ads
Conclusion
If you define a function inside another function, then you’re creating an inner function, also known as a nested function. In Python, inner functions have direct access to the variables and names that you define in the enclosing function. This provides a mechanism for you to create helper functions, closures, and decorators.

In this tutorial, you learned how to:

Provide encapsulation by nesting functions in other functions
Write helper functions to reuse pieces of code
Implement closure factory functions that retaining state between calls
Build decorator functions to provide new functionalities
You’re now ready to take advantage of the many uses of inner functions in your own code. If you have any questions or comments, then be sure to share the in the comment section below.

Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: Python Inner Functions
