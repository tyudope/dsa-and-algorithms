"""
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""

def isUgly(n:int ) -> bool:

    for p in (2,3,5):
        while (n % p == 0) and 0 < n:
            n /= p

    return n == 1

    
"""
Approach:
    Divide out every factor of 2, 3, and 5 in turn. If only those primes
    built n, nothing else remains and n reduces to 1.

Time:  O(log n) — each division at least halves n (factor of 2 case is the slowest).
Space: O(1) — divides in place, no extra structure.

Assumes positive n; the `0 < n` guard rejects zero and negatives (not ugly).
"""