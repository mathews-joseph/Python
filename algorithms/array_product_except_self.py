[1,2,3,4]
[1,1,2,6]
[24,12,4,1]
[24,12,8,6]

def array_product(lst):
    n = len(lst)
    prods = [1] * n
    for i in range(1, n):
        prods[i] = lst[i-1] * prods[i-1]

    r = 1
    for i in range(n-1,-1,-1):
        prods[i] *= r
        r *= lst[i]
    print(prods)

array_product([1,2,3,4])
