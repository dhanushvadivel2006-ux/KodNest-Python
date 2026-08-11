n = int(input())
scores = []

# Read and store all scores
for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())
print("Highest Score:" ,max(scores))
print("Lowest Score:" ,min(scores))
print("Total Score:" ,sum(scores))

# Display the highest, lowest and total scores
# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
