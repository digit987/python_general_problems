place_to_shift = int(input("Enter num of places to shift: "))
salt = list(input("Enter salt: "))

content = ''

with open('encrypt.txt') as f:
    #print(f.read())
    content = f.read()

content = list(content)
print(content)

for i in range(len(content)):
    content[i] = chr(ord(content[i]) + place_to_shift)

print(content)

result = str([chr(ord(i) ^ ord(j)) for i,j in zip(content, salt)])

print(result)

with open('encrypt_enc.txt', 'w') as f:
    f.write(result)

