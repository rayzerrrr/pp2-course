import re
#1

pattern1 = re.compile(r"ab*")

#2
pattern2 = re.compile(r"ab{2,3}")

#3
pattern3 = re.compile(r"[a-z]+\_")

#4
pattern4 = re.compile(r"[A-Z]{1}[a-z]+")

#5
pattern5 = re.compile(r"a.+b\Z")

#6
pattern6 = re.compile(r"[ ,.]")


#7
def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase



#8
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res


#10
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

#11
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res


def main():
    print("Task 1")
    print(pattern1.search("fdskfldkflddsdsab"))

    print("Task 2")
    print(pattern2.search("gjdfkabbbbfkkliu"))

    print("Task 3")
    print(pattern3.findall("fdsfd_ fdjskfjdsk_ fdsf4ds_"))

    print("Task 4")
    print(pattern4.findall("Ffdsf GGfgrhr ImknkJtr"))

    print("Task 5")
    print(pattern5.search("kktngtag423b"))
    print(pattern5.search("fjdjgfdb"))
    print(pattern5.search("fdifafgnjgr3"))

    print("Task 6")
    text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
    print(pattern6.sub(":", text))

    print("Task 7")

    print(snakeToCamel("hello_world_wordle"))

    print("Task 8")
    print(modify("OneTwoThree"))
    
    print("Task 9")
    print(spaces("HelloWordlOneMoreTime"))

    print("Task 10")
    print(camel_to_snake("SnakeCaseVar"))


