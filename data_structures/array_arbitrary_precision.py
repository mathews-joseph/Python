from functools import reduce

# hack using map or reduce
def arb_precision_hack(lst):
    # a = reduce(lambda x,y: str(x) + str(y), lst)
    a = ''.join(map(str, lst))
    return int(a) + 1

def arb_precision(lst):
    lst[-1] += 1
    for i in reversed(range(len(lst))):
        if lst[i] > 9:
            lst[i] = 0
            if i - 1 >= 0:
                lst[i-1] += 1
            else:
                lst.insert(0,1)


test1 = [1, 4, 9]
test2 = [9, 9, 9]

# print(arb_precision_hack(test1))
arb_precision(test1)
print(test1)

for i in range(7,0,-1):
    print(i)