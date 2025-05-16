import sys
from stats import count_words, character_frequency, order_map

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    file_contents = ""
    with open(filepath, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def report_stats(filepath, wordcount, order_map):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words ")
    print("--------- Character Count -------")
    for item in order_map:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def main(filepath):
    content = get_book_text(filepath)
    num_words = count_words(content)
    character_count = character_frequency(content)
    sorted_character_count = order_map(character_count)
    report_stats(filepath, num_words, sorted_character_count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])