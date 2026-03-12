# #while loop

#break statement :
#find even numbers from 1 to 20
# i=0
# while i<=20:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i += 1


# #1. basics of while loop
# count = 1
# while count <= 5 :
#     print("hello world")
#     count+=1

#question 1
#print multiplication table
# n = int (input("enter a number : "))
# i=1
# while i <= 10:
#     print(n*i)
#     i += 1

#question 2 a
#print the elements of the following list using loop
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1

#b
# heroes = ["ironman","thor","hulk","batman","superman"]
# idx = 0
# while idx < len(heroes) :
#     print(heroes[idx])
#     idx += 1

#question 3
#search for a number x in tuple using loop

# nums = (1,4,9,16,81,25,36,49,64,81,100)
# x = 81
# i = 0
# while i < len(nums):
#     if(nums[i] == x ):
#         print("found at index : ",i)
#         break
#     else :
#         print("finding..")
#     i += 1
# print("end of loop")

# # counting positive numbers
# numbers = [1,-2,3,4,-5,-6,5]
# positive_numbers_count = 0
# for num in numbers :
#     if num > 0 :
#         positive_numbers_count += 1
# print(f"positive numbers = {positive_numbers_count}")

# n = int (input ("enter a number : "))
# sum = 0
# for n in range (1,n+1):
#     if n%2 == 0 :
#         sum += 1
# print(f"sum of even numbers : {sum}")


# number = 4
# for i in range (1,11) :
#     if i == 5 :
#         continue
#     print(f"{number} x {i} = {number * i}")

# str = "sufiyan"
# rev_str = ""
# for char in str :
#     rev_str = char + rev_str
# print(rev_str)

#find the first non repeatable char pf string
# str = "teeterabab"

# for char in str :
#     print (char)
#     if str.count(char) == 1 :
#         break
# print(f"char is : {char}")

# num = 6
# temp = num
# fact = 1
# while num > 0 :
#     fact *= num
#     num -= 1
# print(f"factorial of {temp} is = {fact}")
# 

#take input from user untill it gives number b/w 1 to 10
# while True:
#     number = int(input("enter number between 1 to 10 : "))
#     if 1<= number <=10:
#         print("thanks")
#         break
#     else:
#         print("invalid number ! try again")

# num = 6
# is_prime = True
# if num > 1 :
#     for i in range(2,num):
#         if (num %i) ==0 :
#             is_prime = False
#             break

# print(f"{is_prime}")

#check if any items is duplicate is not
# items = ["bat","ball","football","bat"]
# unique_item = set()

# for item in items :
#     print(items)
#     if item in unique_item:
#         print(f"duplicate : {item}")
#         break
#     unique_item.add(item)

# #exponential backoff : (used in real world like password)
# """implement an exponential backoff strategy 
# that doubles the wait time betn retries ,
#  starting from 1 second ,but stops after 5 retries""" 

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries :
#     print(f"attempt {attempts + 1 } - wait time {wait_time}")
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1




