from statistics import mean


def calculatePay(hours, rate):
    overtime = hours - 40
    if overtime < 0:
        overtime = 0
    else:
        hours = 40
    return overtime * 1.5 * rate + hours * rate

def getGrade():
    try:
        score = float(input('Score: '))
    except:
        return None
    score = float(score)
    if score < 0 or score > 1:
        return None
    if score > 0.9:
        return 'A'
    if score > 0.8:
        return 'B'
    if score > 0.7:
        return 'C'
    if score > 0.6:
        return 'D'
    return 'F'
# print(getGrade())
#
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')

def chat(time_of_day):
    print(f'Good {time_of_day}!')
    print('How are you feeling?')
    feeling = input()
    print(f'I am happy to hear that you are feeling {feeling}.')

# times_of_day = ['morning', 'afternoon', 'evening']
# for time_of_day in times_of_day:
#     chat(time_of_day)


def getMean():
    numbers = []
    while True:
        number = input('Enter a number:')
        if number == 'done':
            break
        try:
            number = float(number)
        except:
            print('Invalid input')
            continue
        numbers.append(number)
    return mean(numbers)
print(getMean())


























