amount = int(input("Enter amount: "))
print(amount)

denom_dict = {}

denom_dict[2000] = amount // 2000

amount = amount % 2000

denom_dict[500] = amount // 500

amount = amount % 500

denom_dict[200] = amount // 200

amount = amount % 200

denom_dict[2000] = amount // 2000

amount = amount % 2000

denom_dict[100] = amount // 100

amount = amount % 100

denom_dict[50] = amount // 50

amount = amount % 50

denom_dict[20] = amount // 20

amount = amount % 20

denom_dict[10] = amount // 10

amount = amount % 10

print(amount)

denom_dict[5] = amount // 5

amount = amount % 5

denom_dict[2] = amount // 2

amount = amount % 2

denom_dict[1] = amount // 1

amount = amount % 1

print("Denominations are as follows")
print(denom_dict)

