def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout
print(yell('Hello'))


def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)


def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))


# Decoratos

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")
        
    return inner1

def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()


def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")

        returned_value = func(*args, **kwargs)
        print("after Execution")

        return returned_value
        
    return inner1

@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

print("Sum =", sum_two_numbers(a, b))


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 2

@decor2
@decor1
def num2():
    return 2

print(num())
print(num2())


