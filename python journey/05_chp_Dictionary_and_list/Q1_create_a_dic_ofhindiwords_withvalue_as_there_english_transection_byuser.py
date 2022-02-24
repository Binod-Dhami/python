words={
    'india':"bharat",
    "nepali":"bir gorkhali",
    'masu':"meat"
}
print("options of words are;",words.keys())
a=input("enter the word")
#print('meaning of the word is:',words[a])
#to avoid error
print('meaning of the word is:',words.get(a))
