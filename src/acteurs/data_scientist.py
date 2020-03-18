from acteurs.consultant import Consultant
from acteurs.data import donnees

class Data_Scientist(Consultant):
    def __init__(self):
        self.pseudo = None
        self.mot_de_passe = None
        self.est_connecte = False
        
    def se_connecter(self):
        
        pseudo = input("Entrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        
        if self.pseudo == pseudo and self.mot_de_passe == mot_de_passe:
            continuer = input("Vous êtes connecté ! Appuyez sur entrer pour continuer")
            self.est_connecte = True
            
        else:
            continuer = input("Votre connexion a échoué. Appuyez sur entrer pour continuer")
            
        return self.est_connecte
