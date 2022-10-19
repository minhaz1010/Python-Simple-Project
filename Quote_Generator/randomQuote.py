from quote import quote
quoteWord = quote('love', limit=3)
for i in range(len(quoteWord)):
    print(quoteWord[i]['quote'])
    print()
