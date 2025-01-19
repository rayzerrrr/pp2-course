#strings can be combined 

x = "string"
y = ' is combined'

z = x + y

print(z)

#but string can be combined only with strings , to combine strings with other data types we use F-strings with this syntax

a = 231
txt = f"string combined with int {a}"
print(txt)