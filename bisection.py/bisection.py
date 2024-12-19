def f(x):
    return x**3-4*x-9

def bisection (a,b,n) :
    Condition = True              # loop K lie
    i = 1                         # iteration Klie

    while condition:
        x = (a+b)/2
        if x > 0:
            a = x
        else:
            b = x
        print (f"iteration={i} , x={x} , F(x) = {f(x)}")
         
# for iteration
    if i==n:
        condition = False   # (loop-faise)
    else:
        condition = True    # (loop-true)
        i = i + 1

a = float(input("Enter First approx: "))
b = float(input("Enter Second approx: "))
n = int(input("Enter number of iteration: "))

if f(a) * f(b) > 0:
    print ("invalid value of approx")
    print ("Try again")
else:
    bisection (a, b, n)