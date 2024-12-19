# LOGICAL AND RELATIONAL OPERATORS    ( AND, OR ,NOT )

a = int(input("Enter your Age: "))              # both statement true so print 
if ( a>20 and a<60 ):
    print("you are eligible")
else:
    print("you are not eligible")

# a = int(input("Enter your Age: "))              # Anyone is statement is true so print 
if ( a>20 or a<10 ):
    print("you are eligible")
else:
    print("you are not eligible")

# a = int(input("Enter your Age: "))              # Not statement is print when input is opposite
if ( not a!=10 ):
    print("you are eligible")
else:
    print("you are not eligible")