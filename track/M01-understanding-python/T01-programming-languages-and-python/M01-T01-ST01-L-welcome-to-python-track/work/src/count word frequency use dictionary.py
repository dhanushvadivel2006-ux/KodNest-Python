# Read the number of words
n = int(input())

# Dictionary to store each word and its frequency
word_frequency = {}

# Read and count the words
for _ in range(n):
    word = input().strip()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Print each unique word and its frequency in order of first appearance
for word, count in word_frequency.items():
    print(word, count)
