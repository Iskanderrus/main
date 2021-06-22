# # FileNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:  # just except is too wide - needs to be specified for each error to catch and handle it
#     file = open("a_file.txt", "a")
#     file.write("Some message will be printed here")
# except KeyError as error_message:
#     print(f"There is no key {error_message} in the a_dictionary")
# else:  # --> if all is ok without any error
#     content = file.read()
#     print(content)
# finally:  # code to be run no matter what
#     raise TypeError("This message is here to have a message")
#
#

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Your height is not human.")

bmi = weight / height ** 2
print(bmi)
