def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

choice = int(input("Enter a number: "))
print(f"Factorial of {choice} is: ", factorial(choice))