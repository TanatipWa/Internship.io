textQuestion = input("Enter question of Digit Hangman (integet 12 digits) : ")

listQuestion = []
listAnswer = []
listShow = []

for i in range(12):
    listShow.append("_")

listQuestion = textQuestion.split(' ')

for i in range(5):
    intAnswer = input("Round " + str(i + 1) +
                      " enter answer (integet 0 - 9) : ")
    listAnswer.append(intAnswer)

print("---------------------------")
for i in listQuestion:
    print(i, end=" ")
print()

point = 0
for i in range(5):
    tmpPoint = point
    for j in range(12):
        if (listAnswer[i] == listQuestion[j]):
            listShow[j] = listAnswer[i]
            point += 1
    if (tmpPoint == point):
        listShow.append(listAnswer[i])
    for k in listShow:
        print(k, end=" ")
    print()
print(point)