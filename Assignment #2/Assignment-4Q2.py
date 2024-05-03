import matplotlib.pyplot as plt
# Task 2: Measure the degree of overlapping subproblems
def fib_count_overlap_once(n):
    count = 0
    f = [0] * (n + 1)
    f[0], f[1] = 1, 1
    f4_calls = [0] * (n + 1)  # List to store the number of times F(4) is called
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count += 1  # Count the number of times F(4) is computed
        if i >= 4:
            f4_calls[i] = f4_calls[i - 1] + f4_calls[i - 2] + 1
    return f4_calls

n_values = list(range(5, 51))
f4_calls = fib_count_overlap_once(n_values[-1])

plt.plot(n_values, f4_calls[5:], marker='o')
plt.title('Number of times F(4) is called for F(5) to F(50)')
plt.xlabel('Value of n')
plt.ylabel('Count of F(4) calls')
plt.grid(True)
plt.show()
