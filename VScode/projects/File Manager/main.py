PLACEHOLDER = "[name]"

with open("./email_names.txt") as file:
    names = file.readlines()

with open("./letter_content.txt") as letters:
    letter_content = letters.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f'./emails/letter_for_{stripped_name}.txt', "w") as completed_emails:
            completed_emails.write(new_letter)