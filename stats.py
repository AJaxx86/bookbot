def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    chars = {}

    for c in content:
        if c.isalpha() == False:
            continue

        if c.lower() in chars:
            chars[c.lower()] += 1
        else:
            chars[c.lower()] = 1
    
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    char_list = []
    
    for c in char_dict:
        char_list.append({"char": c, "num": char_dict[c]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list