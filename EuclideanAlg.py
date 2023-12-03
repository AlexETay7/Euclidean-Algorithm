print("\n")
print("The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, a and b.")
print("\n")

# Gather user input
flag = False
while not flag:
    inputOne = input("Enter a non-negative integer for your \"a\" value: ") 
    inputTwo = input("Enter a non-negative integer for your \"b\" value: ")
    variables = [inputOne, inputTwo]
    print("\n")
    
    for var in variables:
            
    # Applying error - handling method
            try:
                # try converting to integer
                int(var)

            except ValueError:
                print("Please enter a valid non-negative integer.")
                inputOne = input("Enter a non-negative integer for your \"a\" value: ") 
                inputTwo = input("Enter a non-negative integer for your \"b\" value: ")
                flag = True
    # flag check
    print("GCD(" + inputOne + ", " + inputTwo + ") = ")
    break
