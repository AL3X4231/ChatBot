from TFIDF import *
import os 
import re
from math import sqrt

listfiles = os.listdir(path="speeches")

Starter={
 "Comment": "Après analyse, ",
 "Pourquoi": "Car, ",
 "Peux-tu": "Oui, bien sûr!"
}


def president():

    list_president=[]
    for i in listfiles:
        if "Chirac" in i:
            if "Jacques Chirac" not in list_president:
                list_president.append("Jacques Chirac")
        elif "Giscard dEstaing" in i:
            if "Valérie Giscard dEstaing" not in list_president:
                list_president.append("Valérie Giscard dEstaing")
        elif "Hollande" in i:
            if "François Hollande" not in list_president:
                list_president.append("François Hollande")
        elif "Macron" in i:
            if "Emmanuel Macron" not in list_president:
                list_president.append("Emmanuel Macron")
        elif "Mitterand" in i:
            if "François Mitterand" not in list_president:
                list_president.append("François Mitterand")
        elif "Sarkozy" in i:
            if "Nicolas Sarkozy" not in list_president:
                list_president.append("Nicolas Sarkozy")
    return(list_president)


for i in range(len(listfiles)):
    ponctuation=['!','"','#','$','%','&','x²','()','*','+',',','- ','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    contractions = {"de":"d'","le":"l'","qui":"qu'","à le": "au", "à les": "aux", "de le": "du", "de les": "des", "je ai": "j'ai", "que il": "qu'il", "que elle": "qu'elle", "qui il": "qu'il", "qui elle": "qu'elle", "ne est": "n'est", "ce est": "c'est", "ce ont": "ont"}
    accents_mapping = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ý': 'y', 'ÿ': 'y', 'ç': 'c', 'ñ': 'n'}

    file=open('speeches/'+listfiles[i],"r",encoding='utf8')
    lignes=file.readlines()
    texte_minuscule=''
    for j in lignes:
        for key, value in contractions.items():
                if value in j:
                    j = j.replace(value, key+' ')
        for letter_with_accent, letter_without_accent in accents_mapping.items():
            if letter_with_accent in j:
                j = j.replace(letter_with_accent, letter_without_accent)

        for k in j:
            if k in ponctuation:
                    texte_minuscule+=''
            elif(k=='-' or k=="'" or k=='\n'):
                texte_minuscule+=' '
            else:
                texte_minuscule+=k.lower()
        

    f = open(f"cleaned/{listfiles[i]}", "w",encoding='utf8')
    f.write(texte_minuscule)
    f.close()


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
        res=res[:-2]
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



def commun_words_between_presidents():
        listefilescleaned=os.listdir('cleaned')
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
        leastimportante=leastimportant(matrix(),'list')
        for i in leastimportante:
            if i in commun_words:
                commun_words.remove(i)
        return(commun_words)


#part 2

def tokenisation(question):
    question=question.lower()
    for i in range(len(question)):
        if (ord(question[i])<97 or ord(question[i])>122) and ord(question[i])<128:
            question=question.replace(question[i],' ')
    separated_words=question.split()
    return(separated_words)

def intersection_qst_corpus(qst,matrix):
    qst=tokenisation(qst)
    intersection=[]
    for i in qst:
        if i in matrix:
            intersection.append(i)
    return(intersection)


def TFIDF_question(question,matrice):
    idf_dic=IDF('cleaned')
    for i in matrice.keys():
        matrice[i]=[0,0,0,0,0,0,0,0]
    words=intersection_qst_corpus(question,matrice)
    if len(words)==0:
        return (words)
    for word in words:
        TF_per_word=[0,0,0,0,0,0,0,0]
        for file in range(len(listfilescleaned)):
            with open('cleaned/'+listfilescleaned[file],'r',encoding='utf-8') as doc:
                occ=0
                content=doc.read()
                content=content.split()

                for i in content:
                    if i==word:
                        occ+=1
                TF_per_word[file]=occ
                matrice[word]=TF_per_word
    for i in words:
        for j in range(len(matrice[i])):
            matrice[i][j]=round(idf_dic[i]*matrice[i][j],2)
    return matrice

def produit_scalaire(matriceA,matriceB):
    matrice_inter={}
    liste_result=[]
    for key in matriceA.keys():
        matrice_inter[key]=[0]*8
        for value in range(8):
            matrice_inter[key][value]=matriceA[key][value]*matriceB[key][value]
    for i in range(8):
        sum=0
        for j in matrice_inter.keys():
            sum+=matrice_inter[j][i]
        liste_result.append(sum)
    return liste_result


def norme(matrix):
    norme_vec=[]
    for i in range(len(matrix[next(iter(matrix))])):
        sum=0
        for values in matrix.values():
            sum+=values[i]**2
        norme_vec.append(sum)
    for i in range(len(norme_vec)):
        norme_vec[i]=sqrt(norme_vec[i])
    return(norme_vec)


def similarity(matA,mat_question,listfichier):
    produit_scal=produit_scalaire(matA,mat_question)
    normeA=norme(matA)
    normeB=norme(mat_question)
    similar_mat=[]
    
    for i in range(len(produit_scal)):
        similar=0
        if normeB[i]!=0:
            similar=(produit_scal[i])/(normeA[i]*normeB[i])
        similar_mat.append(similar)
        
    maxi=0
    for i in range(len(similar_mat)):
        if similar_mat[i]>maxi:
            maxi=similar_mat[i]
            maxi_index=i
    
    doc_similaire=listfichier[maxi_index]
    return(doc_similaire)

def generating_answer(question):
    TFIDF_of_question=TFIDF_question(question,matrix())
    if len(TFIDF_of_question)==0:
        answer='Je suis désolé, le corpus ne fait pas mention cela'
        return answer
    word_high_idf=''
    highest_TFIDF_score=0
    for word,Tfidf in TFIDF_of_question.items():
        for j in range(8):
            if Tfidf[j]>highest_TFIDF_score:
                word_high_idf=word
                highest_TFIDF_score=Tfidf[j]
    listfiles=os.listdir('speeches')
    relevant_document=similarity(matrix(),TFIDF_of_question,listfiles)
    with open('speeches/'+relevant_document,'r',encoding='utf-8') as document:
        sentences=document.read()
        sentences=sentences.split('.')
        for answer in sentences:
            if word_high_idf in answer:
                
                answer=answer+'.'
                answer=answer.replace('\n','')
                for starters in Starter.keys():
                    if starters in question:
                        answer=Starter[starters]+answer
                    else:
                        answer=answer.capitalize()
                if answer is None:
                    answer='Je suis désolé, le corpus ne fait pas mention cela'
                return(answer)



