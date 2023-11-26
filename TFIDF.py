import math
from Basics_function import *

iteration_total={}
IDF={}
TF_IDF={}
list_txt = os.listdir(path="cleaned")

def tf(files):
    txt=open(f"cleaned/{files}", "r",encoding='utf8').readlines()[0]
    i=0
    while i<len(txt):
        mot=''
        if txt[i]==' ':
            i=i+1
        else:
            while txt[i]!=' 'and i<len(txt):
                mot+=txt[i]
                i=i+1
                if i==len(txt):
                    break
            try:
                iteration_total[mot]+=1
            except:
                iteration_total[mot]=1
            idf(mot,txt)

def idf(mot,txt):
    print(len(txt))
    try:
        IDF[mot]
    except:
        for i in range(len(txt)-1):
            if mot in txt:
                try:IDF[mot]+=1
                except:IDF[mot]=1
        
        IDF[mot]=math.log10(len(txt)/(IDF[mot]))
        

def tfidf():
    for i in range(len(list_txt)-1):
        tf(list_txt[i])
    for i in IDF.keys():
        TF_IDF[i]=IDF[i]*iteration_total[i]
    return(TF_IDF)

TFIDF=tfidf()
print(TFIDF)
print('Important word :')
for i,y in TFIDF.items():
    #print(i,end=' ')
    #print(y)
    if y>=1:
        print(i,end=' ')
