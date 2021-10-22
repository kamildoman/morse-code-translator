#The program convert Strings into Morse Code

import json

#Morse Code doesn't recognize Polish special letters, so I convert them into ascii replacements. 
def translator(text):
    polish_letters = "ęóąśłżźćń"
    ascii_replacements = "eoaslzzcn"
    translation_result = str.maketrans(polish_letters, ascii_replacements)
    return text.lower().translate(translation_result)


f = open("morse-code.json", "r", encoding="utf-8")

morse_code_scheme = json.load(f)

text_to_translate = input("Please enter your text: ").lower()
translated_text = ""
not_translated_text = ""

for letter in text_to_translate:
    try:
        translated_text += f"{morse_code_scheme[translator(letter)]} "
    except:
        #if Morse code doesn't recognize a letter it'll write it into "not_translated_text"
        not_translated_text += f"{letter} "

print(f"The morse code for {text_to_translate} is: {translated_text}")
if not_translated_text:
    print(f"I couldn't translate these letters: {not_translated_text}")