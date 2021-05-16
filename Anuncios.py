import math
from datetime import datetime

class Anuncio:

    def __init__(self,nome,cliente,inicio,termino,investimento):

        self.nome=nome
        self.cliente=cliente
        self.inicio=inicio
        self.termino=termino
        self.investimento=investimento

    def getincio(self):
        return self.inicio

    def gettermino(self):
        return self.termino

    def getcliente(self):
        return self.cliente

    def setnome(self,nome):
        self.nome=nome

    def toString(self):
        return 'Anuncio:'+self.nome+'\nCliente:'+self.cliente\
               +'\nData de Inicio do anuncio: ' +self.inicio\
               +'\nData de termino do anuncio: '+self.termino\
               +'\nInvestimento diario:'+str(self.investimento)\
               +'\nVisualiçao total:'+str(self.visualizacaototal())\
               +'\nMaximo de cliques'+str(self.maxcliques())\
               +'\nMaximo de compartilhamentos:'+str(self.maxcompartilhamento())\
               +'\nInvestimento total:'+str(self.investimentototal())

    def isnumber(self):
        try:
            float(self.investimento)
        except ValueError:
            return False
        return True

    def visualizacaototal(self):
        if self.isnumber() == False: return 'Impossivel'

        visualizacoes = float(self.investimentototal()) * 30

        retorno = visualizacoes

        for x in range(1, 5):
            retorno = self.total(retorno)
            visualizacoes += retorno

        return int(visualizacoes)

    def total(self,v):

        return math.floor(self.compartilhamento(self.cliques(v)) * 40)

    def cliques(self,v):
        return  math.floor(v * 12 / 100)

    def compartilhamento(self,pc):
        return math.floor((pc * 3) / 20)
    def maxcliques(self):
        return self.cliques(self.visualizacaototal())
    def maxcompartilhamento(self):

        return self.compartilhamento(self.maxcliques())

    def data(self):
        d1 = datetime.strptime(self.inicio,'%d/%m/%Y')
        d2 = datetime.strptime(self.termino,'%d/%m/%Y')
        return abs((d2 - d1).days)
    def investimentototal(self):
        return self.investimento*self.data()









