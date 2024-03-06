replace_letter = "[name]"
with open("./Input/Letters/starting_letter.txt",mode="r") as Letters:
    letter = Letters.read()
    with open("./Input/Names/invited_names.txt", mode="r") as Names:
        names = Names.readlines()
        for name in names:
            stripped_name = name.strip()
            new_letter = (letter.replace(replace_letter, stripped_name))
            with open(f"./Output/ReadyToSend/Letter_to_{stripped_name}.txt",mode="w") as letter_final:
                letter_final.write(new_letter)




