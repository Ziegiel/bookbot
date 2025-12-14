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