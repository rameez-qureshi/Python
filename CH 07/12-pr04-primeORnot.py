
n = int(input("Enter any number: "))

prime = True

for i in range ( 2,n ):
    if(n%i == 0):
        prime = False
        break

if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")