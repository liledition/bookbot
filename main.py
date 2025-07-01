from stats import word_counter

def get_book_text():
    f = open("books/frankenstein.txt")
    file_contents = f.read()
    return file_contents

"""
def main():
    file_contents = get_book_text()
    print(file_contents)
    return file_contents
"""

def main():
    num_words = word_counter()
    return print(f"{num_words} words found in the document")

main()