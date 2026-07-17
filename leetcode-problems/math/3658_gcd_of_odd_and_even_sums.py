"""
You are given an integer n, Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the smallest n positive odd numbers.
sumEven: the sum of the smallest n positive even nubers.

Return the GCD of sumOdd and sumEven.

"""


def gcdOfOddEvenSums(n:int) -> int:

    def gcd(x:int, y:int) -> int:
        smallest, biggest = min(x,y), max(x,y)
        gcd = 1
        for i in range(1, smallest):
            if biggest % i == 0 and smallest % i == 0:
                gcd = i

        return gcd

    i = 0

    sumOdd = 0
    sumEven = 0
    evenNum = 1
    oddNum = 2
    while i < n:
        if i != 0:
            evenNum += 2
            oddNum += 2
        sumEven += evenNum
        sumOdd += oddNum
        i+= 1
    
    return gcd(sumEven, sumOdd)


print(f"{gcdOfOddEvenSums(4)}")