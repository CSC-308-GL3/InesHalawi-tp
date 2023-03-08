class Grade:
    def __init__(self, code, libelle, taux):
        self.code = code
        self.libelle = libelle
        self.taux = taux
        
    def getCode(self):
        return self.code
        
    def getLibelle(self):
        return self.libelle
        
    def tauxHoraire(self):
        return self.taux

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche
        
    def coutHoraire(self):
        anciennete = self.getAnciennete(self.dateEmbauche)
        if anciennete >= 15:
            taux = 1.12
        elif anciennete >= 11:
            taux = 1.08
        else:
            taux = 1.05
        return self.qualification.tauxHoraire() * taux
        
    def getNumero(self):
        return self.numero
        
    def getNom(self):
        return self.nom
        
    def getQualification(self):
        return self.qualification
        
    def getDateEmbauche(self):
        return self.dateEmbauche
        
    def getAnciennete(self, date):
        

class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm
        
    def distance(self):
        

class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien
        
    def affiche(self):
        print("Intervention numéro:", self.numero)
        print("Date:", self.date)
        print("Durée:", self.duree)
        print("Technicien:", self.technicien.getNom())
        
    def fraisKm(self, dist):
        return self.tarifKm * dist
        
    def fraisMo(self):
        return self.duree * self.technicien.coutHoraire()

class Contrat:
    def __init__(self, numero, date, client, montantContrat, interventions):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = interventions
        self.nbIntervention = len(interventions)
        
    def montant(self):
        return self.montantContrat
        
    def ecart(self):
        coutInterventions = sum([intervention.fraisKm(self.client.distance()) + intervention.fraisMo() for intervention in self.interventions])
        return self.montantContrat - coutInterventions
