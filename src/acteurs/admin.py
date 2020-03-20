from acteurs.geographe import Geographe
from gestion_des_donnees.donnees import donnees

class Admin(Geographe):
    def __init__(self):
        self.pseudo = "Admin"
        self.mot_de_passe = "nistrateur"
        self.est_connecte = False
        
    
