# Miller–Rabin Prime Number Lab

A small Python learning project exploring probabilistic primality testing and random prime generation.

## What it demonstrates

- Decomposing `n - 1` into `2^s × d` for Miller–Rabin witness tests
- Modular exponentiation with Python's `pow(base, exp, mod)`
- Generating odd candidates with an exact requested bit length
- Using `secrets` rather than the general-purpose `random` module
- Unit tests for small primes, composites, and Carmichael numbers

## Run

Requires Python 3.10+; no third-party packages.

```bash
python main.py --bits 32 --rounds 24
python -m unittest discover -s tests -v
```

Example output (your number will differ):

```text
Probable 32-bit prime: ...
Bit length: 32
Miller–Rabin rounds: 24
```

## Notes and limits

This is an **educational experiment**, not a cryptographic key generator. Passing Miller–Rabin means *probably prime*; it is not a mathematical proof. For security-sensitive applications use a vetted cryptographic library and established protocols.

The initial college-era script is preserved in the repository's Git history. This revision makes the experiment reproducible and testable.
