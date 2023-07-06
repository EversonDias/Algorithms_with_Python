def is_palindrome_recursive(word, low_index, high_index):
    if len(word) > 99:
        raise RecursionError
    if not word:
        return False
    word_reverse = word[::-1]
    if word_reverse != word:
        return False
    return True
