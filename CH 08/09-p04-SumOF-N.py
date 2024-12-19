# n! = (n-1) * n                    N factorial
# sum(n) = sum(n-1) + n           SUM facorial

def SumOfN(n):
    if n==0:
        return 0
    else:
        return n + SumOfN(n-1)

print(SumOfN(4))

a = int(input("Enter a positive integer: "))
z = SumOfN(a)
print(f"The sum of the first \" {a} \" natural numbers is: {z}")
