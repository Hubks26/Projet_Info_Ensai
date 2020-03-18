from acteurs.geographe import Geographe
from acteurs.data import donnees

class Admin(Geographe):
    def __init__(self):
        self.pseudo = "Admin"
        self.mot_de_passe = "nistrateur"
        self.est_connecte = False
        
    
