# Read how many numbers will be entered
try:
    number_count = int(input("How many numbers will you enter? "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Initialize counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

# Read and analyze each number
for i in range(number_count):
    try:
        value = int(input(f"Enter number {i+1}: "))
    except ValueError:
        print("Invalid input, please enter an integer.")
        continue  # Skip this iteration if input is invalid

    if value > 0:
        positive_count += 1
    elif value < 0:
        negative_count += 1
    else:
        zero_count += 1

    total += value

# Display the final analysis
print("\n--- Final Analysis ---")
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)

# Extra insights
if number_count > 0:
    print("Average:", total / number_count)
    print("Positive %:", (positive_count / number_count) * 100)
    print("Negative %:", (negative_count / number_count) * 100)
    print("Zero %:", (zero_count / number_count) * 100)
