# As input data, you have a string that consists of words that have duplicated characters at the end of it.

import re


def pretty_message(string):
    out = re.sub(r'(.+?)\1+', r'\1', string)
    return ''.join(out)
