import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 15 

start_time = time.time()
result = fibonacci(n)
end_time = time.time()

print(f"{result}\n{end_time - start_time} seconds")
