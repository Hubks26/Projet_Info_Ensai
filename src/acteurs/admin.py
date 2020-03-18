from acteurs.geographe import Geographe
from acteurs.data import donnees

class Admin(Geographe):
    def __init__(self, pseudo, mot_de_passe):
        self.pseudo = pseudo
        self.mot_de_passe = mot_de_passe
        
    
