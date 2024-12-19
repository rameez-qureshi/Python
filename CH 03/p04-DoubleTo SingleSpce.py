str = "This is a string with double  spaces and we replace double  space from single space."


st = str.find("  ")
print(st)

ds = str.replace("  "," ")            # ds means double spaces
print(ds)


# str = str.replace("  "," ")           # if we keep name of str same no problem
# print(str)

# print(str.replace("  "," "))         # another method