import math

zahl = 1585

roem_buch = [
    ("I", "V", "X"),
    ("X", "L", "C"),
    ("C", "D", "M"),
    ("M", "None", "None")
]

print(zahl)

output = ""
for i in range(len(str(zahl))):
    ziffer = zahl % 10
    if ziffer == 4:
        output = roem_buch[i][0] + roem_buch[i][1] + output
    elif ziffer == 9:
        output = roem_buch[i][0] + roem_buch[i][2] + output
    else:
        output = (ziffer//5)*roem_buch[i][1] + (ziffer%5)*roem_buch[i][0] + output
    zahl = zahl//10


print(output)
