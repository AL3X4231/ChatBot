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
        spoke={}
        if word not in idf:
            return(False)
        if idf[word]!=0:
            print('true')
            liste=matrix[word]
            for i in range(len(liste)-1):
                
                if liste[i]!=0:
                    if list_files[i] not in spoke:
                        spoke[list_files[i]]=liste[i]
                    else:
                        spoke[list_files]+=liste[i]
        list_president={}
        for i,y in spoke.items():
            if "Chirac" in i:
                if "Jacques Chirac" not in list_president:
                    list_president["Jacques Chirac"]=y
                else:
                    list_president["Jacques Chirac"]+=y
            elif "Giscard dEstaing" in i:
                if "Valérie Giscard dEstaing" not in list_president:
                    list_president["Valérie Giscard dEstaing"]=y
                else:
                    list_president["Valérie Giscard dEstaing"]+=y
            elif "Hollande" in i:
                if "François Hollande" not in list_president:
                    list_president["François Hollande"]=y
                else:
                    list_president["François Hollande"]+=y
            elif "Macron" in i:
                if "Emmanuel Macron" not in list_president:
                    
                    list_president["Emmanuel Macron"]=y
                else:
                    list_president["Emmanuel Macron"]+=y
            elif "Mitterand" in i:
                if "François Mitterand" not in list_president:
                    list_president["François Mitterand"]=y
                else:
                    list_president["François Mitterand"]+=y
            elif "Sarkozy" in i:
                if "Nicolas Sarkozy" not in list_president:
                    list_president["Nicolas Sarkozy"]=y
                else:
                    list_president["Nicolas Sarkozy"]+=y    
        return(list_president)


def firstone(dico):
    if dico==False:
        return ('no one')
    for dico in dico.keys():
        if 'Macron' in dico:
            first='macron'
        elif 'Hollande' in dico:
            first='Hollande'
        elif 'Sarkozy' in dico:
            first='Sarkory'
        elif 'Mitterand' in dico:
            first='Mitterand'
        elif 'Giscard' in dico:
            first='Giscard'
        else:first='pas trouver'
    return(first)




        
    

