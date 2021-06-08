with open("/home/alex/Рабочий стол/my_file.txt") as text:
    contents = text.read()
    print(contents)

path = "/home/alex/Рабочий стол/"
file = "my_file.txt"
with open(path + file) as text:
    contents = text.read()
    print(contents)
