import random
import string
import re
punctuation = set(string.punctuation)


def shuffle_words_with_punctuation(text):
    """
    Shuffle the characters inside words of the given text while keeping 
    the starting and ending punctuation intact.

    Args:
    text (str): The text to be processed, where each word will be modified 
                by shuffling its inner characters.

    Returns:
    str: The text with shuffled words, where the starting and ending 
         punctuation of each word is preserved.

    During processing:
    - Each word is checked for leading and trailing punctuation.
    - Words shorter than 3 characters remain unchanged.
    - Words longer than 3 characters have their internal characters shuffled randomly.
    - Empty words (resulting from consecutive spaces) are removed.

    Example:
    >>> shuffle_words_with_punctuation("Hello, world! This is a test.")
    "Hleol, wdorl! Tihs is a tset."

    """

    if not isinstance(text, str):
        raise ValueError("Argument musi być typu str.")

    words_and_spaces = re.split(r'(\s+)', text)
    shuffled_list = []

    start_char = ''
    end_char = ''

    for word in words_and_spaces:
        if word.isspace():
            shuffled_list.append(word)
            continue

        if len(word) > 0 and word[0] in punctuation:
            start_char = word[0]
            word = word[1:]

        if len(word) > 0 and word[-1] in punctuation:
            end_char = word[-1]
            word = word[:-1]

        if len(word) > 3:
            list_of_char = list(word)
            sublist = list_of_char[1:-1]
            cp_sublist = sublist.copy()

            while sublist == cp_sublist:  # <-  condition eliminates shuffling to the same place
                random.shuffle(sublist)   # <-  A custom mixing method can be created.

            list_of_char[1:-1] = sublist
            shuffle_word = ''.join(list_of_char)
            shuffle_word = f"{start_char}{shuffle_word}{end_char}"
            start_char = ''
            end_char = ''

        else:
            shuffle_word = word
            shuffle_word = f"{start_char}{shuffle_word}{end_char}"
            start_char = ''
            end_char = ''

        shuffled_list.append(shuffle_word)

    return ''.join(shuffled_list)
