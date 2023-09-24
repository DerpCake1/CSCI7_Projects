# Jordan Tran

# 7/29/2023

# This program will take an input file (marked as target file within main(), I have multiple of the test files in global variables)
# with multiple functions that will analyze the input file line by line, checking if the value is numeric or not, if it is within
# 0-100, and if it is within the grade ranges. After analyzing every line within the file, it will display to the output file the non numerical
# values, how many valid and invalid (numeric) values appeared, how many times a certain grade appeared, and finally will display
# the highest valid value, lowest valid value, and the average of the valid values.

f1 = "score0.txt" # the test files
f2 = "score1.txt"
f3 = "score2.txt"
f4 = "score3.txt"
f5 = "score4.txt"
outfile = open("output.txt", 'w') # output file

def check_scores():
    file = open(target_file, 'r') # opens file
    
    a=b=c=d=f = 0 # sets grade counters to 0
    valids = 0 
    invalids = 0
    non_numerics = 0
    
    for i in file:
        try:
            i = int(i)
            if 90 <= i <= 100: # if a value is within a certain grade range, it will count as 1 instance of it and goes down the file line
                a += 1
                valids += 1
            elif 80 <= i < 90:
                b += 1
                valids += 1
            elif 70 <= i < 80:
                c += 1
                valids += 1
            elif 60 <= i < 70:
                d += 1
                valids += 1
            elif 0 <= i < 60:
                f += 1
                valids += 1
            else:
                invalids += 1 # counts instances of numeric invalid values
        except ValueError:
            outfile.write(str(i.rstrip('\n')) + " is non-numeric, and is ignored. \n")
            non_numerics += 1 # counts instances of non numeric values
    file.close()        
    return a,b,c,d,f,valids,invalids, non_numerics

def max_low_average():
    file = open(target_file, 'r') # reopens file
    max = 0
    low = 100 
    value = 0
    total = 0
    for i in file:
        try:
            i = int(i)
            if 100 >= i >= 0: # checks if value is valid
                total += 1
                value += i
                if i > max: # makes current value the max if higher than previous max
                    max = i
                if i < low: # makes current value the min if lower than previous min
                    low = i
        except:
            continue
    try:
        average = value / total # valid value sum / amount of valid values
    except:
        average = 0
    file.close()
    return max, low, average

def main():
    global target_file
    target_file = f5 # set to f5 for testing
    
    a,b,c,d,f,valids,invalids,non_numerics = check_scores() # functions
    max,low,average = max_low_average()
    
    if valids == 0 and invalids == 0 and non_numerics == 0: # if there were no recorded values, mark as no statistics
        outfile.write("No score entered. No statistics")
        
    else:
        outfile.write(str(valids) + " valid score(s) entered. " + str(invalids) + " invalid score(s) entered and ignored. \n") # amount of valids and invalids
        if a > 0:
            outfile.write(str(a) + " A\n") # outputs instances of grades if it isnt 0
        if b > 0:
            outfile.write(str(b) + " B\n")
        if c > 0:
            outfile.write(str(c) + " C\n")
        if d > 0:
            outfile.write(str(d) + " D\n")
        if f > 0:
            outfile.write(str(f) + " F\n")
        if valids != 0:
            outfile.write("The high score is " + str(max) + ". The low score is " + str(low) + ". Average score is " + str(format(average, '.2f'))) # provide high, low, and average if there are valids
        
try:
    main()
except IOError: # checks if input file is even valid
    print('An error occurred trying to read: ' + target_file)