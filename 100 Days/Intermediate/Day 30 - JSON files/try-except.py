# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:  # just except is too wide - needs to be specified for each error to catch and handle it
    file = open("a_file.txt", "a")
    file.write("Some message will be printed here")
except KeyError as error_message:
    print(f"There is no key {error_message} in the a_dictionary")
else:  # --> if all is ok without any error
    content = file.read()
    print(content)
finally:  # code to be run no matter what
    file.close()
    print("File was closed")
