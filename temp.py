def tokenisation1(question):
    question=question.lower()
    for i in range(len(question)):
        print(ord(question[i]))
        print(question[i])
        if ord(question[i])<97 or ord(question[i])>122:
            question=question.replace(question[i],' ')
            print(question)
    separated_words=question.split()
    return(separated_words)

def TF_question():
    TF_question={}
    matrice=matrix()
    for i in matrice.keys():
        if matrice in separated_words:
            
