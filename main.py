### Import the other .py 
from fonctionality import *


present="""Hi I'm your virtual assistant, I've analised serveral speeches of the following president :"""

for i in range(len(president())):
    present+=f"\n - {president()[i]}"       ##display the list of president in the corpus

print(present + '\n\n Choose an action :')


menu="[1] Display the least important word \n[2] Display the word(s) with the highest TD-IDF score\n[3] Indicate the most repeated word(s) by President Chirac\n[4] Indicate the name(s) of the president(s) who spoke of a word (Like Nation ofr example) and the one who repeated it the most times\n[5] Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)\n[6] Excepti the so-called unimportant words, which word(s) did all the president mention?\n[7]Any question\n[8]Menu\n[9]Quit"

print(menu)
while True:
    choice=(input('>>'))  ###the user have to  enter an integer between 1 and 9
    while (not choice.isdigit()) or (not(0<int(choice)<=9)):
        choice=(input('Your choice must be an integer between 1 and 9\n>>'))
        
    choice=int(choice)
        
    if choice==1:
        print(leastimportant(matrix(),format='string'))    ###call the function leastimportant (in fonctionnality.py, line 1) and the matrix fonction (in TFIDF.py) as argument
            
    if choice==2:
        print(highest_tfidf(matrix()))      ###call highest_tfidf (in fonctionnality.py, line 19) 
            
    if choice==3:
        print('The most repeated word is :'+str(mostrepeated()))   ###call mostrepeated (in fonctionnality.py, line 41)


    if choice==4:
        word=input('Choisissez un mot à chercher:\n>>')
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
            print(f'Le(s) president(s) ayant parlé de {word} sont/est {strpres}\nCelui qui en a le plus parlé est {maxvalue}') ###Display it for the user


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
        print('Common word between all presidents :',commun_words_between_presidents())            

    if choice==7:
        question=input('Ask me anything :)\n>>')
        answer=generating_answer(question)
        print(answer)
            
            
    if choice==8:
        print(menu)
            
    if choice==9:
        print('See you !')
        break
    
    print('You can ask me another question ;)')