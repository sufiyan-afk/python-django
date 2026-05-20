#add two marks in every existing marks


#  1. without list comprehension
marks = [20,30,40,50,60]
new_marks = []
for x in marks:
    new_marks.append(x+2)
print(new_marks)


# 2. with list comprehension

marks = [20,30,40,50,60]
new_marks = [x+2 for x in marks]
print(new_marks)

#print cube of every even number in range 10
cube = []
for i in range(10+1):
    if i % 2 == 0:
        cube.append(i ** 3)
print(f"using for loop: {cube}")


cube = [i**3 for i in range(10+1) if i %2 ==0 ]
print(f"using list comprehension : {cube}")