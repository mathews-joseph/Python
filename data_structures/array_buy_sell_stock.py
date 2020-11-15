# time complexity: O(n**2)
# space complexity: O(1)
def buy_sell_stock_brute(lst):
    max_profit = 0
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            max_profit = max(max_profit, lst[j] - lst[i])
    return max_profit

# time complexity: O(n)
# space complexity: O(1)
def buy_sell_stock(lst):
    smallest = lst[0]
    max_profit = 0
    for stock in lst:
        smallest = min(smallest, stock)
        max_profit = max(max_profit, stock - smallest)

    return max_profit

a1 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# print(buy_sell_stock_brute(a1))
print(buy_sell_stock(a1))