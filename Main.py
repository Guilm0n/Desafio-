from Anuncio import Anuncio

lista=[]

while True:
    print('Operação(A)=Adiconar Anuncio' + '\nOperação(V)=Ver a lista de anuncios'
          + '\nOperação(F)=Filtrar por:Operação(C)=Cliente ou Operação(D)=Data')
    operacao=input('Digite operacao')

    if operacao=="S":
        break
    elif operacao == "A":

        nome=input('Digite o nome do anuncio-->')
        cliente=input('Digite o cliente')
        inicio=input('Digite a data de inicio em formato D/M/A-->')
        termino=input('Digite a data de termino em formato D/M/A-->')
        investimento=float(input('Valor do investimento diario-->R$'))
        lista.append( Anuncio(nome,cliente,inicio,termino,investimento))

    elif operacao=="V":
        for anuncio in lista:
            print(anuncio.toString())

    elif operacao=='F':
        operacao=input('C ou D?')
        if operacao=='C':
            cliente=input('Digite o nome cliente:')
            for anuncio in lista:
                if anuncio.getcliente()==cliente:
                    print(anuncio.toString())

        elif operacao=='D':
            inicio=input('Digite a data de inicio do anuncio:')
            termino=input('Digite a data de termino do anuncio:')
            for anuncio in lista:
                if anuncio.getinicio()==inicio and anuncio.gettermino()==termino:
                    print(anuncio.toString())

    else:
        print('Operação inválida!!')
