Dict = {
    "Name" : "Rameez" ,
    "Age" : "Eighteen" ,
    "Marks" : [ 10, 10, 10] ,
    "anotherDict" : { "Key" : "Value" },
    1:2
}

print(Dict.keys())              # print keys of dictionary
print(type(Dict.keys()))
print(list(Dict.keys()))

print(Dict.values())            # print values of dictionary
print(Dict.items())             # print whole dictionary


updateDict = {
    "friend" : "Shubham"
}
Dict.update(updateDict)          # update the dictionary
print(Dict.keys()) 



print(Dict.get("Name"))     # Prints value associated with key "Rameez"
print(Dict["Name"])         # Prints value associated with key "Rameez"

# The difference between .get and [] sytax in Dictionaries?
print(Dict.get("harry2"))    # Results None as harry2 is not present in the dictionary
# print(Dict["harry2"])        # throws an error as harry2 is not present in the dictionary