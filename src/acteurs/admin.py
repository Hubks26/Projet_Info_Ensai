from acteurs.geographe import Geographe
from gestion_des_donnees.donnees import donnees
from menu.menu_ouvert import Ouvert

class Admin(Geographe):
    def __init__(self):
        self.est_connecte = False
        self.statut = "a"
        
    def creer_compte(self, contenu):
        
        with open("../files/comptes.txt", "r") as comptes:
            liste_des_comptes = []
            tampon = comptes.readlines()
        for s in tampon:
            liste_des_comptes.append(s[:-1]) #Supprime le caractère responsable du retour à la ligne
        n = len(liste_des_comptes)
        liste_des_pseudos = [liste_des_comptes[i] for i in range(1, n, 3)]
        
        while True:
            type_de_compte = input("\nQuel type de compte voulez vous créer (a/g/d) ? : ")
            if type_de_compte in ["a", "g", "d"]:
                break
            print("\nLa réponse attendue doit être : a pour Admin, g pour Géographe ou d pour Data Scientist.")
        while True:
            pseudo = input("Entrez le pseudo : ")
            if len(pseudo) >= 1:
                if pseudo not in liste_des_pseudos:
                    break
                else : print("\nCe pseudo est déjà attribué à quelqu'un, veuillez en choisir un autre.\n")
            else : print("\nVotre pseudo doit contenir au moins 1 caractères.\n")
        while True:
            while True: # On peut faire ça sans mettre deux while True, faire ça plus proprement si on a le temps.
                mot_de_passe = input("Entrez le mot de passe : ")
                if len(mot_de_passe) >= 4:
                    break
                print("\nVotre mot de passe doit contenir au moins 4 caractères.\n")
            mot_de_passe_confirmation = input("Confirmez le mot de passe : ")
            if mot_de_passe == mot_de_passe_confirmation:
                break
            print("\nLa confirmation ne correspond pas au mot de passe initial.\n")
        with open("../files/comptes.txt", "a") as comptes:
            comptes.write("{}\n".format(type_de_compte))
            comptes.write("{}\n".format(pseudo))
            comptes.write("{}\n".format(mot_de_passe))
            continuer = input("\nLe compte a bien été enregistré.\nAppuyez sur entrer pour continuer.\n")
        return Ouvert(contenu)
    
    def supprimer_compte(self, contenu):
        print("\nATTENTION : Si vous supprimez votre propre compte, vous ne pourrez plus vous connecter après avoir rejoint le menu de choix du statut ou après avoir quitté l'application.")
        pseudo_a_supprimer = input("\nEntrez le pseudo du compte à supprimer : ")
        with open("../files/comptes.txt", "r") as comptes:
            liste_des_comptes = []
            tampon = comptes.readlines()
        for s in tampon:
            liste_des_comptes.append(s[:-1]) #Supprime le caractère responsable du retour à la ligne
        n = len(liste_des_comptes)
        liste_des_pseudos = [liste_des_comptes[i] for i in range(1, n, 3)]
        
        if pseudo_a_supprimer not in liste_des_pseudos:
            continuer = input("\nCe compte n'existe pas.\nAppuyez sur entrer pour continuer.\n")
        else :
            with open("../files/comptes.txt", "r") as comptes:
                nouvelle_liste_des_comptes = []
                indice = None
                for line in liste_des_comptes:
                    if line == pseudo_a_supprimer:
                        indice = liste_des_comptes.index(line)
                for i in range(len(liste_des_comptes)):
                    if i not in [indice-1,indice,indice+1]:
                        nouvelle_liste_des_comptes.append(liste_des_comptes[i])
            with open("../files/comptes.txt", "w") as comptes:
                for line in nouvelle_liste_des_comptes:
                    comptes.write(line+"\n")
            continuer = input("\nLe compte de {} a bien été supprimé.\nAppuyez sur entrer pour continuer.".format(pseudo_a_supprimer))
        return Ouvert(contenu)
