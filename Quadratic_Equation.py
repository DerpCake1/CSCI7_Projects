# Jordan Tran

# 7/16/2023

# This program will take 3 numeral inputs as coefficients to solve a quadratic equation. The program can calculate whether or not
# the inputs can lead to an actual quadratic equation, how many solutions the equation can lead to, and calculate the exact solutions.
# After solving an equation, the program will ask the user whether or not they would like to solve another, if so, the process
# repeats, if not, the program exits.


while True: # will repeat process unless broken
    
    # user inputs / coefficients
    a = float(input("Enter a number for variable a: "))
    b = float(input("Enter a number for variable b: "))
    c = float(input("Enter a number for variable c: "))
    
    # check if a = 0
    if a == 0:
        print("This is a line; not a Quadratic Equation.")
        cont = input("Would you like to solve another Quadratic Equation? Y/N: ")
        if cont == "Y" or cont == "y":
            continue
        elif cont == "N" or cont == "n":
            break
        else:
            print("This is an invalid input.")
            break
        
    # actual formulas
    quad = ((b*b) - 4*(a*c)) # solves for value of discriminant
    uni = -b / (2 * a) # solves for unique solution if discrim = 0
    
    if quad < 0:
        print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has no solution.")
    elif quad == 0:
        print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " has unique solution " + str(uni) + ".")
    else:
        sol1 = ((-(b) + (quad ** 0.5)) / (2 * a))
        sol2 = ((-(b) - (quad ** 0.5)) / (2 * a))
        print(str(int(a)) + "x^2 + " + str(int(b)) + "x + " + str(int(c)) + " has solutions " + str(sol1) + " and " + str(sol2) + ".")
        
    # ask for if they want another input or not
    cont = input("Would you like to solve another Quadratic Equation? Y/N: ")
    if cont == "Y" or cont == "y":
        continue # repeats process
    elif cont == "N" or cont == "n":
        print("Goodbye!") # breaks loop
        break
    else:
        print("This is an invalid input.") # breaks loop if invalid input
        break