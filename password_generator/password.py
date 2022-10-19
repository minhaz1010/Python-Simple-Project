
import random
import math
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '%', '$', '^', '&', '~', '-', '/']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = int(input("How many letter u want in ur passwords: "))
smb = int(input("How many symbol u want in ur passwords: "))
nmb = int(input("How many numbers u want in ur passwords: "))
total = letter+smb+nmb
# letter=math.ceil(letter/2)
passwords = ''
for i in range(letter):
    passwords += capital[random.randint(0, 51)]
for i in range(smb):
    passwords += symbol[random.randint(0, len(symbol)-1)]
for i in range(nmb):
    passwords += number[random.randint(0, len(number)-1)]


list = list(passwords)
random.shuffle(list)
passwords = ''.join(list)
print(f"Your {total} length of secret password is \n{passwords} ")
