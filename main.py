import random
import math
import inflect

p = inflect.engine()

def is_prime(n, k=3):  # Reduced the number of Miller-Rabin tests for speed
    if n <= 1:
        return False
    if n <= 3:
        return True

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def witness(a, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if witness(a, d, n):
            return False

    return True

def find_large_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate

bits = 20
prime = find_large_prime(bits)
prime_str = str(prime)
num_digits = len(prime_str)

magnitude = "Unknown"

# Determine magnitude and set magnitude string accordingly
if num_digits >= 12:
    magnitude = "Trillion"
elif num_digits >= 9:
    magnitude = "Billion"
elif num_digits >= 6:
    magnitude = "Million"
elif num_digits >= 3:
    magnitude = "Thousand"

# Convert single-digit numbers to words
if num_digits == 1:
    magnitude = p.number_to_words(num_digits * 10)

prime_in_words = p.number_to_words(prime)  # Using inflect for converting to words

print(f"A randomly generated {bits}-bit prime number:")
print(f"Prime Number: {prime}")
print(f"Number of digits: {num_digits}")
print(f"In words, it's approximately {prime_in_words} {magnitude}.")
