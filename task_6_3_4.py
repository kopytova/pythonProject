from itertools import zip_longest
from json import dump

exit_code = 0
new_users = []
new_hobbies = []
us_h_dict = {}

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        for users_line in users:
            user = users_line.rstrip('\n').replace(',', ' ')
            new_users.append(user)

        for hobby_line in hobbies:
            hobby = hobby_line.rstrip('\n')
            new_hobbies.append(hobby)

for users_hobby in zip_longest(new_users, new_hobbies, fillvalue=None):
    if users_hobby[0] == None:
        exit_code = 1
        break
    us_h_dict.setdefault(users_hobby[0], users_hobby[1])

with open('dict_us_h.json', 'w', encoding='utf-8') as f:
    dump(us_h_dict, f, ensure_ascii=False, indent=4)
