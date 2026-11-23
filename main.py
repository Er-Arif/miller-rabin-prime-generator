"""Educational Miller–Rabin primality checks and probable-prime generation."""
from __future__ import annotations

import argparse
import secrets

_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_probable_prime(number: int, rounds: int = 24) -> bool:
    """Return whether number passes the specified Miller–Rabin rounds."""
    if rounds < 1:
        raise ValueError("rounds must be positive")
    if number < 2:
        return False
    for prime in _SMALL_PRIMES:
        if number == prime:
            return True
        if number % prime == 0:
            return False

    d = number - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        base = secrets.randbelow(number - 3) + 2
        x = pow(base, d, number)
        if x in (1, number - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True


def generate_probable_prime(bits: int, rounds: int = 24) -> int:
    """Generate an odd probable prime with exactly bits bits."""
    if bits < 2:
        raise ValueError("bits must be at least 2")
    if rounds < 1:
        raise ValueError("rounds must be positive")
    while True:
        candidate = secrets.randbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(candidate, rounds):
            return candidate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=32)
    parser.add_argument("--rounds", type=int, default=24)
    args = parser.parse_args()
    prime = generate_probable_prime(args.bits, args.rounds)
    print(f"Probable {args.bits}-bit prime: {prime}")
    print(f"Bit length: {prime.bit_length()}")
    print(f"Miller–Rabin rounds: {args.rounds}")


if __name__ == "__main__":
    main()
