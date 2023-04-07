#json1 = input("Enter 1st JSON")
#json2 = input("Enter 2nd JSON")
json1 = {"x": 10.1,
"y": 20,
"name": "Anu",
"dob": "2010-10-10"
}
json2 = {
"x": 10,
"y": 20,
"name": "Ani",
"z":100,
"dob": "2010-10-11"
}

json3 = {}

json1_keys = list(json1.keys())
json2_keys = list(json2.keys())

def dob_diff(dob1, dob2):
    dob1 = dob1.split('-')
    dob2 = dob2.split('-')
    return [int(dob1[0])-int(dob2[0]), int(dob1[1])-int(dob2[1]), int(dob1[2])-int(dob2[2])]

for key in json2_keys:
    if key not in json1_keys:
        json3[key] = "Only in 2"

for key in json1_keys:
    if key in json2_keys and json1[key] != json2[key]:
        if type(json1[key]) != type(json2[key]):
            json3[key] = "Different Types"
        if isinstance(json1[key], int) or isinstance(json1[key], float) and isinstance(json2[key], int) or isinstance(json2[key], float):
            json3[key] = abs(round((json1[key] - json2[key]), 1))
        if isinstance(json1[key], str) and isinstance(json2[key], str):
            json3[key] = "Text Change"
        if key == 'dob':
            json3[key] = dob_diff(json1[key], json2[key])
    if key not in json2_keys:
        json3[key] = "Only in 1"
            
print(json3)
