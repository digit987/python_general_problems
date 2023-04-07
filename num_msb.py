num = list(input("Enter a number"))
num[0] = 1
num[1] = 1
print("Number in decimal is: ", num)

num = int(''.join([str(i) for i in num]))
print(num)
bin_num = []

while num != 0:
    bin_num.append(num%2)
    num = num // 2
bin_num.reverse()

print("Number in decimal is": bin_num)

