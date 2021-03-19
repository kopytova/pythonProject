import os

search_dir = 'my_project'
num_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if 0 <= os.stat(os.path.join(root, file)).st_size <= 100:
            num_dict.update({100: num_dict.get(100) + 1})
        elif 100 <= os.stat(os.path.join(root, file)).st_size <= 1000:
            num_dict.update({1000: num_dict.get(1000) + 1})
        elif 1000 <= os.stat(os.path.join(root, file)).st_size <= 10000:
            num_dict.update({10000: num_dict.get(10000) + 1})
        else:
            num_dict.update({100000: num_dict.get(100000) + 1})

print(num_dict)

