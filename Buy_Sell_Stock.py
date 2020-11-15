#  Solution for buy and sell stock in leetcode(selling only once)
A1 = [310, 315, 275, 290, 260, 270, 230, 250]
#  Solution 1: Brute Force Buy sell stock
#  Time Complexity: O(n^2)
#  Space Complexity: O(1)


def buy_sell_once_brute_force(A):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


print(buy_sell_once_brute_force(A1))


#  Solution 2: Max, min sell stock
#  Time Complexity: O(n)
#  Space Complexity: O(1)


def max_min_sell_stock(A):
    max_profit = 0
    min_price = A[0]

    for price in A:
        min_price = min(price, min_price)
        max_profit = max(price-min_price, max_profit)

    return max_profit


print(max_min_sell_stock(A1))
