from math import sqrt

# Compute the nth Fibonacci number using Binet's formula (Equation 3)
def compute_fib(n):
    sqrt5 = sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return round((phi**n - psi**n) / sqrt5)

# Use Equation (4):
def fibonacci_eq4(p, n):
    phi = (1 + sqrt(5)) / 2
    fp = compute_fib(p)
    return round(fp * phi**(n - p))

# Use Equation (5):
def fibonacci_eq5(n):
    phi = (1 + sqrt(5)) / 2
    fn = compute_fib(n)
    return round(fn * phi)

# Print the first 20 Fibonacci numbers using Equation (4) and Equation (5)
def print_first_20_terms():
    print("First 20 Fibonacci numbers (using Eq 4 and Eq 5):")
    phi = (1 + sqrt(5)) / 2
    eq4_list = []
    eq5_list = []

    for n in range(20):
        if n == 0:
            eq4 = 0
            eq5 = 0
        elif n == 1:
            eq4 = 1
            eq5 = 1
        else:
            eq4 = fibonacci_eq4(n - 1, n)
            eq5 = round(eq5_list[-1] * phi)
        
        eq4_list.append(eq4)
        eq5_list.append(eq5)
        print(f"n = {n:<2} | Eq 4: {eq4:<5} | Eq 5: {eq5}")

    return eq5_list  # Return the list for use in ratio check

# Check how close the ratios F3/F2 and F30/F29 are to the golden ratio
def check_golden_ratio(seq):
    ratio_3_2 = seq[3] / seq[2]
    ratio_30_29 = seq[30] / seq[29]
    print("\nChecking golden ratio approximation:")
    print(f"F3 / F2   ≈ {ratio_3_2}")
    print(f"F30 / F29 ≈ {ratio_30_29}")
    print(f"Expected golden ratio ≈ {(1 + sqrt(5)) / 2}")

def main():
    # Ask the user to enter a valid positive integer for p
    while True:
        try:
            p = int(input("Enter a positive whole number for p: "))
            if p > 0:
                break
            else:
                print("p must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Ask the user to enter n (must be >= p)
    n = int(input("Enter n (greater than or equal to p): "))

    # Compute and display F(n) using Equation (4)
    fn_eq4 = fibonacci_eq4(p, n)
    print(f"\nEstimated F({n}) using Equation (4): {fn_eq4}")

    # Compute and display F(n+1) using Equation (5)
    fn_plus1_eq5 = fibonacci_eq5(n)
    print(f"Estimated F({n+1}) using Equation (5): {fn_plus1_eq5}")

    # Generate and print the first 20 terms from both methods
    seq_eq5 = print_first_20_terms()

    # Extend the list to 31 terms to access F30 and F29
    while len(seq_eq5) <= 30:
        next_val = round(seq_eq5[-1] * ((1 + sqrt(5)) / 2))
        seq_eq5.append(next_val)

    # Check how close F3/F2 and F30/F29 are to the golden ratio
    check_golden_ratio(seq_eq5)

main()

