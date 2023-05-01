text = input('텍스트를입력하세요(대문자만!): ')

plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "XYZABCDEFGHIJKLMNOPQRSTUVW"

result = ""

for char in text:
    if char in plain:
        index = plain.index(char)
        result += cipher[index]
    else:
        result += char

print(result)
