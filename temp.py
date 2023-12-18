from fonctionality import *
from TFIDF import *
from math import sqrt


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
                return(answer)


question=""""Pourquoi doit on sauver le climat?"""

Starter={
 "Comment": "Après analyse, ",
 "Pourquoi": "Car, ",
 "Peux-tu": "Oui, bien sûr!"
}   

print(generating_answer(question))