class Port:
    def __init__(self):
        self.__tabStock = []
    
    def ajouteStockage(self, stockage):
        self.__tabStock.append(stockage)
    
    def dechargement(self, navire):
        qteRestante = navire.obtenirQteFret()
        for stockage in self.__tabStock:
            if qteRestante <= stockage.obtenirCapaDispo():
                
                stockage.stocker(qteRestante)
                navire.decharger(qteRestante)
                qteRestante = navire.obtenirQteFret()
                break
            else:
                capaDispo = stockage.obtenirCapaDispo()
                stockage.stocker(capaDispo)
                navire.decharger(capaDispo)
                qteRestante = navire.obtenirQteFret()
            
