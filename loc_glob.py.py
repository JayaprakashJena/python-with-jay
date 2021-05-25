#global & local variable

# a=1000
# print(a)
# def show() :
#     print('i am cr7')
#     a=99  #local variable
#     print(a)

# print(a)
# show()
# print(a)

# #output expected : 1000  1000  i am cr7  99 1000

# a = 1000
# print(a)
# def show():
#     print(a)
#     global a 
#     a=99
#     print(a)

# print(a)
# show()
# print(a)

# # output expexted : 1000 1000 error

# a = 1000
# print(a)
# def show():
#     global b
#     b=111
#     print(b)
#     print(a+b)
#     c=50
#     print(a+b+c)


# show()
# print(a)
# print(b)
# print(c)

#expected output : 1000  111  1111  1161  1000  111 error

# a = 1000
# print(a)
# def show():

#     b=111
#     print(b)
#     print(a+b)
#     c=50
#     print(a+b+c)


# show()
# print(a)
# print(b)
# print(c)

#expected op : 1000  111  1111  1161 1000 error

# list_1 = (1,45,67,8,9)
# list_1(0)=3

# myDict = {
#     "fast": "In a Quick Manner",
#     "harry": "A Coder",
#     "marks": [1, 2, 5],
#     "anotherdict": {'harry': 'Player'},
#     1: 2
# }

# Dictionary Methods
# print(list(myDict.keys())) # Prints the keys of the dictionary
# print(myDict.values()) # Prints the keys of the dictionary 
# print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
# print(myDict)
# updateDict = {
#     "Lovish": "Friend",
#     "Divya": "Friend",
#     "Shubham": "Friend",
#     "harry": "A Dancer"
# }
# myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
# print(myDict)

# print(myDict.get("harry")) # Prints value associated with key "harry"
# print(myDict["harry"]) # Prints value associated with key "harry"

# # The difference between .get and [] sytax in Dictionaries?
# print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
# print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
print("The meaning of your word is:", myDict[a])
# print("The meaning of your word is:", myDict.get(a))