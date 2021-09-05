"""
Print all Jumping Numbers smaller than or equal to a given value
A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.

Example:

Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101

Note: Order of output doesn't matter,
i.e. numbers can be printed in any order

"""


def sol(n):
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(10, n + 1):
        z = True
        x = str(j)
        for i in range(len(x) - 1):
            if int(x[i + 1]) - int(x[i]) != 1 and int(x[i + 1]) - int(x[i]) != -1:
                z = False
                break
        if z is True:
            y.append(j)
    return y


if __name__ == "_main_":
    n = int(input("enter range:"))
    print(sol(n))
