student = ("Dara", 20, "Computer Science", "Year 3")
print("TASK 1 - STUDENT REGISTRATION")
print("Student name:", student[0])
print("Major:", student[2])
print("Total number of items:", len(student))
print("Student's year (negative indexing):", student[-1])

courses = ("Python", "Database", "Networking", "Python", "Web Development")
print("\nTASK 2 - COURSE ENROLLMENT")
print("Courses:", courses)
print('Number of times "Python" appears:', courses.count("Python"))
print('Index of "Networking":', courses.index("Networking"))
print("Each course:")
for course in courses:
    print(course)

registered_courses = ("Python", "Database", "Networking")
print("\nTASK 3 - UPDATING STUDENT COURSES")
print("Original tuple:", registered_courses)


course_list = list(registered_courses)
course_list.append("Cloud Computing")
registered_courses = tuple(course_list)

print("Updated course registration:", registered_courses)
