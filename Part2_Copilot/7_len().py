# Write a function text_length(s) that returns how many characters the text has.
# Ask the user for a word and print its length.

# Write your code here:
def text_length(s):
    return len(s)

word = input("Enter a word: ")
print("Length of the word:", text_length(word))