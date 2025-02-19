import re

txt = r"ab*"

pattern = re.compile(txt)

text = "ab a abb abbb aabbaa"
matches = pattern.findall(text)
print(matches)  # ['ab', 'a', 'abb', 'abbb', 'a']
