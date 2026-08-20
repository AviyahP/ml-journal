"""This script holds the wordfreq2 function"""

def wordfreq2(file_name):
    """calculate the frequencies of words in file_name and print the 10 most frequent"""
    # open the file and read it
    with open(file_name) as f:
        text = f.read()
    # extract words from the text
    words = text.split()
    stripped_lower_words = [word.lower().strip("[](){}!?_-,.") for word in words]
    cleaned_words = [word for word in stripped_lower_words if word]
    # put word frequencies into a dictionary
    word_frequencies = {}
    for word in cleaned_words:
        word_frequencies[word] = word_frequencies.get(word,0) + 1
    # sort and print the most frequent ones
    sorted_top = sorted(word_frequencies.items(), key = lambda x : x[1], reverse=True)[:10]
    for index in range(0,len(sorted_top)):
        print(f'{index+1}: The word "{sorted_top[index][0]}" appears {sorted_top[index][1]} times in the book.')

wordfreq2("book.txt")

