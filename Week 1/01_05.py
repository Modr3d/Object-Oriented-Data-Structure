num = int(input("Enter Input : "))
count1 = (num*2+4)/2-1
for i in range(int((num*2+4)/2)) :
    count2 = count1
    count1 -= 1
    for j in range(int((num*2+4)/2)) :
        if count2 > 0 :
            print(".", end="")
            count2 -=1
        else :
            print("#", end="")
    for j in range(int((num*2+4)/2)) :
        if (i > 0 and i < ((num*2+4)/2)-1) and (j > 0 and j < ((num*2+4)/2-1)) :
            print("#", end="")
        else :
            print("+", end="")
    print()

count1 = (num*2+4)/2

for i in range(int((num*2+4)/2)) :
    count2 = count1
    count1 -= 1
    for j in range(int((num*2+4)/2)) :
        if (i > 0 and i < ((num*2+4)/2)-1) and (j > 0 and j < ((num*2+4)/2-1)) :
            print("+", end="")
        else :
            print("#", end="")
    for j in range(int((num*2+4)/2)) :
        if count2 > 0 :
            print("+", end="")
            count2 -=1
        else :
            print(".", end="")
    print()