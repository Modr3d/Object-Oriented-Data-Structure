def odd_list(al):
    temp = []
    for ele in al:
        if ele % 2 != 0:
            temp.append(ele)
    return temp


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
