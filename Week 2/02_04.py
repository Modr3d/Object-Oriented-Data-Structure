def hbd(years):
    i = 2
    age = int(years)
    while True:
        if (age%i == 0) and (int(age/i)%i) == 2 and ((int(int(int(age/i)/i)/i)) <= 9 and int(int(age/i)/i)%i <= 1) :
            check = 1
            break
        elif (age%i == 1) and (int(age/i)%i == 2) and ((int(int(int(age/i)/i)/i)) <= 9 and int(int(age/i)/i)%i <= 1):
            check = 2
            break
        else :
            i += 1
    if check == 1 :
        return "saimai is just 20, in base " + str(i) +"!"
    elif check == 2 :
        return "saimai is just 21, in base " + str(i) +"!"""

year = input("Enter year : ")
print(hbd(year))