def leastimportant(matrix,format):
    leastimp=[]
    res='The least important word are : \n'
    for i,y in matrix.items():
        total=0
        for j in y:
            total+=j
        if total==0:
            leastimp.append(i)
            res+=(str(i)+', ')
    if format=='string':
        return(res)
    else:
        return(leastimp)

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
        list_president=[]
        for i in spoke:
            if "Chirac" in i:
                if "Jacques Chirac" not in list_president:
                    list_president.append("Jacques Chirac")
            elif "Giscard dEstaing" in i:
                if "Valérie Giscard dEstaing" not in list_president:
                    list_president.append("Valérie Giscard dEstaing")
            elif "Hollande" in i:
                if "François Hollande" not in list_president:
                    list_president.append("François Hollande")
            elif "Macron" in i:
                if "Emmanuel Macron" not in list_president:
                    list_president.append("Emmanuel Macron")
            elif "Mitterand" in i:
                if "François Mitterand" not in list_president:
                    list_president.append("François Mitterand")
            elif "Sarkozy" in i:
                if "Nicolas Sarkozy" not in list_president:
                    list_president.append("Nicolas Sarkozy")
            
        return(spoke)


        



        
    

