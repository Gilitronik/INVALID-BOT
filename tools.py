def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True
