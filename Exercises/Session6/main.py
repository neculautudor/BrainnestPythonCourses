import re


def ex1(date):
    regx = re.compile(r"^[0-3]{0,1}\d{1}/[0-1]{1}\d{1}/\d{4}$")
    return regx.search(date)
# print(ex1('01/01/2000'))


def ex2(phoneNumber):
    regx = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return regx.match(phoneNumber)
# print(ex2('123-456-7890'))


def ex3(string):
    regx = re.compile(r'^\w+\W+\w+$')
    return regx.match(string)
# print(ex3('hello world'))


def ex4(string):
    regx = re.compile(r'^\d+\.\d{2}$')
    return regx.match(string)
# print(ex4('1.23'))


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f'My name is {self.name} and i am {self.age} years old')

    def greet(self):
        print('Greetings, how are you?')

    def __str__(self):
        return f'{self.name} {self.age} {self.address}'
person = Person('tudor', 23, 'london')
# print(person)


class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('*animal sound*')


class Dog(Pet):
    def __init__(self):
        super().__init__('Toto')

    def speak(self):
        print('WOOF')


class Cat(Pet):
    def __init__(self):
        super().__init__('Tiberiu')

    def speak(self):
        print('MIAU')
