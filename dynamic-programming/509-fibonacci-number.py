def fib(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 4:
        return n-1
    
    
    sum = [2, 3]

    for _ in range(4, n):
        temp = sum[1]
        sum[1] = sum[1] + sum[0]
        sum[0] = temp

    return sum[1]

print(fib(11))