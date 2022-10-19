from random_word import RandomWords
from quote import quote
randomWord=RandomWords().get_random_word()
randomQuote=quote(randomWord,limit=1)
for i in range(len(randomQuote)):
    print(randomQuote[i]['quote'])
    print()