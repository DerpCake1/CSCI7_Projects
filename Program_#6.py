f1 = open("score0.txt", 'r')
f2 = open("score1.txt", 'r')
f3 = open("score2.txt", 'r')
f4 = open("score3.txt", 'r')
f5 = open("score4.txt", 'r')
outfile = open("output.txt", 'w')

def file_to_list():
    target_list = []
    for i in target_file:
        target_list.append(i.rstrip("\n"))
    print(target_list)
    return target_list
    
def clear_invalids(file): # check later if values are read as int or str
    non_numerics = []
    invalids = 0
    for value in file:
        try:
            if int(value) > 100:
                invalids += 1
            elif int(value) < 0:
                invalids += 1
            else:
                pass
        except ValueError:
            non_numerics.append(value)
            invalids += 1
    return non_numerics, invalids

def check_scores(target_list):
    a = b = c = d = f = 0
    valids = 0
    global valid_list
    valid_list = []
    
    for value in target_list:
        try:
            value = int(value)
            if 90 <= value <= 100:
                a += 1
                valids += 1
                valid_list.append(value)
            elif 80 <= value < 90:
                b += 1
                valids += 1
                valid_list.append(value)
            elif 70 <= value < 80:
                c += 1
                valids += 1
                valid_list.append(value)
            elif 60 <= value < 70:
                d += 1
                valids += 1
                valid_list.append(value)
            elif 0 <= value < 60:
                f += 1
                valids += 1
                valid_list.append(value)
            else:
                pass
        except ValueError:
            pass
    return a,b,c,d,f,valids

def max_low(valids_list):
    max = 0
    low = 100
    for value in valids_list:
        if int(value) > max:
            max = value
        if int(value) < low:
            low = value
    return max,low

def avg(valids_list):
    try:
        total = 0
        for value in valids_list:
            total += value
        average = total / len(valid_list)
        return average
    except:
        return 0
        
def output(a,b,c,d,f,valids,non_numerics,invalids,max,low,average):
    if len()
    if len(non_numerics) != 0:
        for i in non_numerics:
            outfile.write(i + " is nonumeric, and is ignored. \n")
    outfile.write(str(valids) + " valid score(s) entered. " + str(invalids) + " invalid score(s) entered and ignored. \n")
    if a > 0:
        outfile.write(str(a) + " A\n")
    if b > 0:
        outfile.write(str(b) + " B\n")
    if c > 0:
        outfile.write(str(c) + " C\n")
    if d > 0:
        outfile.write(str(d) + " D\n")
    if f > 0:
        outfile.write(str(f) + " F\n")
    else:
        pass
    if len(valid_list) != 0:
        outfile.write("The high score is " + str(max) + ". The low score is " + str(low) + ". Average score is " + str(format(average, '.2f')))
        
    
def main():
    global target_file
    target_file = f1
    target_list = file_to_list()
    non_numerics, invalids = clear_invalids(target_list)
    a,b,c,d,f,valids = check_scores(target_list)
    max,low = max_low(valid_list)
    average = avg(valid_list)
    output(a,b,c,d,f,valids,non_numerics,invalids,max,low,average)
    
main()
   