
def convert_inches_to_cm(num):
    p =  (num*2.54)
    return p


a = int(input("Enter Inches: "))
z = convert_inches_to_cm(a)
print(f"{a} in cm is: {z}")