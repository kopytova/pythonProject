from collections import Counter

list_result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.readline()
    while content:
        el_content = content.split(' ')
        ip = el_content[0]
        method = el_content[5].strip('"')
        uri = el_content[6]
        list_result.append((ip, method, uri))
        content = f.readline()

inquiry = dict(Counter(list_result).most_common())

print(list_result)

print(inquiry)
