import sys

def get_path():
    arguments = sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        return path

def get_book_text():
    f = open(get_path())
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

def sotr_by_count():
    list = character_count()
    result = sorted(list.items(), reverse=True, key=lambda x: x[1])
    dict = '\n'.join(f"{char}: {num}" for char, num in result[0:])
    return dict
