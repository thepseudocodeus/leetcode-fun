Playful Python

Home About Courses Sign In
Y Combinator in Python
August 22, 2022 5 min read 0
It's time to take a break from practical applications of functional programming to something less practical, but very interesting to know 😎

You may have heard of Y Combinator, one of the first and most well known startup accelerator. Have you ever wondered what the name means?

Y Combinator comes from a branch of mathematics called combinatorial logic. As usual, we will skip the maths and jump to look at what the Y Combinator does.

Recursive Functions
Recursive functions are functions that call themselves. The most common example given is a factorial function, so let us go with that.

def factorial(x):
if x == 0: return 1
return x * factorial(x - 1)
PythonCopy
So if we were to calculate factorial(3) that would evaluate to 3*factorial(2) which in turn would evaluate to 3*2*factorial(1), then 3*2*1*factorial(0) and finally 3*2*1*1 which is 6.

Imagine the ability for a function to call itself by its name did not exist in our language (Early versions of many languages did not support recursion for example).

It turns out that if the language supports higher order functions then you can use that property to create recursive functions – even without the ability for a function to call itself by name. Let us see how.

Building a recursive factorial
We want to build a recursive factorial implementation where the factorial function doesn't call itself directly.

We start with this base implementation. We will call it fact_nr since it is not recursive

def fact_nr(fn):
def inner(n):
if n == 0:
return 1
return n _ fn(n-1)
return inner
PythonCopy
,.
Take a look at the inner function first. It looks just like a factorial function, but in the recursion step, instead of calling itself like n _ inner(n - 1) instead it calls n \* fn(n - 1). What is fn? That is the function that we pass in as a parameter to fact_nr.

So this implementation allows us to configure a function fn which will be used during the recursion step. Lets see how it works

def error(n):
raise Exception()

fact_1 = fact_nr(error)
print(fact_1(0)) # 1
print(fact_1(1)) # Exception
PythonCopy
Here we pass in an error function to fact_nr to create fact_1. The error function will always just raise an exception when called. When we call fact_1(0) then it goes into the if n == 0 line and returns 1. When we call fact_1(1) then the execution goes into the recursion step where it executes fn. Since fn is configured to error, that will execute and raise the exception.

What we really want is that when going into the recursion step we want it to call itself again. Suppose we pass in fact_nr function as its own parameter, like this

fact_2 = fact_nr(fact_nr(error))
print(fact_2(0)) # 1
print(fact_2(1)) # 1
print(fact_2(2)) # Exception
PythonCopy
This time when it needs to recurse once then it executes the second fact_nr that was passed in and we get the right output. But if we need to recurse a second time we end up executing the error function.

We can extend this however long we want by doing something like this

# this will recurse until depth 6

fact_6 = fact_nr(fact_nr(fact_nr(fact_nr(fact_nr(fact_nr(error))))))
PythonCopy
But eventually we need to pass in some terminating function (error in this case). A true recursive function would be like

factorial = fact_nr(fact_nr(fact_nr(fact_nr(fact_nr(fact_nr(..... # forever
PythonCopy
Y Combinator
The Y Combinator can take a non-recursive function like fact_nr and convert it to a true recursive version.

Here is the Y Combinator definition in the form usually found in literature

def Y(fn_nr):
return (lambda x: fn_nr(lambda y: x(x)(y)))(lambda x: fn_nr(lambda y: x(x)(y)))
PythonCopy
or in a simpler form

def Y(fn_nr):
def \_inner(cc):
return fn_nr(lambda x: cc(cc)(x))
return \_inner(\_inner)
PythonCopy
It is pretty daunting to look at. If you are interested in how it works in detail, check out the reference section below.

The main thing here is that Y takes the non-recursive function fn_nr as input and returns another function as output which is fully recursive. Here it is in action

factorial = Y2(fact_nr)

print(factorial(10)) # 3828800
PythonCopy
Isn't that magical?

You can use the same trick with other recursive functions. You just make the function take a fn parameter and in the recursion step you call that function instead of itself. Any function of that form can be passed into Y to get a true recursive version.

For instance here is a non-recursive version to calculate the length of a list

def len_nr(fn):
def inner(lst):
if lst == []:
return 0
return 1 + fn(lst[1:])
return inner
PythonCopy
Pass it to Y and we now have a recursive implementation of length of a list

len_lst = Y(len_nr)

print(len_lst([1, 2, 3])) # 3
PythonCopy
But Is It Useful?
Well thats great and all but as python natively supports recursion, is there any point to all of this. Well, short answer is no 😆

Well there is one practical application. When you need to modify the recursive function at runtime then you might want to implement the code in the non-recursive form shown here. Then you can pass it in to higher order functions to do runtime transformations before finally sending it along to Y to get a recursive version.

This technique is described in more detail by Bruce McAdam in his paper "That About Wraps It Up" which you can read here.

Apart from that, there isn't a place that I'd use the Y Combinator in practical use. Ultimately it is a fun bit of magic that's nice to know and marvel at.

And that magic is what caused Paul Graham – a hardcore functional programmer himself – to name his startup accelerator Y Combinator. An apt metaphor for a company that takes a not-quiet-finished product as input and turns out a fully working version as output.

Did you like this article?
If you liked this article, consider subscribing to this site. Subscribing is free.

Why subscribe? Here are three reasons:

You will get every new article as an email in your inbox, so you never miss an article
You will be able to comment on all the posts
Once in a while, I will be posting conference talk slides, longer form articles (such as this one), and other content as subscriber-only
References

I first came across the Y Combinator in the book The Little Schemer. This is a fantastic book which is very accessible to even to beginner programmers. If you are interested in functional programming, then I would highly recommend checking it out. Chapter 9 of this book contains the section on the Y Combinator where it is derived from first principles with an explanation of every step.

And for those interested in the math of combinatoric logic, check out Raymond Smullyan's book To Mock a Mockingbird, where combinatoric logic is explained in the form of puzzles involving birds that sing various songs.
