import re

RE_LOG = re.compile(r'^([0-9.]+) - - \[([^\]]+)\] "([A-Z]+) ([^ ]+) [^"]+" (\d{3}) (\d+)')


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(re.findall(RE_LOG, line))
