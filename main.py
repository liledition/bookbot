from stats import word_counter, sotr_by_count, get_path, get_book_text

def main():
    num_words = word_counter()
    list = sotr_by_count()
    return print(f"""============ BOOKBOT ============
Analyzing book found at {get_path()}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{list}
============= END ===============""")

main()
