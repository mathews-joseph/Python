# 0 1 1 2 3 5 8 13

def fib_tuples(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b

def fib_dp_top_down(n, results):
    if n in results:
        return results[n]
    if n == 1:
        val = 1
    elif n == 2:
        val = 1
    else:
        val = fib_dp_top_down(n-1, results) + fib_dp_top_down(n-2, results)
    results[n] = val
    return results[n]



def fib_dp_bottom_up(n):
    results = [0] * int(n+1)
    results[0] = 0
    results[1] = 1
    for i in range(2,n+1):
        results[i] = results[i-1] + results[i-2]
    return results[n]

# O(2**n)
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# print(fib_rec(6))
# print(fib_dp_bottom_up(6))
# print(fib_tuples(5))
print(fib_dp_top_down(5,{}))