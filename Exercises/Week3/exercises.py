import os


def ex1():
    filename = input('Enter the file name: ')
    with open(filename) as f:
        return f.read().upper()
# print(ex1())

def ex2():
    filename = input('Enter the file name: ')
    if filename == 'test.txt':
        return 'I just don\'t feel like opening the file'
    else:
        try:
            f = open(filename)
            return f.read()
        except ValueError:
            return ValueError
# print(ex2())

def ex3():
    total = 0
    with open('mbox-short.txt') as f:
        for line in f:
            line = line.split(' ')
            if line[0] == 'From':
                print(f'Sender: {line[1]}')
                total += 1
    print(f'Total number of lines: {total}')
# ex3()

def ex4():
    institutions_frequency = {}
    with open('mbox-short.txt') as f:
        for line in f:
            line = line.split(' ')
            if line[0] == 'From':
                domain = line[1].split('@')[1]
                if domain in institutions_frequency.keys():
                    institutions_frequency[domain] += 1
                else:
                    institutions_frequency[domain] = 1
    return institutions_frequency
# print(ex4())

# tuples exercises

def tuple_ex1(tpl):
    setCheck = set()
    repeatedElements = set()
    for element in tpl:
        if element in setCheck:
            repeatedElements.add(element)
        else:
            setCheck.add(element)
    return repeatedElements
# print(tuple_ex1((1, 2, 3, 1, 2, 4, 5, 3, 7)))


def tuple_ex2(tpl):
    secondHalfIncrement = 0 if len(tpl) % 2 else 1
    return tpl[:len(tpl)//2] == tpl[-1:len(tpl)//2 - secondHalfIncrement:-1]
# print(tuple_ex2((1, 2, 3, 4, 5, 4, 3, 2, 1)))


def tuple_ex3(tpl):
    freq = {}
    for element in tpl:
        if element in freq.keys():
            freq[element] += 1
        else:
            freq[element] = 1
    return freq
# print(tuple_ex3((1, 2, 3, 1, 3, 4)))


def tuple_ex4(tpl):
    even_elements = []
    for element in tpl:
        if not element % 2:
            even_elements.append(element)
    return tuple(even_elements)
# print(tuple_ex4((1, 2, 3, 4, 5, 6)))


def tuple_ex5(tpl):
    new_tpl = set()
    unique = set()
    for element in tpl:
        if element in unique:
            new_tpl.remove(element)
            continue
        unique.add(element)
        new_tpl.add(element)
    return tuple(new_tpl)
print(tuple_ex5((1, 2, 3, 4, 5, 1)))


