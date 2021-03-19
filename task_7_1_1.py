import os

f_dict = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dir(f_list):
    for f, f_s in f_list.items():
        if not os.path.exists(f):
            for i in f_s:
                os.makedirs(os.path.join(f, i))


make_dir(f_dict)
