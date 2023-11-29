def count_words(text):
    words = text.split()
    return len(words)

def count_charactors(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_count(item):
    return item[1]

def generate_report(file_contents):
    num_words = count_words(file_contents)
    num_char = count_charactors(file_contents)

    sorted_charactors = sorted(num_char.items(),key=get_count, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} is the Number of the words")

    for char, count in sorted_charactors:
        if char.isalpha():
            print(f"The {char} character was found {count} times")
    print("--- End Report ---")
path_to_file = r'C:\Users\user\workspace\github.com\HamedGraphist\bookbot\books\frankenstein.txt'




with open(path_to_file) as file:
    
    file_contents = file.read()
    


print(file_contents)
generate_report(file_contents)

