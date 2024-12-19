
a = int(input("Enter any number: "))

if ( a>0 and a<10 ) :                      # PASS Statement will do nothing just pass the line 
    print("greater than 0")                # Pass statement is like null statement in python 
elif ( a>10 and a<20 ) :                   
    pass                                   # when you enter number b/w 10 and 20 it give no result.
elif ( a>20 ) :   
    print("greater than 20")
else :
    print("greater")

print("Done")