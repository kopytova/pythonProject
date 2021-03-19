import os


pn = 'my_project'
if not os.path.exists(pn):
    for s in ('settings', 'mainapp', 'adminapp', 'authapp'):
        os.makedirs(os.path.join(pn, s))

