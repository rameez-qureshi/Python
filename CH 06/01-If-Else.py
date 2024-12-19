# CONDITIONALS

# 2. IF ELSE STATEMENTS LADDER -----------------------------------

# a = int(input("Enter any number below 100: "))
# if ( a<20 ):                                             # this code give result only 1 statement acc to "a" .
#     print( "The value of \"a\" is less than 20" )
# elif ( a<40 ):
#     print( "The value of \"a\" is less than 40" )
# elif ( a<60 ):
#     print( "The value of \"a\" is less than 60" )
# elif ( a<80 ):
#     print( "The value of \"a\" is less than 80" )
# elif ( a<100 ):
#     print( "The value of \"a\" is less than 100" )
# else :
#     print( "The value of \"a\" is greater than than 100" )

# 2. MULTIPLE IF STATEMENTS ----------------------------------------

a = int(input("Enter any number below 100: "))

if ( a<25 ):                                             # this code give multiple results
    print( "The value of \"a\" is less than 25" )        # Every IF statement has their own identity
                                                         
if ( a<50 ):                                             # not any relation between IF statements 
    print( "The value of \"a\" is less than 50" )

if ( a<75 ):
    print( "The value of \"a\" is less than 75" )

if ( a<100 ):
    print( "The value of \"a\" is less than 100" )
else :
    print( "The value of \"a\" is greater than than 100" )

print("Done")