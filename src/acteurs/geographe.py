from acteurs.individu import Individu
from gestion_des_donnees.donnees import donnees

class Geographe:
    def __init__(self):
        self.pseudo = None
        self.mot_de_passe = None
        self.est_connecte = False
        
    def se_connecter(self):
        
        pseudo = input("\nEntrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        
        if self.pseudo == pseudo and self.mot_de_passe == mot_de_passe:
            print("\nVous êtes connecté !")
            continuer = input("Appuyez sur entrer pour continuer.")
            self.est_connecte = True
            
        else:
            print("\nVotre connexion a échoué.")
            continuer = input("Appuyez sur entrer pour continuer.")
            
        return self.est_connecte
    
