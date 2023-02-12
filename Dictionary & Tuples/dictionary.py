"""
Dictionary is something that allow you to store key-value fairs. also known as Maps, Hashtable or Associate arrays.
A classical example will be a phone directory.
Let's see an example:
"""
dic_phone = {
    "Faisal": 93788743234,
    "Fawad": 93777634020,
    "Fayez": 93984333533,
    "Faizan": 93238378348
}
# To display all items of dictionary
print(dic_phone)
# To display each item separately.
print("Faisal phone number is: ", dic_phone['Faisal'])
print("Fawad phone number is: ", dic_phone['Fawad'])
print("Fayez phone number is: ", dic_phone['Fayez'])
print("Faizan phone number is: ", dic_phone['Faizan'])

# To add a new item to a dictionary:  ==> add(), insert() and append() is not working here.
dic_phone["Mansoor"] = 93238787344

print(dic_phone)

# Displaying all records of dictionary using loop:
for item in dic_phone:
    print(dic_phone[item])

# To display all items with their keys using loop:
for i in dic_phone:
    print(i, ": ", dic_phone[i])

# or
for k, v in dic_phone.items():
    print("Key: ", k, " Value:", v)

# To check,whether someone is present in the dictionary:
print("Fahim" in dic_phone)

# To delete a specific item from dictionary:
del dic_phone["Mansoor"]
print(dic_phone)

# To delete all records from dictionary:
dic_phone.clear()
print("Dictionary is empty!!!", dic_phone)

# These were all about python dictionary.
