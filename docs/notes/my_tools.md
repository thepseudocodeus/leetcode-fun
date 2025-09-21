---
id: ts6y960ekrd1gxl8gucte2c
title: My_tools
desc: ''
updated: 1758489188421
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
