print("*** Reading E-Book ***")
fullText = input("Text , Highlight : ").split(",")
text = fullText[0]
hl = fullText[1]
added = []
for i in text[:]:
    if i == hl:
        added.append("["+i+"]")
    else:
        added.append(i)
for ele in added:
    print(ele, end="")
