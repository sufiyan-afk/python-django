print("program started")

try:
    a=10
    b=a/0
    print(b)
    print(10+"mdkad")

except Exception as e:
    print("exception")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

else:
    print("execute sucessfully")
finally:
    print("always executable")