
# RECURSION

# this is a method which call itself in a function. for further info goto notes

def factorial_recursion(n):                           # 4 x factorial(3)
    if n==1 or n==0:                                  # 4 x [ 3 x factorial(3) ]
        return 1                                      # 4 x 3 x  [ 2 x factorial(1) ]
    return n * factorial_recursion(n-1)               # 4 x 3 x 2 x 1

print(factorial_recursion(6))

z=factorial_recursion(8)
print(z)