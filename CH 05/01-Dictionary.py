MyDict = {
    "Name" : "Rameez" ,                           # First name is key and second is its value
    "Age" : "Eighteen" ,
    "Marks" : [ 10, 10, 10] ,
    "anotherDict" : { "Key" : "Value" }
}

print(MyDict["Name"])
print(MyDict["Marks"])
print(MyDict["anotherDict"])
print(MyDict["anotherDict"]["Key"])

MyDict["Name"] = "Shaka"
print(MyDict["Name"])

MyDict["Marks"] = [25, 50]
print(MyDict["Marks"])

# Dictionary is unordered
# Dictionary is changeable
# Dictionary is indexed
# Dictionary can't contain duplicate keys