def leastimportant(matrix):
    leastimp=[]
    res='The least important word are : \n'
    for i,y in matrix.items():
        total=0
        for j in y:
            total+=j
        if total==0:
            leastimp.append(i)
            res+=('- '+str(i)+'\n')
            
    return(res)

def highest_tfidf():
    print('bite')

