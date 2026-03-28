#concatination
# str1 = "Sufiyan"
# str2 = " Tal"
# final_str = str1 +str2
# print (len(final_str))

#slicing
# str = "sufiyan tal"
# print(str[1:4])
# print(str[ :4])
# print(str[1:])

#basic string operations
# 1.  concatination
"""
str1 = "Hello everyone"
str2 = " My name is Sufiyan"
final_str = str1 + str2
print(final_str)
"""

# 2. functionfinding length 
"""
str = "Sufiyan"
print(len(str))
"""

# 3. indexing : position assigned to a character
#  S u f i y a n _ t a l
#  0 1 2 3 4 5 6 7 8 9 10 
#negative slicing -3 -2 -1 position

# accesing character through index = str[] function
"""
str = "Sufiyan_tal"
print(str[2])
"""

# we cannot manipulate or modify string directly with indexing


# Slicing : accesing parts of a string
#eg str[starting_idx : ending_idx]
# ending is always exclusive

"""
str = "sufiyan_tal"
print(str[0 : 7]) #is sufiyan
"""

# negative index : means it acts as a reverse function

"""
str = "sufiyan_tal"
print(str[-1]) #is 'l'
print(str[-12 : len(str)])# is sufiyan_tal
"""

# string functions

str = "i am studying python from Tops Technologies"

print(str.endswith("es")) # returns true if string is ending with subject of str
print(str.capitalize()) # capitalizes 1st character
print(str.replace("python","full stack"))# replaces all occurance of old with new
print(str.find("python"))# returns 1st index of 1st occurance
print(str.count("o"))# counts how many times substr in string occured











