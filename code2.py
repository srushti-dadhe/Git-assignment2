name = input("Enter student name: ")

marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 75:
    print("Grade: Distinction")
elif average >= 60:
    print("Grade: First Class")
elif average >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")