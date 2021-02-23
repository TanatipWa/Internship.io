numLoop = int(input("Enter number of Country name (integer) : "))

initials = []

for i in range(numLoop):
    tmpInitials = ''
    text = input("Enter Country name " + str(i + 1) + " : ")
    tmpText = text.split(' ')
    for j in tmpText:
        if (j[0].isupper()):
            tmpInitials += j[0]
    initials.append(tmpInitials)

initials.sort(key=lambda item: (-len(item), item))

print("---------------------------")
for i in initials:
    print(i)