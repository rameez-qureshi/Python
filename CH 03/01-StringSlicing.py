# greeting = "Good Morning, "
# name = "Harry"
# print(type(name))
# c = greeting + name
# print(c)


# STRING SLICING

name = "Harry"
print(name[4])                      # name[3] = "d" --> Does not work
print(name[1:4])
print(name[:4])                 # is same as name[0:4]
print(name[1:])                 # is same as name[1:5]
c = name[-4:]                 # is same is name[1:5]
print(c)

# name = "HarryIsGood"
# z = name[0::3]
# print(z)
# d = name[:0:-1]
# print(d)


# STR SICING WITH SKIP VALUE

name = "HarryIsGood"    # Length is 11
# b= name[0:11:1]       # same as name [0:11]
b= name[0:11:2]
print(b)