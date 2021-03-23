import re


def email_parse(email_address):
    RE_EMAIL = re.compile(r'^([A-Za-z0-9_.-]+)@([A-Za-z0-9.-]{1,255})$')
    m = RE_EMAIL.match(email_address)
    if not m: raise ValueError(f'Wrong e-mail {email_address}')
    return {'username': m.group(1), 'domain': m.group(2)}


print(email_parse('tatiana.simko@gmail.com'))
