file1 = open('arrivee.move','r')
file2 = open('result.move','w')

text = file1.readlines()

for line in text:
    if "head" not in line and "bust" not in line and "abs" not in line:
        file2.write(line)
