
# in the given list find index of 5 , and check it.
nums = [1,2,3,4,5,6]
target = 5
found = False

for i , n in enumerate (nums):
    if target == n:
        found = True
        print(f"found on index :{i}") 

if found == True:
    print("found")
else:
    print("not found")






# find minimun number from the list without using min() function

lst = [4 , 7 , 1 , 9 , 3 ]
min_value = lst[0]  # for starting from index 0 

for i in lst:
    if i < min_value:  # if found min element
        min_value = i   # replace it 
print(min_value)






# find index of minimun number from the list without using min() function

lst = [4,7,1,9,3]
min_value = lst[0]
min_index = 0

for i , n in enumerate(lst):
    if n < min_value:
        min_value = n
        min_index = i

print(f"minimum value and its index = {min_value} = [{min_index}]")






    