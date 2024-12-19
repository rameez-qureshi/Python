
def table(n):
    for i in range(1,11):
        print (f"{n} x {i} = {n*i}")
        i = i + 1

n = int(input("Enter any number: "))
print(table(n))
