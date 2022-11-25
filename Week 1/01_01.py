print("*** Converting hh.mm.ss to seconds ***")
time = input("Enter hh mm ss : ").split()
h = int(time[0])
m = int(time[1])
s = int(time[2])
totalT = h*60*60+m*60+s

if h < 0:
    print("hh" + "(" + str(h) + ")" + " is invalid!")
elif m < 0 or m >= 60:
    print("mm" + "(" + str(m) + ")" + " is invalid!")
elif s < 0 or s >= 60:
    print("ss" + "(" + str(s) + ")" + " is invalid!")
else:
    print("{:02d}".format(h) + ":" + "{:02d}".format(m) + ":" +
          "{:02d}".format(s) + " = " + f"{totalT:,}" + " seconds")
