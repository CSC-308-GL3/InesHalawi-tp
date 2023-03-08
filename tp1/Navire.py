
class Navire:
    def __init__(self, noNavire, nomNavire, libelleFret, qteFret):
        self.__noNavire = noNavire
        self.__nomNavire = nomNavire
        self.__libelleFret = libelleFret
        self.__qteFret = qteFret
    
    def obtenirQteFret(self):
        return self.__qteFret
    
    def decharger(self, qte):
        self.__qteFret -= qte
        
    def estDecharge(self):
        return self.__qteFret == 0

     