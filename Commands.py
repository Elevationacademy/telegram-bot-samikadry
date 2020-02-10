import math


def isPrime(num):
    if num > 1:
        for i in range(2, (num // 2)+1):
            if (num % i) == 0:
                return f"{num} isn't a prime number"
        else:
            return f"{num} is a prime number"
    else:
        return f"{num} isn't a prime number"


def isFactorial(num):
    fact = i = 1
    while i <= num:
        fact *= i
        i += 1
        if fact == num:
            return f"{num} is a result of factorial operation"
    return f"{num} isn't a result of factorial operation"


def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return f"{num} is PALINDROME"
    return f"{num} isn't PALINDROME"


def isIntegerSqrt(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return f"{num} have an integer square root"
    return f"{num} doesn't have an integer square root"
