from Basics_function import *
import time
from Analize import *

present="""Hi I'm your virtual assistant, I've analised serveral speeches of the following president :"""
for i in range(len(president())):
    present+=f"\n - {president()[i]}"

print(present + '\n\n Choose an action :')

menu="[1] Display the most important word \n[2] Display the word(s) with the highest TD-IDF score\n[3] Indicate the most repeated word(s) by President Chirac\n[4] Indicate the name(s) of the president(s) who spoke of the Nation and the one who repeated it the most times\n[5] Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)\n[6] Excepti the so-called unimportant words, which word(s) did all the president mention?\n>>"
#fonction=[fct(),fct2(),fct3(),fct4(),fct5(),fct6()]

while True:
    choice=int(input(menu))
    if isinstance(choice, int) and 0<choice<7:
        if choice==1:
            print(leastimportant(matrix=0))
        if choice==2:
            print(leastimportant(matrix=0))
        if choice==3:
            print(leastimportant(matrix=0))
        if choice==4:
            print(leastimportant(matrix=0))
        if choice==5:
            print(leastimportant(matrix=0))
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



    
        
    
