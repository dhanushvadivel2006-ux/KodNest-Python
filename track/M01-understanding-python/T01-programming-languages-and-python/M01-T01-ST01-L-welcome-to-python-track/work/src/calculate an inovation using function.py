# Read how many numbers will be entered
number_count = int(input())

# Initialize the counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

# Read and analyze each number
for i in range(number_count):
    value = int(input())

    if value > 0:
        positive_count += 1
    elif value < 0:
        negative_count += 1
    else:
        zero_count += 1

    total = total + value

# Display the final analysis
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)
