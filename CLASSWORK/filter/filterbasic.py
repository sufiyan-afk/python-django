# filter: this function will iterate the elements in the list and give out on the basis of true and false
# if the condition gets false it wont give output , so it give only the out which satisfies the condition
marks = [77 , 97 , 64 , 35 , 55]

def failing(score):
    return score < 60

result = filter(failing,marks)
print("Failing score",list(result))  