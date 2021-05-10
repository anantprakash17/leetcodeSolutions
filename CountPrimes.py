class Solution:
    def countPrimes(self, n: int) -> int:
        # We will use Sieve of Eratosthenes to calculate number of primes up to n.
        if n < 2:
            return 0
        arr = [True] * n
        primes = 0
        arr[0] = False
        arr[1] = False 
        for i in range(2, n):
            if arr[i]:
                for j in range(i * i, n, i):
                    arr[j] = False    
                primes += 1
        return primes
                    
                        
