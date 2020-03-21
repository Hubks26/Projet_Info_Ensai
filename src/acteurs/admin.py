from acteurs.geographe import Geographe
from gestion_des_donnees.donnees import donnees
from menu.menu_ouvert import Ouvert

class Admin(Geographe):
    def __init__(self):
        self.est_connecte = False
        self.statut = "a"
        
    def creer_compte(self, contenu):
        if self.est_connecte:
            while True:
                type_de_compte = input("\nQuel type de compte voulez vous créer (a/g/d) ? : ")
                if type_de_compte in ["a", "g", "d"]:
                    break
                print("\nLa réponse attendue doit être : a pour Admin, g pour Géographe ou d pour Data Scientist.")
            while True:
                pseudo = input("Entrez le pseudo : ")
                if len(pseudo) >= 1:
                        break
                print("\nVotre pseudo doit contenir au moins 1 caractères\n")
            while True:
                while True:
                    mot_de_passe = input("Entrez le mot de passe : ")
                    if len(mot_de_passe) >= 4:
                        break
                    print("\nVotre mot de passe doit contenir au moins 4 caractères\n")
                mot_de_passe_confirmation = input("Confirmez le mot de passe : ")
                if mot_de_passe == mot_de_passe_confirmation:
                    break
                print("\nLa confirmation ne correspond pas au mot de passe initial\n")
            with open("../files/comptes.txt", "a") as comptes:
                comptes.write("{}\n".format(type_de_compte))
                comptes.write("{}\n".format(pseudo))
                comptes.write("{}\n".format(mot_de_passe))
                continuer = input("\nLe compte a bien été enregistré.\nAppuyez sur entrer pour continuer.\n")
        else:
            print("\nVEUILLEZ D'ABORD VOUS CONNECTER.")
            continuer = input("Appuyez sur entrer pour continuer.")
            
        return Ouvert(contenu)
