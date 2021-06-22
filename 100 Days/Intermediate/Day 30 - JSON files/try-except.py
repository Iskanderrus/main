# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "a")
    file.write("Some message will be printed here")
except KeyError as error_message:
    print(f"There is no key {error_message} in the a_dictionary")
else: # --> if all is ok without any error
    content = file.read()
    print(content)
finally: # code to be run no matter what
    file.close()
    print("File was closed")