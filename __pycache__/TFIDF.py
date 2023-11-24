txt1='Son nom est célébré par le bocage qui frémit et par le ruisseau qui murmure les vents l emportent jusqu à l arc céleste, l arc de grâce et de consolation que sa main tendit dans les nuages'
txt2='À peine distinguait-on deux buts à l extrémité de la carrière : des chênes ombrageaient l un, autour de l autre des palmiers se dessinaient dans l éclat du soir'
txt3='Ah le beau temps de mes travaux poétiques  les beaux jours que j ai passés près de toi Les premiers inépuisables de joie, de paix et de liberté  les derniers empreints d une mélancolie qui eut bien aussi ses charmes'

iteration={}

def fct(txt):
    IDF=iteration
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
                iteration[mot]+=1
            except:
                iteration[mot]=1
            
            

fct(txt2)
print(iteration)
