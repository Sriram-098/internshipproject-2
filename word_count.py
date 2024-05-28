def count_words(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Count the number of words
    num_words = len(words)
    return num_words

# Main functionality
text = input("Enter a text: ")
word_count = count_words(text)
print(f"The number of words in the text is: {word_count}")