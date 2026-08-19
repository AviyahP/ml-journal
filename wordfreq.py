# Reading the book in file 'book.txt'
with open("book.txt") as f:
    text = f.read()

# Lowercase and split into words
words = text.lower().split()
# Strip panctuation from each word
words = [w.strip(".,;:!?\"'()") for w in words]
# Count int a dict
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1


# Print the top 10, one per line, with an f-string
top10 = sorted(word_count.items(), key= lambda kv: kv[1], reverse=True)[:10]
for i in range(10):
    print(f'{i+1}: The word "{top10[i][0]}" appears {top10[i][1]} times.')