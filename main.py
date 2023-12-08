### Import the other .py 
from Basics_function import *
from fonctionality import *


present="""Hi I'm your virtual assistant, I've analised serveral speeches of the following president :"""

for i in range(len(president())):
    present+=f"\n - {president()[i]}"       ##display the list of president in the corpus

print(present + '\n\n Choose an action :')


menu="[1] Display the most important word \n[2] Display the word(s) with the highest TD-IDF score\n[3] Indicate the most repeated word(s) by President Chirac\n[4] Indicate the name(s) of the president(s) who spoke of a word (Like Nation ofr example) and the one who repeated it the most times\n[5] Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)\n[6] Excepti the so-called unimportant words, which word(s) did all the president mention?\n>>"


while True:
    choice=int(input(menu))     ###the user have to  enter an integer between 1 and 7
    if isinstance(choice, int) and 0<choice<7:
        if choice==1:

            print(leastimportant(matrix(),format='string'))    ###call the function leastimportant (in fonctionnality.py, line 1) and the matrix fonction (in TFIDF.py) as argument
        if choice==2:

            print(highest_tfidf(matrix()))      ###call highest_tfidf (in fonctionnality.py, line 19) 
        if choice==3:
            print('The most repeated word is :', end=' ')
            print(mostrepeated())    ###call mostrepeated (in fonctionnality.py, line 41)


        if choice==4:

            word=input('Choisissez un mot a chercher:\n>>')
            listepres=(mostspoke(word,listfiles))   ###call mostspoke (in fonctionnality.py, line 58) take in parameter the IDF dict of the corpus a chosen word be the user the matrice and the list of files and return a dict
            if listepres==False:
                print('No one speak about it sorry :(')   
            else:
                strpres=''
                maxvalue=''
                max=0
                for keys,tfidf in listepres.items():  
                    strpres+=keys+', '  ###link all president in one string
                    if tfidf>max: ###find the max value and link it with his president
                        max=tfidf 
                        maxvalue=keys
                print(f'les presidents ayant parler de {word} sont {strpres}\n Celui qui en a le plus parler est {maxvalue}') ###Display it for the user



        if choice==5:

            climat=mostspoke('climat',listfiles)   ### mostspoke again
            first=firstone(climat)
            print(f'The first who spoke about climat is {first}')

            ecology=mostspoke('écologie',listfiles)
            first=firstone(ecology)
            if ecology==False:
                res='No one speak about ecology'
            else:
                res=f'The first who spoke about ecology is {first}'
            print(res)


        if choice==6:
            print('Common word between all presidents :')
            mot_commun(listfiles)

        othqs=input('Do you want to ask another qst ? Type y or n\n>>')  ###Ask the user if he want to ask another qst
        while othqs!='y' and othqs!='n':         
            othqs=input('Retry wrong input \n>>')     ###If the user don't enter y or n it will ask to retry
        if othqs=='n':
            break
        else:
            pass


while True:    
    kill=input('quit ? Type q\n>>')   ###close the program
    if kill=='q':
        break
    print('Wrong input')