# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.
# 1.json:
# [{"name": "user_1”, "password": "pass_1”}, {"name": "user_2”, "password": ["pass_1", "qwerty“]}]
# find("1.json", "password") returns ["pass_1", "qwerty"]
#
# 2.json:
# [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}},
# {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
#
# 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
# find("3.json", "password") returns ["1234qweQWE"]

import json


def find(file, key):
    with open(file) as f:
        d = json.load(f)
        key_words = []
        for el in d:
            if el == 'name':
                key_words.append(d.get(key))
                break
            elif key in el.keys():
                key_words.append(el[key])
            continue

        result = []
        for i in key_words:
            if i in result:
                break
            elif type(i) is list:
                result.extend(i)
            else:
                result.append(i)

        return list(set(result))
