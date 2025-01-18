def sum_total(a, b):
    return a + b

if __name__ == "__main__":
    print("This program will ask for two numbers and give you the sum of those two numbers.")
    print("Please key in a number: ")
    a = float(input())
    print("Please key in the second number: ")
    b = float(input())
    c = sum_total(a, b)
    print("The sum of those two numbers is {:.2f}.".format(c))

