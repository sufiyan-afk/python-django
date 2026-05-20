marks = [77 , 97 , 64 , 85 , 55]

def grade(marks):
    if marks >= 90:
        return 'A'
    
    elif 80 <= marks < 90 :
        return 'B'
    
    elif 70 <= marks <80:
        return 'C'
    
    elif 60 <= marks <70:
        return 'D'
    
    else:
        return 'F'
    
grade = map(grade , marks)
print("Exam scores:",marks)
print("grades:" , next(grade))  # it will iterate the list one by one   ---  output --> C because 77 lies in C grade
print("grades: ",list(grade))   # it will give iterate the list and give the output of all at once in the form of list ---  ['c' , 'A' , 'D' ,' B' ,'F']
