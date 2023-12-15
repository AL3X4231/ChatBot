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

print(intersection)


