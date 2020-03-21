from acteurs.consultant import Consultant
from gestion_des_donnees.donnees import donnees

class Data_Scientist(Consultant):
    def __init__(self):
        self.est_connecte = False
        self.statut = "d"
        
    def se_connecter(self):
        
        with open("../files/comptes.txt", "r") as comptes:
            tampon = []
            liste_des_comptes = []
            ligne = None
            while ligne != "":
                ligne = comptes.readline()
                tampon.append(ligne)
        tampon.pop() # Retire le dernier élément du tableau qui est ""
        for s in tampon:
            liste_des_comptes.append(s[:-1]) #Supprime le caractère responsable du retour à la ligne
        n = len(liste_des_comptes)
        liste_des_statuts = [liste_des_comptes[i] for i in range(0, n, 3)]
        liste_des_pseudos = [liste_des_comptes[i] for i in range(1, n, 3)]
        liste_des_mots_de_passe = [liste_des_comptes[i] for i in range(2, n, 3)]
        
        pseudo = input("\nEntrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        
        for i in range(len(liste_des_statuts)):
            if self.statut == liste_des_statuts[i] and pseudo == liste_des_pseudos[i] and mot_de_passe == liste_des_mots_de_passe[i]:
                self.est_connecte = True
                print("\nVous êtes connecté !")
                continuer = input("Appuyez sur entrer pour continuer.")

        if not self.est_connecte:
            print("\nVotre connexion a échoué.")
            continuer = input("Appuyez sur entrer pour continuer.")
            
        return self.est_connecte
