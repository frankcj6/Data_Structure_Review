#  sieve of eratosthenes algorithm

def count_prime(n):
    if n<= 2:
        return 0
    count = n-2
    prime = [True]*n
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
                for j in range(i*i, n, i):
                    if prime[j]:
                        prime[j] = False
                        count -= 1
    return max(0, count)




n = 10
print(count_prime(10))