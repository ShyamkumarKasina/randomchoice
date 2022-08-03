import re
txt = "Use of python in Machine Learning"
x = re.search("^Use.*Learning$", txt)
if(x):
    print("YES! we have a match")
else:
    print("no match")
