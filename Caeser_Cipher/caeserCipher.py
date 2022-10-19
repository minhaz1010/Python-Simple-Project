import sys


def encode(sentence, shift):
    s = ''.join(' ' if i == ' ' else chr(ord(i) + shift) for i in sentence)
    print(s)


def decode(sentence, shift):
    s = ''.join(' ' if i == ' ' else chr(ord(i) - shift) for i in sentence)
    print(s)


while True:
    print("What do you want ?")
    user = input("Encode,Decode,Quit: ").lower()
    if user == "encode":
        sentence = input("What do u want to encode: ")
        shift = int(input("Type the shift number:"))
        encode(sentence, shift)
    elif user == "decode":
        sentence = input("What do u want to decode: ")
        shift = int(input("Type the shift number: "))
        decode(sentence, shift)
    elif user == 'quit':
        sys.exit()
