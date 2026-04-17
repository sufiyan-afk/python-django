# find max element in the list without using max function

lst = [3,6,2,10,20,1]
max_num = lst[0]

for i in lst:
    if i > max_num:
        max_num = i
print(max_num)


# find min element in the list without using min function

lst = [2,34,2,4324,52,1]
min_val= lst[0]

for i in lst:
    if i < min_val:
        min_val = i
print(min_val)





# reverse the list without using reverse() method
lst = [1,2,3,4,5]

# swap 1 : index 0  and 4 
temp = lst[0]             # temp = lst[0] --> 1
lst[0] = lst [4]          #lst[0] = lst[4] --> 5
lst[4] = temp             #lst[4] = temp --> 1
print(lst)          # -->    lst = [5,2,3,4,1]
#swap 2 : index 1 and 3
temp = lst[1]             # temp = lst[1]  --> 2
lst[1] = lst [3]          #lst[1] = lst[3] --> 4
lst[3] = temp             #lst[3] = temp   --> 2
print(lst)         # final swap --> [5,4,3,2,1]
