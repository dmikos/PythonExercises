

"""
https://projecteuler.net/problem=4
http://euler.jakumo.org/problems/view/4.html
"""
def is_palindrome(num):
    x = str(num)
    return x == x[::-1]


def palindrome_factors(digits):
    max_num = (10 ** digits) -1
    min_num = max_num // 10

    best = (0, 0, 0)
    for i in range(max_num, min_num, -1):
        for j in range(i, min_num, -1):
            multi = i * j
            # if multi > best[0] and is_palindrome(multi):
            if multi <= best[0]:
                break
            if is_palindrome(multi):
                best = (multi, i, j)
    return best


print(palindrome_factors(5))