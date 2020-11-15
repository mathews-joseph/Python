def int_2_str(n):
    """
    You are given some integer as input
    (i.e -321, 123,...). Convert the integer
    you are given to a string. Do not make
    use of the built-in "str" function.

    Examples:
        Input: 123
        Output: "123"
        Input: -123
        Output: "-123"

    Parameters:
        n: int

    Returns:
        str
    """
    res = ''
    is_neg = False
    if n < 0:
        is_neg = True
        n *= -1
    while n > 0:
        digit = n % 10
        n //= 10
        res = chr(ord('0')+digit) + res
    if is_neg:
        res = '-' + res
    return res

print(int_2_str(-123))
print(int_2_str(123))