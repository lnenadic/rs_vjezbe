def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(isPrime(7))
print(isPrime(10))


def primes_in_range(start, end):
    primes = []
    for numbers in range(start, end + 1):
        if isPrime(numbers):
            primes.append(numbers)
    return primes


print(primes_in_range(1, 10))
