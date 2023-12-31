import os
import math
from collections import defaultdict

listfilescleaned = os.listdir(path="cleaned")

def Tf(sentence):   #calculate the fre

    words = sentence.split()

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return word_dict


def IDF(directory):   #Calculate the Idf of the corpus
    documents=os.listdir(directory)
    nb_fichier = len(documents)  
    count_doc = defaultdict(int)
    idf_scores = defaultdict(float)

    for doc in documents:
        with open(os.path.join(directory, doc), "r",encoding='utf8') as f:
            content = f.read()
            words = content.split()

        unique_words = set(words)
        for word in unique_words:
            count_doc[word] += 1
    for word, count in count_doc.items():
        if count != 0:
            idf_scores[word] =(math.log10(nb_fichier / (count+1)))
            if idf_scores[word]<0:
                idf_scores[word]=0
    
    return(idf_scores)



def TFIDF(directory): #calculate the tfidf of the corpus
    
    documents = os.listdir(directory)
    score_tfidf={}

    idf_scores = IDF(directory)
    
    for doc in documents:
        with open(f"cleaned/{doc}","r",encoding='utf8') as document:
            sentence=document.read()

        tf_scores = Tf(sentence)
        tfidf_doc={}
        
        for word, tf_score in tf_scores.items():
            if word in idf_scores:
                tfidf_doc[word] = round(tf_score * idf_scores[word],2)
            else:
                tfidf_doc[word] = 0
        
        score_tfidf[doc] = tfidf_doc
    
    return score_tfidf

    
def matrix():    #Create the matrix of tfidf
    score_tfidf = TFIDF('cleaned') 

    matrice = {}

    for value in score_tfidf.values():
        for word in value.keys():
            if word not in matrice:
                matrice[word]=[]
    
    for i in matrice.keys():
        for value in score_tfidf.values():
            if i in value:
                matrice[i].append(value[i])
            else:
                matrice[i].append(0)

    return matrice