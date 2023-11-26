def leastimportant(matrix):
    leastimp=[]
    res='The least important word are : \n'
    for i,y in matrix.items():
        total=0
        for j in y:
            total+=j
        if total==0:
            leastimp.append(i)
            res+=(str(i)+', ')
            
    return(res)

def highest_tfidf(matrix):
    max={'':0}
    for i,y in matrix.items():
        localmax=0
        for j in y:
            if j>localmax:
                localmax=j
        for maxi in max.values():
            if maxi<localmax:
                max={i:localmax}
            if maxi==localmax:
                max[i]=localmax
                break
    maxword=''
    for i,j in max.items():
        maxword+="'"+i+ "' "
        maxvalue=j
    res=f'The word with the highest TF-IDF score is : {maxword}with a TF-IDF={maxvalue}'
    return res

#matrix={'voiture5':[1,2,3,5],'voiture4':[9,8,3,4],'voiture3':[9,2,3,4],'voiture2':[9,2,7,4],'voiture1':[10,0,3,4]}

def mostspoke(word,list_files,idf,matrix):
        spoke=[]
        if idf[word]!=0:
            print('true')
            liste=matrix[word]
            for i in range(len(liste)-1):
                
                if liste[i]!=0:
                    
                    spoke.append(list_files[i])
        return(spoke)


        



        
    

