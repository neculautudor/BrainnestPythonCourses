import math


def create_adder(x):
    def adder(y):
        return x+y

    return adder

# add_15 = create_adder(15)
# print(add_15(10))

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

#
# a, b = 1, 2
#
# print("Sum =", sum_two_numbers(a, b))


def greet(func):
    def inner(*args):
        print('greet')
        return func(*args)
    return inner

@greet
def say_hello():
    print('say_hello')

# say_hello()


def authorize(func):
    def wrapper(password):
        if is_authorized(password):
            func()
        else:
            return 'Unauthorized access'

    def is_authorized(password):
        return password == 'pass'

    return wrapper

@authorize
def secret_data():
    print('This is confidential data')

# print(secret_data('pass'))

def validate(func):
    def wrapper(*args):
        if not all([isinstance(x, (int, float)) for x in args]):
            return 'Invalid argument type'
        return func(*args)
    return wrapper

@validate
def add(*args):
    return sum(args)

# print(add(1, 2, 3, 4, '6'))

def isPrime(nr):
    if nr <= 0:
        return False
    if nr == 1 or nr == 2:
        return True
    for i in range(2, int(math.sqrt(nr) + 1)):
        if not nr % i:
            return False
    return True


def primeNumbers(limit):
    i = 2
    while limit:
        if isPrime(i):
            yield i
            limit -= 1
        i += 1

# prime_generator = primeNumbers(10)
# print(list(prime_generator))


def generate(word, filename):
    with open(filename) as f:
        for line in f:
            if word in line:
                yield line
lines_generator = generate('tudor', 'last_exercise_file.txt')
print(list(lines_generator))
