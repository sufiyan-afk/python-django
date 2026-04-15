"""def onlystring(func):
    def wrapper(value):
        if value.isalpha():
            return func(value)
        else:
            return "Not a valid string"
    return wrapper


def onlynums(func):
    def wrapper(value):
        if value.isdigit():
            return func(int(value))
        else:
            return "Not a valid number"
    return wrapper


@onlystring
def get_string(value):
    return f"String value: {value}"


@onlynums
def get_number(value):
    return f"Number value: {value}"


x = input("Enter the value: ")

# Decide which function to call
if x.isalpha():
    print(get_string(x))
elif x.isdigit():
    print(get_number(x))
else:
    print("Invalid input")"""

