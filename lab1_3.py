name = input("Please enter your name:")
labGrade = int(input("Please enter your lab grade:"))
midtermGrade = int(input("Please enter your midterm grade:"))
finalGrade = int(input("Please enter your final grade:"))

lastScore = (labGrade*0.25) + (midtermGrade*0.35) + (finalGrade*0.40)

print("\nName:"+name)
print("Lab:"+str(labGrade))
print("Midterm:"+str(midtermGrade))
print("Final:"+str(finalGrade))
print("Last Score:"+str(lastScore))
