from acteurs.geographe import Geographe
from gestion_des_donnees.donnees import donnees

class Admin(Geographe):
    def __init__(self):
        self.pseudo = "admin"
        self.mot_de_passe = "istrateur"
        self.est_connecte = False
