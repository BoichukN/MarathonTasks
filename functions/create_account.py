# Create function create_account(user_name: string, password: string, secret_words: list).
# This function should return inner function check.
# The function check compares the values of its arguments with password and secret_words:
# the password must match completely, secret_words may be misspelled (just one element).
# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,
# special character and one number.
# Otherwise function create_account raises ValueError.
# For example:
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# then
# tom("Qwerty1_",  ["1", "word"]) return True
# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
# tom("Qwerty1_",  ["word", "12"]) return True

import re


def create_account(user_name: str, password: str, secret_words: list):
    if not re.search(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#_~&\/,.:;№!$%*<>?]).{6,}', password):
        raise ValueError

    def check(password_check, secret_check: list):
        count = 0
        if password_check != password or len(secret_check) != len(secret_words):
            return False
        for i in range(len(secret_words)):
            if secret_words[i] in secret_check:
                secret_check.remove(secret_words[i])
                count += 1
        return len(secret_words) - count <= 1
    return check
