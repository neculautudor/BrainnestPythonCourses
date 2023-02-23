

#TODO check
# import math
# def findLargestPrimeFactor(n):
#     maxPrime = -1
#     while not n % 2:
#         n /= 2
#         maxPrime = 2
#     while not n % 3:
#         n /= 3
#         maxPrime = 3
#     for i in range(5, int(math.sqrt(n)) + 1, 6):
#         while not n % i:
#             n /= i
#             maxPrime = i
#         while not n % (i + 2):
#             maxPrime = i + 2
#             n = n / (i + 2)
#     if n > 4:
#         maxPrime = n
#     return maxPrime
# print(findLargestPrimeFactor(600851475143))
def gcd(x, y): return y and gcd(y, x % y) or x

# def test(): return a() and b()
# def a():
#     print('a')
#     return 2
# def b():
#     print('b')
#     return 1
# print(test())
def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x, y)
n = 1
for i in range(1, 21):
     n = lcm(n, i)
print('the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:', n)
#
# def has_all_divisors(number):
#     for no in range(20, 1, -1):
#         if number % no != 0:
#             return False
#     return True
#
#
# for number in range(1, 1000000000000):
#     if has_all_divisors(number):
#         print(number)
#         break
#
# def isPrime(x):
#     prime = True
#     for i in range(2, x):
#         if x % i == 0:
#             prime = False
#             break
#         else:
#             continue
#     return prime
#
# primes = (a for a in range(2, 2000000) if isPrime(a))
# print(sum(primes))

# import math
# def isPrime(n):
#     if n < 4:
#         return True
#     if not n % 2:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if not n % i:
#             return False
#     return True
# curPrimePos = 2
# curNr = 3
# curPrimeNr = curNr
# while curPrimePos <= 10001:
#     if isPrime(curNr):
#         curPrimePos += 1
#         curPrimeNr = curNr
#     curNr += 2
# print(curPrimeNr)
