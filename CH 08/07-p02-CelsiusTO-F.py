
def celsius(num):
    p =  (num * 9/5) + 32
    return p


a = celsius(60)
print(a)

n = int(input("Enter temp in celcius: "))
z = celsius(n)
print(f"{n} in fahrenheit is {z}")