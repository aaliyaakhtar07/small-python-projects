#Student Record Manager
student_records = {}
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
    print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["grades"].add(grade)
    print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(is_enrolled("Alice", "Math"))  # Should return True
print(is_enrolled("Alice", "Biology"))  # Should return False
print(is_enrolled("Bob", "Biology"))  # Should return True
print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return False
print(student_records)
