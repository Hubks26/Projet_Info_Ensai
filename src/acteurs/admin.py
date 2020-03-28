from acteurs.geographe import Geographe
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"

class Admin(Geographe):
    def __init__(self):
        self.est_connecte = False
        self.statut = "a"
        self.contenu_du_menu_initial = {}
        
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
            if len(pseudo) >= 2:
                if pseudo not in liste_des_pseudos:
                    break
                else : print("\nCe pseudo est déjà attribué à quelqu'un, veuillez en choisir un autre.\n")
            else : print("\nVotre pseudo doit contenir au moins 2 caractères.\n")
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
    
    def supprimer_section(self, contenu, contenu_precedent): # Il doit y avoir un moyen plus simple de faire cette fonction
        if not self.est_connecte:
            continuer = input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        section_a_supprimer = input("\nVeuillez entrer le nom de la section à supprimer : ")
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        chemin = contenu["chemin de la recherche"][1:]
        contenu_section = donnees[chemin[0]]
        for section in chemin[1:]:
            contenu_section = contenu_section[section]
        if section_a_supprimer in contenu_section.keys():
            confirmation = input("\nConfirmation de la suppression de la section #Cela supprimera aussi toutes ses sous-sections# (O/N) ?\n> ")
            if confirmation in ["o","O"]:
                del contenu_section[section_a_supprimer]
                with open(directory_data + filename, "w") as json_file:
                    json.dump(donnees, json_file)
                continuer = input("\nLa section a bien été supprimée.\nAppuyez sur entrer pour continuer.")
            else :
                continuer = input("\nVotre tentative de suppression n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                return Ouvert(contenu)
        else:
            continuer = input("\nCette section n'existe pas.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        tampon = contenu["chemin de la recherche"].pop()
        if len(contenu["chemin de la recherche"]) == 1:
            contenu["chemin de la recherche"].pop()
        return self.afficher_section(tampon, contenu_precedent)
            
