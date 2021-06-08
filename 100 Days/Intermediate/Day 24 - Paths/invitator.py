with open("People/mailing_list.txt") as file:
    names = file.readlines()
    new_names = []
    for name in range(0, 7):
        new_names.append(names[name][:-1])
    new_names.append(names[-1])
    for person in new_names:
        with open("Letter_templates/birthday_invitation.txt", "r") as text:
            contents = text.read()
            contents = contents.replace("[name]", person)

        new_letter = open(f"Output/ReadyToSend/ invitation_for_{person}.txt", mode="w")
        new_letter.write(contents)
        new_letter.close()
