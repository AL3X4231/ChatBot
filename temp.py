from TFIDF import*
import os

def tokenisation(question):
    question=question.lower()
    for i in range(len(question)):
        if ord(question[i])<97 or ord(question[i])>122:
            question=question.replace(question[i],' ')
    separated_words=question.split()
    return(separated_words)

def intersection_qst_corpus(qst,matrix):
    intersection=[]
    for i in qst:
        if i in matrix:
            intersection.append(i)
    return(intersection)

listfilescleaned = os.listdir(path="cleaned")

def TF_question(question,matrice):
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
                # print(content)
                
                for i in content:
                    if i==word:
                        #print(i)
                        print(word)
                        occ+=1
                TF_per_word[file]=occ
                matrice[word]=TF_per_word
            
    return matrice
TF_question('décentralisation ?',matrix())








def intersection_qst_corpus(qst,matrix):
    intersection=[]
    for i in qst:
        if i in matrix:
            intersection.append(i)
    return(intersection)

matrix_e=matrix()