title: Walking through 6 Ways to Use ChatGPT to Learn Code
date: 2/04/2023
image: deepmind-egDR0kw-Ptw-unsplash.jpg
status: published


So I was poking around on the web and decided to watch the video "THE Game Changer for Learning to Code"  https://www.youtube.com/embed/H1fBdboJeBo and then attempt to use it on code I use in class.  

TLDR:  Describing vocabulary, describing code, making suggestions for improving code, and finding resources all very useful.  Generating code is super dangerous (ChatGPT makes incorrect code) and using it in many cases can be considered plagiarism, just as if you copied from another person.

### Describing vocabulary -- useful

I started with,

> **ME**:  you're a professor trying to teach a student about euler's method. how would you phrase it?

> **ChatGPT**:
Euler's method is a numerical method used to approximate the solution to a first-order ordinary differential equation (ODE). It is a simple and straightforward way of approximating the solution by using the tangent line to the solution curve at a given point. The basic idea behind Euler's method is to divide the interval of interest into smaller sub-intervals and then estimate the value of the solution at the end of each sub-interval by using the tangent line. This process is then repeated, starting at the end of each sub-interval, until the desired level of accuracy is reached. Euler's method is a powerful tool for solving ODEs and is widely used in many scientific and engineering applications.

Not bad.  Seems useful to describe vocabulary.

### Describing code -- useful

Then I gave it some code I used in class,

> **ME:** Can you explain what this code is doing: 
```python
x_start=-5
x_end=15
step=1

S=Storage()

x=x_start
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    m=(y_right-y_left)/(step) # rise over run
    
    S+=x,m   # saving the result for later
    
    x=x+step
    
print("done.")

x,m=S.arrays()  # give me the saved results as two arrays
```

> **ChatGPT**: This code is implementing a numerical method called the midpoint method to estimate the derivative of a function `fun` over a range `x_start` to `x_end` with a step size `step`.
>
The `Storage` class is used to store the results of the midpoint method at each iteration. The `x` variable is initialized to `x_start` and the loop continues until `x` is greater than `x_end`.
>
In each iteration, the values of the function `fun` at `x-step/2` and `x+step/2` are calculated and stored in `y_left` and `y_right` respectively. The derivative at the midpoint `x` is then estimated as the rise over run `m = (y_right - y_left) / step`. The result is stored in the `Storage` object `S` using the `+=` operator.
>
Finally, after the loop, the results stored in `S` are retrieved as two arrays `x` and `m` using the `arrays()` method.
>
The midpoint method is a simple numerical method to estimate the derivative of a function. It is based on the idea that the derivative of a function at a point can be estimated as the average rate of change over a small interval around that point.

That is really impressive, and I think quite useful for students.


### Improving code -- somewhat useful

> **ME:** how would you improve that code?

> **ChatGPT:**  Here are a few suggestions to improve the code:
>
>1.  Use functions: You can define the midpoint method as a function and reuse it for different functions and different intervals. This makes the code more modular and easier to maintain.
  >  
> 2.  Document the code: Adding comments and documentation to the code can help someone who is unfamiliar with the code understand what it does. For example, you can add a comment explaining the purpose of the code and what each variable represents.
>    
>3.  Input validation: You can add input validation to check if the step size `step` is positive and non-zero. You can also add input validation to check if the interval `x_start` to `x_end` is well-defined.
  >  
>4.  Use `numpy` arrays: The `numpy` library provides arrays that are optimized for numerical computations. Instead of using the `Storage` class, you can use `numpy` arrays to store the results of the midpoint method.
  >  
>5.  Plotting: You can use a plotting library such as `matplotlib` to visualize the results of the midpoint method. This can be helpful in understanding the results and detecting any issues with the code.
  >  
>
By making these changes, you can make the code more readable, reusable, and understandable.


Most of this is good.  I laugh at (2) because I notoriously do not put documentation in.  Perhaps I should use ChatGPT to document my class code?  I don't use (4) for a couple of reasons.

1. you need to know ahead of time how many values you need to save if you use arrays
2. there is extra boilerplate code for setting up the initial arrays, and saving the data in the right indices

The `Storage()` class I made solves these problems, and is [discussed in more detail here](https://bblais.github.io/posts/2020/Feb/24/common-python-pattern-building-up-lists-to-plot/). 

Of course, ChatGPT wouldn't be expected to know that, but it does highlight some limitations.   We do (5) in later cells, and will do (1) later, but this code was just an introduction.  

### New code -- dangerous!

> **ME:**  how would you use this code to find the minimum and maximum of a function? please show the resulting code

What I was looking for is to use the derivative code above, find where it equals (or is close to) zero and return those points.  What I got was **incorrect code** described perfectly.  

> **ChatGPT:** To find the minimum and maximum of a function using this code, you can modify the code to keep track of the minimum and maximum values of the derivative. If the derivative at a point is zero, it means that the function has a local extremum (minimum or maximum) at that point.
>
Here's an updated version of the code that finds the minimum and maximum of a function:

```python
import numpy as np

def midpoint_method(fun, x_start, x_end, step):
    x = x_start
    min_x = max_x = None
    min_m = max_m = None
    while x <= x_end:
        y_left = fun(x - step / 2)
        y_right = fun(x + step / 2)
        m = (y_right - y_left) / step
        if min_m is None or m < min_m:
            min_m = m
            min_x = x
        if max_m is None or m > max_m:
            max_m = m
            max_x = x
        x += step
    return min_x, min_m, max_x, max_m

x_start = -5
x_end = 15
step = 1

min_x, min_m, max_x, max_m = midpoint_method(fun, x_start, x_end, step)

print("Minimum at x=", min_x, " with derivative ", min_m)
print("Maximum at x=", max_x, " with derivative ", max_m)
```

> In this updated version of the code, a function `midpoint_method` is defined to encapsulate the midpoint method. The function takes four arguments: `fun`, `x_start`, `x_end`, and `step`. The function returns four values: the `x`-coordinates and the values of the minimum and maximum derivatives.
>
In the main part of the code, the `midpoint_method` function is called with the input parameters, and the results are stored in `min_x`, `min_m`, `max_x`, and `max_m`. Finally, the minimum and maximum are printed.

This printed the **minimum and maximum of the derivative not the function**.  Unless you knew what was going on, this would be seriously dangerous to use.


### Finding resources -- useful


> **ME:** where can I learn more about numerical derivatives in python and include specific links


> **ChatGPT:** Here are several resources with specific links to help you learn about numerical derivatives in Python:
>
>1.  Online tutorials:
>
>-   The official Python documentation has a section on numerical differentiation: [https://docs.python.org/3/tutorial/floatingpoint.html](https://docs.python.org/3/tutorial/floatingpoint.html)
 -   A comprehensive tutorial on numerical derivatives in Python can be found here: [https://realpython.com/numerical-derivatives-python/](https://realpython.com/numerical-derivatives-python/)
>
> 2.  Books:
> 
> -   "Python for Data Analysis" by Wes McKinney covers the use of numerical methods in data analysis and provides examples using Python: [https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662)
> -   "Numerical Python" by Robert Johansson covers numerical methods and scientific computing using the Python programming language: [https://www.amazon.com/Numerical-Python-Scientific-Computing-Array/dp/1491911662](https://www.amazon.com/Numerical-Python-Scientific-Computing-Array/dp/1491911662)
> 
> 3.  Online courses:
> 
> -   Coursera offers several online courses on numerical methods and scientific computing in Python: [https://www.coursera.org/courses?query=numerical%20python](https://www.coursera.org/courses?query=numerical%20python)
> -   Udemy also has several online courses that cover numerical methods in Python: [https://www.udemy.com/topic/numerical-methods/](https://www.udemy.com/topic/numerical-methods/)
> -   edX offers a course on numerical methods for scientific computing with Python: [https://www.edx.org/learn/numerical-methods-for-scientific-computing-with-python](https://www.edx.org/learn/numerical-methods-for-scientific-computing-with-python)
> 
> 4.  Scientific libraries:
> 
> -   The `numpy` library in Python has a comprehensive documentation on numerical derivatives: [https://numpy.org/doc/stable/reference/routines.math.html#derivatives](https://numpy.org/doc/stable/reference/routines.math.html#derivatives)
> -   The `scipy` library also has a section on numerical derivatives: [https://docs.scipy.org/doc/scipy/reference/signal.html#differentiation](https://docs.scipy.org/doc/scipy/reference/signal.html#differentiation)
> 
> 5.  Community resources:
> 
> -   Stack Overflow is a great resource for asking questions and getting help with numerical derivatives in Python: [https://stackoverflow.com/questions/tagged/python](https://stackoverflow.com/questions/tagged/python)
> -   The official Python mailing list is another good resource for asking questions and getting help: [https://mail.python.org/mailman/listinfo/python-list](https://mail.python.org/mailman/listinfo/python-list)
> -   Reddit has several communities dedicated to Python programming, including r/learnpython and r/python, where you can ask questions and get help with numerical derivatives: [https://www.reddit.com/r/learnpython/](https://www.reddit.com/r/learnpython/) and [https://www.reddit.com/r/python/](https://www.reddit.com/r/python/)
> 


### Here's the Video Again


<iframe width="560" height="315" src="https://www.youtube.com/embed/H1fBdboJeBo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
