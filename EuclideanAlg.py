
class EuclideanAlg:

    
    # Create a main method that prompts user
    def __init__(self) -> None:
        print("\n")
        print("The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, a and b.")
        print("\n")
        self.get_user_input()
        self.create_spreadsheet()
         

    # Gather user input method
    def get_user_input(self):
        while True:
            try:
                input_one = input("Enter a non-negative integer for your \"a\" value: ")
                input_two = input("Enter a non-negative integer for your \"b\" value: ")
                
                # Check if both inputs are non-negative integers
                if input_one.isdigit() and input_two.isdigit():
                    input_one = int(input_one)
                    input_two = int(input_two)

                    # Check if both inputs are non-negative
                    if input_one >= 0 and input_two >= 0:
                        self.a_value = input_one
                        self.b_value = input_two
                        break
                    else:
                        print("Please enter non-negative integers.")
                else:
                    print("Please enter valid non-negative integers.")
                
            except ValueError:
                print("Please enter valid non-negative integers.")

    # Create diagram of values method
    def create_spreadsheet(self):
        print("--------------------------------------")
        print(f"x: {self.a_value}| y: {self.b_value}|")
        print("     |      |")


euclidean_instance = EuclideanAlg()
