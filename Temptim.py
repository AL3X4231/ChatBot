from fonctionality import *

qst=['Miterrand','climat','guerre','poule']

def intersection_qst_corpus(qst,matrix):
    intersection=[]
    for i in qst:
        if i in matrix:
            intersection.append(i)
    return(intersection)


matrix_e=matrix()

intersection=intersection_qst_corpus(qst,matrix_e)

dicti={'le':[0,1,0,1,0,2,3,9],'ruban':[0,1,0,1,0,2,3,9],'est':[0,1,0,1,0,2,3,9],'bleu':[0,1,0,1,0,2,3,9]}

def idf_qst():
    
    
print(intersection)


