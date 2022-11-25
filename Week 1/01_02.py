wh = input("Enter your High and Weight : ").split()
weight = float(wh[1])
height = float(wh[0])
bmi = weight/pow(height, 2)

if bmi < 18.5:
    print("Less Weight")
elif 18.5 <= bmi < 23:
    print("Normal Weight")
elif 23 <= bmi < 25:
    print("More than Normal Weight")
elif 25 <= bmi < 30:
    print("Getting Fat")
else:
    print("Fat")
