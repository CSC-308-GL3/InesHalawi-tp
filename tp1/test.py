from Navire import Navire
from Port import Port
from Stockage import Stockage


class Test:
    def __init__(self):
        # Création des stockages
        silo1 = Stockage(150, 100)
        silo2 = Stockage(200, 280)
        silo3 = Stockage(370, 300)
        hangar1 = Stockage(1000, 500)
        hangar2 = Stockage(1000, 750)

        # Création du port et ajout des stockages
        port = Port()
        port.ajouteStockage(silo1)
        port.ajouteStockage(silo2)
        port.ajouteStockage(silo3)
        port.ajouteStockage(hangar1)
        port.ajouteStockage(hangar2)

        # Création du navire ESMERALDA
        esmeralda = Navire("0092493603", "ESMERALDA", "Riz", 1200)

        # Déchargement du navire
        while not esmeralda.estDecharge():
            port.dechargement(esmeralda)

        # Affichage des stocks finaux
        print("Stocks finaux:")
        for stockage in [silo1, silo2, silo3, hangar1, hangar2]:
            print(f"{type(stockage).__name__}: {stockage.obtenirCapaDispo()} tonnes")

test = Test()