def get_str_info(text):
    l = len(text)
    n = len(set(text))
    return l, n

def is_noun(word):
    return word[0].isupper()
