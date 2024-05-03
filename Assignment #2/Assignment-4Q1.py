import time
import matplotlib.pyplot as plt

# 自頂向下計算 Fibonacci 數列
def fibonacci_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]

# 自底向上計算 Fibonacci 數列
def fibonacci_bottom_up(n):
    if n <= 2:
        return 1
    bottom_up = [0] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]

# 測量執行時間
def measure_execution_time(func, max_n):
    execution_times = []
    for n in range(1, max_n + 1):
        start_time = time.time()
        func(n)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times

max_n = 100
top_down_times = measure_execution_time(fibonacci_top_down, max_n)
bottom_up_times = measure_execution_time(fibonacci_bottom_up, max_n)


# 繪製折線圖
plt.plot(range(1, max_n + 1), top_down_times, label='Top-Down')
plt.plot(range(1, max_n + 1), bottom_up_times, label='Bottom-Up')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time of Fibonacci Calculation')
plt.legend()
plt.show()
