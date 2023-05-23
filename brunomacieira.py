"""
Find if number is prime

is_prime(int:number)

Find if list of numbers is prime

is_prime_list(list[int])
Returns prime numbers list
"""

def is_prime(num):
        is_prime = True

        if num <= 1 or (num % 2 == 0 and num != 2):
            is_prime = False
        else:
            for i in range(2, int(num / 2) + 1):
                if num == 1 and num % 2 == 0 and num % i == 0:
                    is_prime = False

        if is_prime == True:
            return True
        else:
            return False

def is_prime_list(*num):
    primes = []
    for item in num:
        a,b=(item,is_prime(item))
        if b==True:
            primes.append(a)
    return(primes)