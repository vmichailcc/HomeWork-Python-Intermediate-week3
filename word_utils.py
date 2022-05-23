import re


def clean_sign(text):
    clean_line = re.sub(r'[^\w\s]', "", text)
    return clean_line


def get_list(text):
    words = text.split()
    return words


def get_long_word(text):
    long_word = max(text.split(), key=len)
    return long_word
