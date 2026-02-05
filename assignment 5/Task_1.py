students = {"alice": 85, "bob": 90}
name = input("Enter the student's name: ").lower().strip()
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")