numGrades = input("Enter numerical value for number of grades to process: ")
studentName = input("Please enter your name: ")
loopCount = 0
sumGrades = 0
while loopCount < int(numGrades):
    assignmentGrade = input("Enter numerical value of your grade: ")
    sumGrades = sumGrades + int(assignmentGrade)
    loopCount = loopCount + 1
studentAverage = sumGrades / int(numGrades)
print(studentName, "has an average of", studentAverage)