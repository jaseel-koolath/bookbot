def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    result = {}
    for char in text:
        lowerchar = char.lower()
        if lowerchar in result:
            result[lowerchar] += 1
        else:
            result[lowerchar] = 1
    return result

def sort_char_dict(char_dict):
    def sort_by(item):
        return item["num"]
    chars = []
    for char in char_dict:
        chars.append({
            "char": char,
            "num": char_dict[char]
        })
    chars.sort(reverse=True, key=sort_by)
    return chars
