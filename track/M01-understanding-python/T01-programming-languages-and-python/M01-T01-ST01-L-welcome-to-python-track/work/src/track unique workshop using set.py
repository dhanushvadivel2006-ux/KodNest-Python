# Read the number of registration entries
n = int(input())

# Create an empty set to store unique student IDs
registrations = set()
all_entries = []

# Read and store the student IDs
for _ in range(n):
    student_id = input().strip()
    all_entries.append(student_id)
    registrations.add(student_id)

# Read the student ID to search
search_id = input().strip()

# Calculate the number of unique registrations
unique_count = len(registrations)

# Calculate the number of duplicate entries
duplicate_count = len(all_entries) - unique_count

# Print the counts
print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

# Check whether search_id exists in registrations
if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")
