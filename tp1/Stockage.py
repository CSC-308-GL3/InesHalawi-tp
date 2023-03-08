class Stockage: 

    def __init__(self, capaMax, capaDispo):
        self.__capaDispo = capaDispo
        self.__capaMax = capaMax

    def obtenirCapaDispo(self):
        return self.__capaDispo

    def stocker(self, qte):
        self.__capaDispo += qte

    def estVide(self):
        return self.__capaDispo == self.__capaMax

    def estRemplie(self):
        return self.__capaDispo == 0