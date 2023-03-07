name = input("Please enter your name:")
labGrade = int(input("Please enter your lab grade:"))
midtermGrade = int(input("Please enter your midterm grade:"))
finalGrade = int(input("Please enter your final grade:"))

lastScore = (labGrade*0.25) + (midtermGrade*0.35) + (finalGrade*0.40)

print("\nName:"+name)
print("Lab:", labGrade)
print("Midterm:", midtermGrade)
print("Final:", finalGrade)
print("Last Score:", lastScore)
