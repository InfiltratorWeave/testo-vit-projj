import random

def generate_random_numbers(n, lower, upper):
    return [random.randint(lower, upper) for _ in range(n)]

def main():
    n = int(input("Enter the number of random numbers to generate: "))
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    
    random_numbers = generate_random_numbers(n, lower, upper)
    print("Generated random numbers:", random_numbers)

if __name__ == "__main__":
    main()