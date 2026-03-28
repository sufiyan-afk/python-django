#   1.  string  methods and functions

s = "hello world"

print(s.upper())          # converts to uppercase
print(s.lower())          # converts to lowercase
print(s.capitalize())     # first letter uppercase
print(s.title())          # every word first letter uppercase

print(s.strip())          # removes spaces from both sides
print(s.lstrip())         # removes spaces from left
print(s.rstrip())         # removes spaces from right

print(s.replace("hello", "hi"))  # replaces substring

print(s.split(" "))       # splits string into list
print(s.join(["a","b"]))  # joins list into string

print(s.find("world"))    # returns index of substring (-1 if not found)
print(s.index("world"))   # returns index (error if not found)

print(s.count("l"))       # counts occurance of character

print(s.startswith("he")) # returns True/False
print(s.endswith("ld"))   # returns True/False

print(s.isalpha())        # only letters? True/False
print(s.isdigit())        # only digits? True/False
print(s.isalnum())        # letters + digits? True/False
print(s.isspace())        # only spaces? True/False

print(s.len())            # length of string
print(len(s))             # correct way

print(s[0])               # indexing
print(s[0:5])             # slicing


# 2. all list methods / functions

l = [3,4,3,1,2,5]

l.append(6)      # add value at the end
print(l)

l.insert(1, 9)   # add value in given position or index
print(l)

l.remove(1)      # removes the first occurance
print(l)

l.pop()          # removes the last element of the list
print(l)

l.sort()         # sorting in asc or desc
print(l)

l.reverse()      # reverses the list
print(l)

l.index(2)       # returns index of given value
print(l)

l.count(3)       # counts the repitition of value
print(l)

l.clear()        # removes all elements
print(l)


# 3. all tuple methods

t = (1,2,2,3)

t.count(2)       # counts the repitition of value
print(t)

t.index(3)       # returns index of given value
print(t)


# 4. all set methods

s = {1,2,3}

s.add(4)              # add one element
s.update([5,6])       # add multiple elements
s.remove(2)           # removes element (error if not found)
s.discard(2)          # removes element (no error if not found)
s.pop()               # removes random element
s.clear()             # removes all elements
print(s)

s1 = {1,2,3}
s2 = {3,4,5}

s1.union(s2)          # combines both sets
s1.intersection(s2)   # common elements only
s1.difference(s2)     # elements in s1 not in s2
print(s1)



#          5. all   dictionary

clear()
copy()
fromkeys()
get()
items()
keys()
pop()
popitems()
setdefault()
update()
values()

