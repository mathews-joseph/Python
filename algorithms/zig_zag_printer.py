test_string = "mathewsjoseph"
no_of_rows = 3
"""
m   e   o   h
a h w j s p
t   s   e
"""

def zig_zag_printer(string, n):
    rows = [''] * n
    i = 0
    step = 1
    for char in string:
        rows[i] += char
        i += step
        if i == 0 or i == n-1:
            step *= -1
    for row in rows:
        print(row)

zig_zag_printer(test_string, no_of_rows)