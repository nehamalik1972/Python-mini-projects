print("Student Data and Results")

total_students = 4
pass_count = 0
fail_count = 0

for i in range(total_students):
    name = input("\nName: ")
    rollno = input("Roll No: ")
    marks = int(input("Marks: "))

    print(name)
    print(rollno)
    print(marks)

    if marks >= 35:
        result = "Pass"
        pass_count += 1
    else:
        result = "Fail"
        fail_count += 1

    print("Result:", result)

print("\nSummary")
print("Total Students:", total_students)
print("Pass:", pass_count)
print("Fail:", fail_count)
