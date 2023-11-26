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
            idf_scores[word] = round(math.log10(nb_fichier / count) + 1, 5)
    
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
                tfidf_doc[word] = tf_score * idf_scores[word]
            else:
                tfidf_doc[word] = 0
        
        score_tfidf[doc] = tfidf_doc
    
    return score_tfidf


    
print(TFIDF('cleaned'))  
    
    
    
    #for word,score in (IDF(directory)).items():
        
        
        #score_tfidf[word]=score*(Tf(all_sentences)[word])

    
