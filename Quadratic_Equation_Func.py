# Jordan Tran

# 7/19/2023

# This program will take 3 numeral inputs as coefficients to solve a quadratic equation. The program uses different functions
# to calculate whether or not the inputs can lead to an actual quadratic equation, how many solutions the equation can lead to, 
# and calculate the exact solutions. After solving an equation, the program will ask the user whether or not they would like to solve another, 
# if so, the process repeats, if not, the program exits. (The same function as program #4, with the same output)

def GetInputs(): # gets user inputs
    InputA = float(input("Enter a number for variable a: "))
    InputB = float(input("Enter a number for variable b: "))
    InputC = float(input("Enter a number for variable c: "))
    return InputA, InputB, InputC

def QuadRoots(a,b,c): # checks the value of the radical and returns a value which will lead to EquationKind
    rad = ((b**2) - (4 * (a*c)))
    if a == 0:
        return -1 # not a quadratic
    elif rad < 0:
        return -2 # no real solution
    else:
        return 0

def Print(a, b, c, root1, root2, EquationKind): # prints based on equationkind, and will provide equation and roots if there are any
    if EquationKind == -1:
        print("This is a line; not a Quadratic Equation.")
    elif EquationKind == -2:
        print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has no solution.")
    else:
        disc = ((b*b) - 4*(a*c))
        if disc == 0:
            print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has unique solution " + str((-b / (2 * a))) + ".")
        else:
            print(str(int(a)) + "x^2 + " + str(int(b)) + "x + " + str(int(c)) + " has solutions " + str(root1) + " and " + str(root2) + ".")

def main():
    while True:
        a, b, c = GetInputs() # return statement to variables
        EquationKind = QuadRoots(a, b, c)
        
        if a == 0:
                Print(a, b, c, 0, 0, EquationKind) # its a line
        else:
            root1 = ((-b + ((b**2) - (4 * (a * c)))) / (2 * a))
            root2 = ((-b - ((b**2) - (4 * (a * c)))) / (2 * a))
            
            Print(a, b, c, root1, root2, EquationKind)
        
        cont = input("Would you like to solve another Quadratic Equation? Y/N: ") # asks if user wants to continue
        if cont == "Y" or cont == "y":
            continue
        else:
            print("Goodbye!")
            break
main()
        