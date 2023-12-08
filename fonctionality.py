from TFIDF import *

def leastimportant(matrix,format):
    leastimp=[]
    res='The least important word are : \n'
    for i,y in matrix.items():
        total=0
        for j in y:
            total+=j
        if total==0:
            leastimp.append(i)
            res+=(str(i)+', ')

    if format=='string':
        return(res)
    else:
        return(leastimp)

def highest_tfidf(matrix):
    max={'':0}
    for i,y in matrix.items():
        localmax=0
        for j in y:
            if j>localmax:
                localmax=j
        for maxi in max.values():
            if maxi<localmax:
                max={i:localmax}
            if maxi==localmax:
                max[i]=localmax
                break
    maxword=''
    for i,j in max.items():
        maxword+="'"+i+ "' "
        maxvalue=j
    res=f'The word with the highest TF-IDF score is : {maxword}with a TF-IDF={maxvalue}'
    return res


def mostrepeated():
    with open("cleaned/Nomination_Chirac1.txt","r",encoding='utf8') as document1:
        sentence1=document1.read()
    with open("cleaned/Nomination_Chirac2.txt","r",encoding='utf8') as document2:
        sentence2=document2.read()
    sentence=Tf(sentence1+sentence2)
    max=0
    word=[]
    for i,j in sentence.items():
        if j>max:
            max=j
            word=[i]
        elif j==max:
            word.append(i)
    return word


def mostspoke(word,list_files):
        idf=IDF('cleaned')
        matrice=matrix()
        spoke={}
        if word not in idf:
            return(False)
        if idf[word]!=0:
            liste=matrice[word]
            for i in range(len(liste)-1):
                
                if liste[i]!=0:
                    if list_files[i] not in spoke:
                        spoke[list_files[i]]=liste[i]
                    else:
                        spoke[list_files]+=liste[i]
        list_president={}
        for i,y in spoke.items():
            if "Chirac" in i:
                if "Jacques Chirac" not in list_president:
                    list_president["Jacques Chirac"]=y
                else:
                    list_president["Jacques Chirac"]+=y
            elif "Giscard dEstaing" in i:
                if "Valérie Giscard dEstaing" not in list_president:
                    list_president["Valérie Giscard dEstaing"]=y
                else:
                    list_president["Valérie Giscard dEstaing"]+=y
            elif "Hollande" in i:
                if "François Hollande" not in list_president:
                    list_president["François Hollande"]=y
                else:
                    list_president["François Hollande"]+=y
            elif "Macron" in i:
                if "Emmanuel Macron" not in list_president:
                    
                    list_president["Emmanuel Macron"]=y
                else:
                    list_president["Emmanuel Macron"]+=y
            elif "Mitterand" in i:
                if "François Mitterand" not in list_president:
                    list_president["François Mitterand"]=y
                else:
                    list_president["François Mitterand"]+=y
            elif "Sarkozy" in i:
                if "Nicolas Sarkozy" not in list_president:
                    list_president["Nicolas Sarkozy"]=y
                else:
                    list_president["Nicolas Sarkozy"]+=y    
        return(list_president)


def firstone(dico):
    if dico==False:
        first=False
    else:
        for dico in dico.keys():
            if 'Macron' in dico:
                first='macron'
            elif 'Hollande' in dico:
                first='Hollande'
            elif 'Sarkozy' in dico:
                first='Sarkory'
            elif 'Mitterand' in dico:
                first='Mitterand'
            elif 'Giscard' in dico:
                first='Giscard'
        return(first)



import os

def mots_communs_presidents(repertoire):
    mots_presidents = {}

    # Parcourir les fichiers dans le répertoire
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(repertoire, fichier)

            with open(chemin_fichier, "r", encoding="utf8") as document:
                contenu = document.read()

            # Tokeniser les mots
            mots = set(contenu.split())

            # Mettre à jour les mots communs pour chaque président
            if not mots_presidents:
                mots_presidents = mots
            else:
                mots_presidents = mots_presidents.intersection(mots)

    return mots_presidents

# Appel de la fonction avec le répertoire contenant les documents de chaque président
repertoire_presidents = "cleaned"
resultat = mots_communs_presidents(repertoire_presidents)

# Affichage des résultats
print("Les mots évoqués par tous les présidents sont :", resultat)

   
    # leastimportant_list = leastimportant(matrix(),'list')
    # for i in mots_presidents:
    #     if i in leastimportant_list:
    #         mots_presidents.remove(i)
    # return mots_presidents

def mot_commun(listefilescleaned):
        with open(f'cleaned/{listefilescleaned[0]}',"r",encoding='utf8') as document1:
            sentence0=document1.read()
        with open(f'cleaned/{listefilescleaned[1]}',"r",encoding='utf8') as document2:
            sentence1=document2.read()
        sentence=sentence0+sentence1
        
        with open(f'cleaned/{listefilescleaned[5]}',"r",encoding='utf8') as document1:
            sentence1=document1.read()
        with open(f'cleaned/{listefilescleaned[6]}',"r",encoding='utf8') as document2:
            sentence2=document2.read()
        sentence1=sentence1+sentence2
        
        
        with open(f'cleaned/{listefilescleaned[2]}',"r",encoding='utf8') as document1:
            sentence2=document1.read()
            
        with open(f'cleaned/{listefilescleaned[3]}',"r",encoding='utf8') as document1:
            sentence3=document1.read()
        with open(f'cleaned/{listefilescleaned[4]}',"r",encoding='utf8') as document1:
            sentence4=document1.read()
        with open(f'cleaned/{listefilescleaned[7]}',"r",encoding='utf8') as document1:
            sentence5=document1.read()
        
        
        exemple=Tf(sentence5)
        all_sentence=[sentence,sentence1,sentence2,sentence3,sentence4]
        
        commun_words=[]
        for i in exemple.keys():
            occurence=0
            for j in all_sentence:
                if i in Tf(j):
                    occurence+=1
            if occurence==5:
                commun_words.append(i)
        return(commun_words)
                    
            
            
            
            
print(mot_commun(listfilescleaned))