# The Sieve of Eratosthenes
#   An algorithm for counting prime numbers named after an ancient greek mathematician
#   Sift the twos & sift the threes, the sieve of eratosthenes.
#   When the multiples sublime, the numbers that remain are prime

def sieve():
    n = 20  # end of the range of numbers to check for primes
    still_is_prime = (n + 1) * [True]  # assume prime until disproven
    for i in range(2, n):
        if still_is_prime[i]:
            # mark multiples of i as not prime
            j = 2 * i
            while j <= n:
                still_is_prime[j] = False
                j += i
    # now every possible prime is a definite prime
    count = sum([1 for v in still_is_prime[2:] if v])
    print("\nQuestion 3: The Sieve of Eratosthenes\n")
    print(count)
    return count
