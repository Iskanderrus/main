# Open file with the list of invited persons
with open("Input/People/mailing_list.txt") as file:

    # Create a list of the names and clean it adding to a new list
    names = file.readlines()
    stripped_names = []
    for name in names:
        stripped_names.append(name.strip())

    # Going through the list of the cleaned names open the template and replace the placeholder [names] by actual name
    for person in stripped_names:
        with open("Input/Letter_templates/birthday_invitation.txt", "r") as text:
            contents = text.read()
            contents = contents.replace("[name]", person)

        # Create a letter and save it for each person in separate file
        with open(f"Output/ReadyToSend/ invitation_for_{person}.txt", mode="w") as new_letter:
            new_letter.write(contents)
