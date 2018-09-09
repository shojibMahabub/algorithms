from timeit import timeit


def sieve(limit):
    # returns a list of prime number
    prime = [True] * limit
    for number in range(3, limit, 2):
        if number**2 > limit:
            break
        if prime[number]:
            for other in range(number * number, limit, 2 * number):
                prime[other] = False
    return [2] + [number for number in range(3, limit, 2) if prime[number]]


test = lambda value: timeit(lambda: value(10000000), number=1)
reference = test(sieve)
print(reference)
