# Read a text file
# Remove unwanted characters
# Split into words
# Count word occurrences
# Get the 10 most common words
# Print the total number of words
# Print the number of unique words, not counting stop words
# Print the number of stop words
# Create bar chart with matplotlib


import matplotlib.pyplot as plt

def get_words_from_file(filename):
    # Read text file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove unwanted characters
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.replace('!', ' ')
    text = text.replace('?', ' ')
    text = text.replace('"', ' ')
    text = text.replace(";", ' ')
    text = text.replace("--", ' ')

    # Split into words
    return text.split()

# Stop words, far from all there are
stop_words = {
    "a", "an", "and", "as", "be", "had", "have", "he", "his", "him", "i", "in", "is", "it", "it's",
    "of", "that", "the", "them", "they", "to", "was", "with", "you"
}

occurance = {}

words = get_words_from_file("dickens_carol.txt")

# Get count of unique words, not counting stop words
stopped_words = 0
for word in words:
    word = word.lower()
    if word in stop_words:
        stopped_words += 1
        continue
    if word in occurance:
        occurance[word] += 1
    else:
        occurance[word] = 1

# Make a list of words and occurances
word_list = []
for word, count in occurance.items():
    word_list.append((count, word))

# List the 10 most common words
word_list.sort(reverse=True)
for item in word_list[0:10]:
    print(f"{item[1]}: {item[0]}")


print(f"Total number of words: {len(words)}")
print(f"Number of unique words, not counting some stop words: {len(occurance)}")
print(f"Number of words in stop word list: {stopped_words}")


# Create bar chart with matplotlib
top_10 = word_list[:10]
top_words = [word for count, word in top_10]
top_counts = [count for count, word in top_10]


plt.figure(figsize=(10, 6))
bars = plt.bar(top_words, top_counts, color="#4C72B0")

plt.title("Top 10 Most Common Words (excluding some stop words)")
plt.xlabel("Words")
plt.ylabel("Occurrences")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

# Add value labels above bars
for bar, value in zip(bars, top_counts):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        str(value),
        ha="center",
        va="bottom"
    )

# Save and show the plot
plt.savefig("top10_words.png", dpi=150)
plt.show()