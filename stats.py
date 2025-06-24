def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return ""

def word_counter(filepath):
    book_text = get_book_text(filepath)
    book_as_list = book_text.split()
    return len(book_as_list)

def char_counter(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    def sort_on(item):
        return item["num"]
    
    char_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
