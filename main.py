# Only modify the code between the two comment lines

###################################################################################################

# --- PART 1: THE LOGIC (We test this) ---
def add(a, b):
    # TODO: return the sum of a and b
    pass

def subtract(a, b):
    # TODO: return a minus b
    pass

def multiply(a, b):
    # TODO: return a multiplied by b
    pass

def divide(a, b):
    # TODO: return a divided by b. Finish the condition for dividing by 0
    # Insert the correct condition in the if statement
    if ():
        return None
    pass

####################################################################################################


# DO NOT TOUCH THE CODE BELOW THIS LINE


def run_calculator():
    print("--- Python Calculator ---")
    try:
        # We use a loop so they can keep calculating without restarting
        while True:
            print("\nOptions: [1] Add [2] Subtract [3] Multiply [4] Divide [q] Quit")
            choice = input("Select an option: ")
            
            if choice.lower() == 'q':
                break
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result is None:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {result}")
            else:
                print("Invalid option.")
                
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    run_calculator()