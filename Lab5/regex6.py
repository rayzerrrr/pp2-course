import re

def replace(text):

    pattern = r'[ ,.]'

    replaced_text = re.sub(pattern, ':', text)
    return replaced_text


text = input()
replaced_text = replace(text)
print("Original text:", text)
print("Text with spaces, commas, and dots replaced by colon:", replaced_text)
