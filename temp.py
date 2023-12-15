from TFIDF import*
import os

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

listfilescleaned = os.listdir(path="cleaned")

def TF_question(question,matrice):
    idf_dic=IDF('cleaned')
    for i in matrice.keys():
        matrice[i]=[0,0,0,0,0,0,0,0]
    words=intersection_qst_corpus(question,matrice)
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

def produit_sclalaire(matriceA,matriceB):
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