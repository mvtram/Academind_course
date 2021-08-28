# my_name = input('Please enter your name: ')
# print('your Name is', my_name)

# file = open('name.txt', mode='w')
# file.write(my_name)
# file.close()

# file = open('name.txt','r')
# name_file = file.read()
# print(name_file)

age = '29'
age = int(age)+1
bool_val = int(True)
print(bool_val)
print(age)

# improve readability  fans = 1_000_000 is same as  1000000
# 1e6 === 1000000
longer_txt = """ i am a new text
in python, like to write more"""

print(longer_txt)

blockchain = [1, 2, 3, 4, 5]
print(blockchain[:-1])

x = blockchain[1] + 0.5
print(x)
print(blockchain)
blockchain.append(6)
blockchain.pop()
# List is immutable


def greet():
    print("heelllo function")


greet()
