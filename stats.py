def get_book_text():
    f = open("books/frankenstein.txt")
    file_contents = f.read()
    return file_contents

def word_counter():
    text = get_book_text()
    words = text.split()
    count = len(words)
    return count

def character_count():
    character_list = {}
    words = get_book_text().lower()
    word = words.split()
    for a in word:
        b = list(a)
        for c in b:
            if c not in character_list:
                character_list[c] = 1
            else:
                character_list[c] += 1
    return character_list

def main():
    list = character_count()
    return print(list)

main()