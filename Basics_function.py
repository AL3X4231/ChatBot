import os 
listfiles = os.listdir(path="speeches")
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
print(list_president)


for i in len(listfiles):
    file=open(listfiles[i],"r")



