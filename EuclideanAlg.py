
class EuclideanAlg:

    print("\n")
    print("The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, a and b.")
    print("\n")

    # Create a prompt user method
    def __init__(self) -> None:
         self.get_user_input()
         

    # Gather user input
    def get_user_input(self):
        flag = False
        while not flag:
            inputOne = input("Enter a non-negative integer for your \"a\" value: ") 
            inputTwo = input("Enter a non-negative integer for your \"b\" value: ")
            variables = [inputOne, inputTwo]
            print("\n")
            
            for var in variables:
                    
            # Applying error - handling method, there are issues here 
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
    
euclidean_instance = EuclideanAlg()
