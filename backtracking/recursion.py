"""
Recursion is a programming technique where a function calls itsel, directly or indirectly,
to solve smaller version of same problem. Thik of it as breaking down a complex problem into simpler, identical
subproblems, until a basic case is reached.

Key Components of Recursive function:
Base Case: Condition under which the function stops recursing and returns a value
Recursive Case: The part where the function calls itself with modified input.
"""

def factorial(n):
    # Base: When 0 or 1m the factorial is 1 
    if n ==0 or n == 1:
        return 1 
    
    # Recursue step
    else:
        return n * factorial(n-1)
    
print(factorial(5))