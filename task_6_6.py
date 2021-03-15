from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as data_recording:
    data_recording.write(argv[1] + '\n')
