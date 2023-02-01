# Fibonacci Sequence

def fib(n) -> int:
    """returns the nth_fibonacci number"""
    return _fib(n, {})

def _fib(n, memo) -> int:
    """uses memoization to find and return the nth fib number"""
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = _fib(n -1, memo) + _fib(n-2, memo)
    return memo[n]

print(fib(0)) # 0   
print(fib(1)) # 1   
print(fib(2)) # 1
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(35)) # 9227465
print(fib(46)) # 1836311903


# Tribonacci Number

def tribonacci(n) -> int:
    """Returns the nth tribonacci number"""
    return _tribonacci(n, {})

def _tribonacci(n, memo) -> int | dict:
    """Returns the nth tribonacci number and a dictionary used for memoization"""
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    memo[n] = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
    return memo[n]

print(tribonacci(0)) # 0
print(tribonacci(1)) # 0
print(tribonacci(2)) # 1
print(tribonacci(5)) # 4
print(tribonacci(20)) # 35890
print(tribonacci(37)) # 1132436852

# Sum Possible

def sum_possible(amount, numbers) -> bool:
    """returns boolean result from _sum_possible()"""
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    """returns boolean indicating whether any combo of numbers can sum to amount"""
    if amount in memo:
        return memo[amount]
    if amount < 0:
        return False
    if amount == 0:
        return True
    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True
    memo[amount] = False
    return False

print(sum_possible(15, [6, 2, 10, 19])) # False
print(sum_possible(271, [10, 8, 265, 24])) # False
print(sum_possible(103, [6, 20, 1])) # True


# Min Change

def min_change(amount, coins) -> int:
    """returns -1 if not possible to make change or answer from _min_change()"""
    ans = _min_change(amount, coins, {})
    if ans == float('inf'):
        return -1
    return ans

def _min_change(amount, coins, memo) -> int:
    """returns number of coins needed to make change for amount"""
    if amount in memo:
        return memo[amount]
    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0
    min_coins = float('inf')
    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        if num_coins < min_coins:
            min_coins = num_coins
    memo[amount] = min_coins
    return min_coins

print(min_change(13, [1, 9, 5, 14, 30])) # 5
print(min_change(200, [1, 5, 10, 25])) # 8
print(min_change(271, [10, 8, 265, 24])) # -1
