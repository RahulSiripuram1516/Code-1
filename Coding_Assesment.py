"""There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbours.
What is the minimum candies you must give?
Input Format:
The first and the only argument contains N integers in an array A.
Output Format:
Return an integer, representing the minimum candies to be given.
Example:
Input 1:
 A = [1, 2]
Output 1:
 3
"""
def min_candies(A):
    n = len(A)
    candies = [1] * n

    # Pass 1: Go from left to right to assign candies to children with higher ratings
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Pass 2: Go from right to left to assign candies to children with higher ratings
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Return the total number of candies
    return sum(candies)


"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the
stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.
Problem Constraints
0 <= len(A) <= 7e5
1 <= A[i] <= 1e7
Input Format
The first and the only argument is an array of integers, A.
Output Format
Return an integer, representing the maximum possible profit.
Example Input
Input 1:
 A = [1, 2]
Input 2:
 A = [1, 4, 5, 2, 4]
Example Output
Output 1:
 1
Output 2:
 4
"""

def max_profit(prices):
    max_profit = float('-inf')
    for i in range(1, len(prices)):
        potential_profit = prices[i] - prices[i-1]
        max_profit = max(max_profit, potential_profit)
    return max_profit

"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
Example :
Input 1:
A = 2 Output 1:
2 Explanation 1:
[1, 1], [2] Input 2:
A = 3 Output 2:
3 Explanation 2:
[1 1 1], [1 2], [2 1]
"""

def staircase(A):
    dp = [0] * (A + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, A + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[A]



def max_profit(prices, k):
    n = len(prices)
    if k > n // 2:
        return max_profit(prices, n // 2)

    dp = [[float('-inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], prices[i] - prices[i - 1])

    for j in range(1, k + 1):
        for i in range(j, n):
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1] + prices[i] - prices[i - 1])

    return dp[k][n - 1]

"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbours.
What is the minimum candies you must give?
Input Format:
The first and the only argument contains N integers in an array A.
Output Format:
Return an integer, representing the minimum candies to be given.
Example:
Input 1:
 A = [1, 2]
Output 1:
 3

"""

def get_row(k):
    row = [1] * (k + 1)

    for i in range(k):
        row[k - i - 1] = row[k - i - 1] * (i + 1) // (i + 2)

    return row
"""
There are certain problems which are asked in the interview to also check how you take care of overflows
in your problem.
This is one of those problems.
Please take extra care to make sure that you are type-casting your ints to long properly and at all places.
Try to verify if your solution works if number of elements is as large as 105
Food for thought :
• Even though it might not be required in this problem, in some cases, you might be required to order the
operations cleverly so that the numbers do not overflow.
For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate
factorial(n), factorial(k) and then divide them.
Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
Obviously approach 1 is more susceptible to overflows.
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra
memory?
Note that in your output A should precede B.
Example:
Input:[3 1 2 5 3]
Output:[3, 4]
A = 3, B = 4
"""
p = 0
while xor1 > 0:
    xor1 = xor1 & (xor1 - 1)
    p += 1

xor1 = 0
xor2 = 0
for i in range(n):
    if arr[i] & (1 << p):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (arr[i] & (1 << p))
    else:
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (arr[i] & ~(1 << p))


