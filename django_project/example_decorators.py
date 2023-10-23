# Example 1
def say_hi(name):
    return f"Hi, {name}!"

def say_hello_formal(name):
    return f"Good morning, Sir/Madam {name}."

def greet_alice(greeter_func):
    return greeter_func("Alice")

test = greet_alice(say_hello_formal)
# print(test)

# Example 2
def double(number):
    return number * 2

def plus_one(number):
    return number + 1

def square(number):
    return number * number

data = [1, 2, 3, 4, 5]

def apply(sequence, operation_func):
    result = []
    for n in sequence:
        result.append(operation_func(n))
    return result

# print(apply(data, square))

# Example 3

def get_greeting(number):

    def first():
        print("Hi!")
    
    def second():
        print("Welcome aboard!")
    
    if number == 1:
        return first
    else:
        return second

my_func = get_greeting(2)
# my_func()


# Example 4

def first_decorator(func):
    def wrapper():
        print("We are before func!!")
        func()
        print("We are after func...")
    
    return wrapper

def say_something():
    print("Something!")

@first_decorator
def say_something_else():
    print("Something else!")


say_something = first_decorator(say_something)
say_something()
say_something_else()
