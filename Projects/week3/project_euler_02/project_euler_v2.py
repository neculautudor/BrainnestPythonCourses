# did exercises 1, 2, 3, 4, 6

def ex1():
    '''we only need to work with the last 10 digits of all the numbers, and the result as well'''
    with open('ex1_numbers') as text:
        numbers = text.readlines()
    try:
        numbers = [int(number) for number in numbers]
    except ValueError as msg:
        print(f'One of the numbers could not be converted, {msg}')
        return
    last_ten_digits = 0
    for number in numbers:
        last_ten_digits += (last_ten_digits + (number % (10 ** 10))) % 10 ** 10
    return last_ten_digits
# print(ex1())

def ex2():
    already_checked = set()
    highest_length_number = 1
    highest_length = 0
    '''function for getting the length of a number chain'''
    def collatz_chain_length(nr):
        chain_length = 1
        while nr > 1:
            nr = nr // 2 if not nr % 2 else nr * 3 + 1
            '''adding all the numbers in a chain to an exclusion set, because, being in the inner part of a chain, they
            will automatically have less length than the number we're checking right now, therefore we will avoid it
            (results in function running twice faster for 1 million)'''
            already_checked.add(nr)
            chain_length += 1
        return chain_length

    for i in range(2, 10 ** 6):
        '''skipping the numbers that appeared in the inner of a chain'''
        if i in already_checked:
            continue
        cur_length = collatz_chain_length(i)
        if highest_length < cur_length:
            highest_length, highest_length_number = cur_length, i
    return highest_length_number
# print(ex2())


def ex3():
    return sum([int(c) for c in list(str(2 ** 1000))])
# print(ex3())

def ex4():
    '''contains all the verbally special numbers'''
    numbers_to_verbal = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        1000: 'onethousand',
    }

    def verbal_number(number):
        if number == 1000:
            return numbers_to_verbal[number]
        hundreds = ''
        if number > 99:
            hundreds = f'{numbers_to_verbal[number // 100]}hundred'
            number %= 100
            if not number:
                return hundreds
            hundreds = ''.join([hundreds, 'and'])
        try:
            last_two = numbers_to_verbal[number]
        except KeyError:
            last_two = ''.join([numbers_to_verbal[number - number % 10], numbers_to_verbal[number % 10]])
        return ''.join([hundreds, last_two])

    total_length = 0
    for i in range(1, 1001):
        total_length += len(verbal_number(i))
    return total_length
# print(ex4())


def ex6():
    '''the digit sum of the product of two numbers is equal to the product of the digit sums of each number
    digitSum(a*b) = digitSum(a) * digitSum(b) => digitSum(100!) = digitSum(1) * digitSum(2) * ... * digitSum(100)'''
    def digit_sum(nr):
        return sum([int(c) for c in list(str(nr))])
    total_sum = 1
    for i in range(2, 100):
        total_sum *= digit_sum(i)
    return total_sum
# print(ex6())
