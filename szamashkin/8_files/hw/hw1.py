words = []

file_name = input("Please enter the file name: ")
if len(file_name) < 1:
    file_name = 'unixdict.txt'

with open(file_name, 'r') as file:
    for line in file:
        words.append(line.rstrip())

for word in words:
    if word[::-1] in words:
        print(word, word[::-1])