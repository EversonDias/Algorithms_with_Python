def is_palindrome_iterative(word):
    if not word:
        return False
    word_reverse = word[::-1]
    if word_reverse != word:
        return False
    return True
