UrduDict = {
    "Mango" : "Aam",
    "Apple" : "Seib",
    "Banana" : "Keela",
    "Watermelon" : "Tarbooz",
    "Kiwi" : "Keewe",
}

print("Options", list(UrduDict.keys()))
a = input("Enter any fruit name: ")

# b=UrduDict[a]                   # this method will print error if enter key is not present.
# print(a,"in urdu is",b)

b=UrduDict.get(a)                # this method will print none if enter key is not present.
print(a,"in urdu is",b)