---
id: ts6y960ekrd1gxl8gucte2c
title: My_tools
desc: ''
updated: 1758509372752
created: 1758487402598
---

We solve problems mathematically. Thus, we work declaratively not imperatively.

## Declarative Operations

def cond(predicate, true_func, false_func, *args, **kwargs):
    """A functional conditional expression.
    Returns true_func(*args,**kwargs) if predicate is Truthy,
    otherwise returns false_func(*args, **kwargs).
    """
    return (true_func if predicate else false_func)(*args,**kwargs)

def do(**funcs):
    def run(iterable, initializer=None)
    return run

def my_reduce(func, iterable, initializer=None):
    iterator = iter(iterable)

    # Get the first item imperatively. This is our one necessary side effect.
    if initializer is None:
        try:
            first_item = next(iterator)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value") from None
        return _recursive_reducer(func, iterator, first_item)
    else:
        return _recursive_reducer(func, iterator, initializer)

def _recursive_reducer(func, iterator, accumulated_value):
    """Purely recursive part of the reduction."""
    try:
        next_item = next(iterator) # The only side effect
    except StopIteration:
        return accumulated_value    # Base case
    new_value = func(accumulated_value, next_item)
    return _recursive_reducer(func, iterator, new_value)

def my_pipe(*funcs):
    """Create a pipeline from a sequence of functions using our own my_reduce."""

    def composed(initial_value):
        # The function we reduce with is: "apply the next function to the current value"
        apply_func = lambda current_value, next_func: next_func(current_value)
        # Start with the initial_value, and apply each function in order.
        return my_reduce(apply_func, funcs, initial_value)

    return composed

def do(value, *funcs):
    """Apply a series of functions to a value."""
    return pipe(*funcs)(value) # Builds the pipeline and runs it immediately.

result = do("  ALICE  ", clean, capitalize, add_greeting)
print(result)

def compose(*funcs):
    """Compose functions from right to left.
    compose(f, g, h)(x) is equivalent to f(g(h(x)))."""
    return functools.reduce(lambda f, g: lambda x: f(g(x)), funcs)

format_name = compose(add_greeting, capitalize, clean)
result = format_name("  ALICE  ")

def pipe(*funcs):
    """Create a pipeline from a sequence of functions.
    Returns a new function: value -> f(g(h(value)))"""
    def composed(initial_value):
        # [] TODO: import reduce from functools to use
        return reduce(lambda value, func: func(value), funcs, initial_value)
    return composed

def cond(predicate, true_func, false_func, *args, **kwargs):
    """A functional conditional expression.
    Returns true_func(*args,**kwargs) if predicate is Truthy,
    otherwise returns false_func(*args, **kwargs).
    """
    return (true_func if predicate else false_func)(*args,**kwargs)
