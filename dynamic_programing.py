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
