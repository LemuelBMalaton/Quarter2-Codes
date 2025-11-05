students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
counter = 0
counter2 = 0
allscores = []
while students - 1 >= counter:
    counter2 = 0
    counter += 1
    print("")
    print("Student", counter)
    scores = []
    while subjects - 1 >= counter2:
        counter2 += 1
        score = int(input("Enter score " + str(counter2) + ": "))
        scores.append(score)
    print("Average for Student", counter, "=", sum(scores)/len(scores))
    allscores.append(scores)
allscoresint = [y for x in allscores for y in x]
print("")
print("Class Average =", sum(allscoresint)/len(allscoresint))