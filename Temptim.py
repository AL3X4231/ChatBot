from fonctionality import *
from TFIDF import *

qst="Miterrand, climat, guerre, poule"

def tokenisation(question):
    question=question.lower()
    for i in range(len(question)):
        print(ord(question[i]))
        print(question[i])
        if ord(question[i])<97 or ord(question[i])>122:
            question=question.replace(question[i],' ')
            print(question)
    separated_words=question.split()
    return(separated_words)

def intersection_qst_corpus(qst,matrix):
    qst=tokenisation(qst)
    intersection=[]
    for i in qst:
        if i in matrix:
            intersection.append(i)
    return(intersection)


matrix_e=matrix()

intersection=intersection_qst_corpus(qst,matrix_e)

dicti={'le':[0,1,0,1,0,2,3,9],'ruban':[0,1,0,1,0,2,3,9],'est':[0,1,0,1,0,2,3,9],'bleu':[0,1,0,1,0,2,3,9]}

def idf_qst(idf_dic):
    for i in words:
        for j in len(matrice[i]):
            matrice[i][j]=idf_dic[i]*matrice[i][j]
    return matrice
            
    
    
print(intersection)
