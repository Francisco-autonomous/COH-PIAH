import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    st = 0
    for traco_a, traco_b in zip(as_a,as_b):
        st = st + abs(traco_a - traco_b)
    
    return st / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    l = lista_sentencas[:]
    lista_frases = []
    for sentenca in range(len(l)):
        l[sentenca] = separa_frases(l[sentenca])
        frasei = l[sentenca]
        for frase in range(len(frasei)):
            lista_frases.append(frasei[frase])
    l = lista_frases[:]
    lista_palavras = []
    for frase in range(len(l)):
        l[frase] = separa_palavras(l[frase])
        pala = l[frase]
        for palavra in range(len(pala)):
            lista_palavras.append(pala[palavra])
    stp = 0
    for palavra in range(len(lista_palavras)):
        stp = stp + len(lista_palavras[palavra])
    wal = stp / len(lista_palavras)
    ttr = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    hlr = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    o = lista_sentencas[:]
    for sentenca in range(len(lista_sentencas)):
        lista_sentencas[sentenca].split()
    sts = 0
    for sentenca in range(len(o)):
        sts = sts + len(o[sentenca])
    sal = sts / len(lista_sentencas)
    sac = len(lista_frases) / len(lista_sentencas)
    p = lista_frases[:]
    for frase in range(len(p)):
        p[frase].split()
    stf = 0
    for frase in range(len(p)):
        stf = stf + len(p[frase])
    pal = stf / len(lista_frases)

    
    return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_de_assinaturas = []
    for texto in range(len(textos)):
        lista_de_assinaturas.append(calcula_assinatura(textos[texto]))
    
    lista_graus = []
    for assinatura in range(len(lista_de_assinaturas)):
        lista_graus.append(compara_assinatura(lista_de_assinaturas[assinatura],ass_cp))
        
    for grau in range(len(lista_graus)):
        if lista_graus[grau] is min(lista_graus):
            return grau + 1
    
ass_cp = le_assinatura()  
textos = le_textos()  
grau = avalia_textos(textos, ass_cp)
print(f'O autor do texto {grau} está infectado com COP-PIAH')
    
