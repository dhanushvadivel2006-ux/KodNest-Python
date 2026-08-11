name = input()
course = input()
score = int(input())

# Create the tuple
student_record = name, course, score

# Unpack the tuple
studen_name, student_cource, student_score = student_record

# Display the unpacked values
print("Name:", name)
print("Course:", course)
print("Score:", score)
