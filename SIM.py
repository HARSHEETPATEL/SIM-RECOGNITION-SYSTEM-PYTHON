# Function to generate Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Input from the user
number = int(input("Enter a number: "))
print("Fibonacci sequence up to", number, ":")
fibonacci(number)
