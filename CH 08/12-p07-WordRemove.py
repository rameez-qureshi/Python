
def remove_word_in_string( str , word):
    newstr = str.replace( word ,"")             # replace word with empty space
    return newstr.strip()                         # .strip can remove empty spaces from string



a = input("Enter string: ")
b = input("Enter word want to remove from string: ")
z = remove_word_in_string( a , b )
print(z)