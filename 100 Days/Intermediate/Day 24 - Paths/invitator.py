with open("Input/People/mailing_list.txt") as file:
    names = file.readlines()
    stripped_names = []
    for name in names:
        stripped_names.append(name.strip())
    for person in stripped_names:
        with open("Input/Letter_templates/birthday_invitation.txt", "r") as text:
            contents = text.read()
            contents = contents.replace("[name]", person)

        with open(f"Output/ReadyToSend/ invitation_for_{person}.txt", mode="w") as new_letter:
            new_letter.write(contents)
