import sys
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', " ": "/"}
REVERSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def morse():
    # this is sentence to morse code
    message = input("Give A sentence to translate into morse code: ")
    message1 = " ".join(MORSE_CODE_DICT[i] for i in message.upper())
    # ekta letter nisi then setaa morse_code_dict e khuje ber korsi then add korsi space sooho
    print(message1)


def sentence():
    message1 = input("Give a morse code to translate into sentence: ")
    # this is morse code to sentence
    message2 = "".join(REVERSE_CODE_DICT[i] for i in message1.split(" "))
    # protita morse code er letter space dara alada hoye ache
    # orthat space er aage holo ekta letter
    # message1.split(" ") er maddhome ekta kore morse letter paisi thenseta reverse_Code_dict e khuje ber korsi then add korsi space chara
    print(message2)


while True:
    print('Enter "Morse" to translate sentece to morse code,'
          'Enter "Snt" to translate in to sentence ',
          'Enter "q" to exit program')
    user = input("(morse,snt or q): ")
    if user == "morse":
        morse()
        print("="*51)
    elif user == "snt":
        sentence()
        print("="*51)
    else:
        sys.exit()
