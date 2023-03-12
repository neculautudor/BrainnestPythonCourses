def ex1(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    N = len(coins)
    number_of_combinations = 0

    def backtracking(sum, index):
        nonlocal number_of_combinations
        if sum == target:
            number_of_combinations += 1
            return
        if sum > target:
            return
        for i in range(index, N):
            backtracking(sum + coins[i], i)
    backtracking(0, 0)
    return number_of_combinations
# print(ex1(200))


def ex5():
    primes = set()
    non_primes = set()
    rotational_primes = [2]

    def is_prime(n):
        if not n % 2:
            return False
        for i in range(3, int(n ** 0.5) + 1):
            if not n % i:
                return False
        return True

    def get_all_rotations(n):
        numbers = []
        string_number = str(n)
        for i in range(len(string_number)):
            numbers.append(int(string_number[-i:] + string_number[:-i]))
        return numbers

    def check_rotations(rotations):
        for rotation in rotations:
            if rotation in primes:
                continue
            if rotation in non_primes:
                return False
            if is_prime(rotation):
                primes.add(rotation)
            else:
                non_primes.add(rotation)
                return False
        return True
    for i in range(3, 1000000, 2):
        rotations = get_all_rotations(i)
        if check_rotations(rotations):
            rotational_primes.append(i)
    return rotational_primes


# print(ex5())

