def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    charecter_count = {}

    for char in text.lower():
        if char in charecter_count:
            charecter_count[char] += 1
        else:
            charecter_count[char] = 1

    return charecter_count
def sort_on(item):
    return item["num"]

def refactor_count_characters(dict_of_characters):
    refactored_list = []

    for key, value in dict_of_characters.items():
        refactored_list.append({
            "char": key, 
            "num": value,
            })

    refactored_list.sort(key=sort_on, reverse=True)

    return refactored_list

