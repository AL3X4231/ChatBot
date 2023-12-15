from fonctionality import *
from TFIDF import *
from math import sqrt

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
   
    
print(intersection)

def produit_scalaire():
    return [9,5,25,15,49]

def norme(matrix):
    norme_vec=[]
    for i in range(len(matrix[next(iter(matrix))])):
        sum=0
        for j,y in matrix.items():
            sum+=y[i]^2
        norme_vec.append(sum)
    print(norme_vec)
    for i in range(len(norme_vec)):
        norme_vec[i]=sqrt(norme_vec[i])
    return(norme_vec)
        
def similarité():
    matA=matrix()
    matB=TF_question(question,matrix())
    produit_scal=produit_scalaire(matA,matB)
    normeA=norme(matA)
    normeB=norme(matB)
    similarité_mat=[]
    for i in range(len(produit_scal)):
        similarité=(produit_scal[i])/(normeA[i]*normeB[i])
        similarité_mat.append(similarité)
    return(similarité_mat)
        

question='décentralisation relança? avez'
#dic={'gar':[1,2,4,1,8,7,3,4],'noir':[1,4,9,1,8,7,3,4],'nigeria':[1,2,4,9,8,7,3,4]}