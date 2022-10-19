def quiz():
  pass


questions={"Who wrote the famous book - 'We the people'?":'A',
"Who is the author of the book 'Nineteen Eighty Four'?":'B',
"Who is the author of the book 'Forbidden Verses'?":'D'
}

answers=[
  {
    'A':'Nani Palkhivala',
    'B':'TN Kaul',
    'C':'Hudai',
    'D':'kushwant'

  },
  {
    'A':'THOMAS HARDY',
    'B':'GEORGE ORWELL',
    'C':'WALTER SCOTT',
    'D':'EMILE ZOLA'
  },
   {
    'A':'SALMAN RUSHDEI',
    'B':'ABBU NUWAS',
    'C':'TOSLIMA NASRIN',
    'D':'D.H LAWRENCE'
   }
]

#print(answers[0].keys())
#print(answers[1])
#...
#for i in range(len(answers)):
 # for k in answers[i].items():
  #  print(k[0],k[1])
#
listofAnswer = []
k=-1
for keys,values in questions.items():
  print('='*51)
  print(keys)
  k+=1
  for i,j in answers[k].items():
    print(i,j)
  print("#"*11)  
  x=input("what is ur answers: ")
  x=x.capitalize()
  listofAnswer.append(x)

m=0
correct=0
for i,j in questions.items():
  if listofAnswer[m]==j:
    correct+=1
    m+=1
  else:
    m+=1 
print("-"*40)
print(f"Your total right answer is  {correct}")  
    
  