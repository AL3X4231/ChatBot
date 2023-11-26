import os
import math
from collections import defaultdict


def Tf(sentence):

    words = sentence.split()

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return word_dict



def IDF(directory):
    documents=os.listdir(directory)
    nb_fichier = len(documents)  # Correction ici, utiliser 'docs' au lieu de 'fichier'

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



def TFIDF(directory):
    
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
                tfidf_doc[word] = round(tf_score * idf_scores[word],5)
            else:
                tfidf_doc[word] = 0
        
        score_tfidf[doc] = tfidf_doc
    
    return score_tfidf

    
def matrix():
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

def fonctionnalité3():
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


def mots_communs_presidents():
    mots_presidents = {}
    repertoire='cleaned'
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(repertoire, fichier)

            with open(chemin_fichier, "r", encoding="utf8") as document:
                contenu = document.read()

            mots = set(contenu.split())

            if not mots_presidents:
                mots_presidents = mots
            else:
                mots_presidents = mots_presidents.intersection(mots)
    
    return mots_presidents

