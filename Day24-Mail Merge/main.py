PLACEHOLDER = "NAME"

# Puts names from file in a list
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Gets the letter template
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # First strip the newlines on each name
        stripped_name = name.strip()
        # Replace the placeholder with each name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Create a new letter text file for each person
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)











