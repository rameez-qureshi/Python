
# n = 5
# factorial = 1
# for i in range (n):
#     factorial = factorial * (i+1)
# print(factorial)

def factorial(n):
    f = 1
    for i in range (n):
        f = f * (i+1)
    return f

print(factorial(4))

z = factorial(6)
print(z)