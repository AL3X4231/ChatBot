import os 
import re
listfiles = os.listdir(path="speeches")
def president():

    list_president=[]
    for i in listfiles:
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
    return(list_president)


for i in range(len(listfiles)):
    ponctuation=['!','"','#','$','%','&','x²','()','*','+',',','- ','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    file=open('speeches/'+listfiles[i],"r",encoding='utf8')
    lignes=file.readlines()
    texte_minuscule=''
    for j in lignes:
        for k in j:
            if k in ponctuation:
                    texte_minuscule+=''
            elif(k=='-' or k=="'" or k=='\n'):
                texte_minuscule+=' '
            else:
                texte_minuscule+=k.lower()

    f = open(f"cleaned/{listfiles[i]}", "w",encoding='utf8')
    f.write(texte_minuscule)
