from Basics_function import *
import time
from Analize import *
from test import *

present="""Hi I'm your virtual assistant, I've analised serveral speeches of the following president :"""
for i in range(len(president())):
    present+=f"\n - {president()[i]}"

print(present + '\n\n Choose an action :')

menu="[1] Display the most important word \n[2] Display the word(s) with the highest TD-IDF score\n[3] Indicate the most repeated word(s) by President Chirac\n[4] Indicate the name(s) of the president(s) who spoke of the Nation and the one who repeated it the most times\n[5] Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)\n[6] Excepti the so-called unimportant words, which word(s) did all the president mention?\n>>"
#fonction=[fct(),fct2(),fct3(),fct4(),fct5(),fct6()]

while True:
    choice=int(input(menu))
    mat=matrix()
    if isinstance(choice, int) and 0<choice<7:
        if choice==1:

            print(leastimportant(matrix(),format='string'))
        if choice==2:

            print(highest_tfidf(matrix()))
        if choice==3:

            print(leastimportant())
        if choice==4:
            word=input('Choisissez un mot a chercher:\n>>')
            listepres=(mostspoke(word,listfiles,IDF('cleaned'),matrix()))
            if listepres==False:
                print('No one speak about it sorry :(')
            else:
                strpres=''
                maxvalue=''
                max=0
                for keys,tfidf in listepres.items():
                    strpres+=keys+', '
                    if tfidf>max: 
                        max=tfidf 
                        maxvalue=keys
                print(f'les presidents ayant parler de {word} sont {strpres}\n Celui qui en a le plus parler est {maxvalue}')
        if choice==5:
            climat=mostspoke('climat',listfiles,IDF('cleaned'),matrix())
            print(climat)
            first=firstone(climat)
            print(f'The first who spoke abput climat is {first}')
            ecology=mostspoke('écologie',listfiles,IDF('cleaned'),matrix())
            print(ecology)
            first=firstone(ecology)
            print(f'The first who spoke abput climat is {first}')
        if choice==6:
            print(leastimportant(matrix=0))
        othqs=input('Do you want to ask another qst ? Type y or n\n>>')
        while othqs!='y' and othqs!='n':
            othqs=input('Retry wrong input \n>>')
        if othqs=='n':
            break
        else:
            pass


while True:    
    kill=input('quit ? Type q\n>>')
    if kill=='q':
        break
    print('Wrong input')



    
        
    
