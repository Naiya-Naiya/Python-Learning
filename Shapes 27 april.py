length = 10
for pos in range(1,length+1):
    print("n"*pos)

#-Shapes with python
length = 10
TP = "a"

#ascending order triangle
for pos in range(1,length+1):
    print(TP*pos)

#decsending order triangle
for pos in range(length,0,-1):
    print(TP*pos)

#one less character triangle
for pos in range(length-1,0,-1):
    print(TP*pos)