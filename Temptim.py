from fonctionality import *
from TFIDF import *
from math import sqrt

qst="Miterrand, climat, guerre, poule"

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
        for j,y in matrix.items():
            
            sum+=y[i]**2
        norme_vec.append(sum)
    for i in range(len(norme_vec)):
        norme_vec[i]=sqrt(norme_vec[i])
    return(norme_vec)
        
def similarité():
    matA=matrix()
    matB=TF_question(question,matrix())
    produit_scal=produit_scalaire(matA,matB)
    normeA=norme(matA)
    normeB=norme(matB)
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
    
    listfichier=os.listdir('speeches')
    doc_similaire=listfichier[maxi_index]
    return(doc_similaire)
        

question="""'Le monde entier a regardé notre élection présidentielle.
Partout, on se demandait si les Français allaient décider à leur tour de se replier sur le passé illusoire, s'ils allaient rompre avec la marche du monde, quitter la scène de l'Histoire, céder à la défiance démocratique, l'esprit de division et tourner le dos aux Lumières, ou si au contraire ils allaient embrasser l'avenir, se donner collectivement un nouvel élan, réaffirmer leur foi dans les valeurs qui ont fait d'eux un grand peuple.
Le 7 mai, les Français ont choisi.
Qu'ils en soient ici remerciés.
La responsabilité qu'ils m'ont confiée est un honneur, dont je mesure la gravité.
Le monde et l'Europe ont aujourd'hui, plus que jamais, besoin de la France.
Ils ont besoin d'une France forte et sûre de son destin.
Ils ont besoin d'une France qui porte haut la voix de la liberté et de la solidarité.
Ils ont besoin d'une France qui sache inventer l'avenir.
Le monde a besoin de ce que les Françaises et les Français lui ont toujours enseigné : l'audace de la liberté, l'exigence de l'égalité, la volonté de la fraternité.
Or, depuis des décennies, la France doute d'elle-même.
Elle se sent menacée dans sa culture, dans son modèle social, dans ses croyances profondes.
Elle doute de ce qui l'a faite."""
similar=(similarité())

print(similar)
    
