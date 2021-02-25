# Given a string, check if its characters can be rearranged to form a palindrome.
# Where a palindrome is a string that reads the same left-to-right and right-to-left.


def is_palindrome(word):
    """

    :param word:
    :return: bool
    """
    unmatched = 0
    unique = set(word)
    for i in unique:
        if word.count(i) % 2:
            unmatched += 1
            if unmatched > 1:
                return False
        else:
            continue
    return True
