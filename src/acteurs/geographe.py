from acteurs.individu import Individu
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"

class Geographe(Individu):
    def __init__(self):
        self.est_connecte = False
        self.statut = "g"
        self.contenu_du_menu_initial = {}
        
    def se_connecter(self):
        
        with open("../files/comptes.txt", "r") as comptes:
            liste_des_comptes = []
            tampon = comptes.readlines()
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
    
    def modifier_texte(self, contenu):
        if not self.est_connecte:
            continuer = input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
        else:
            modification = input("\nEntrez le nouveau texte :\n> ")
            with open(directory_data + filename) as json_file:
                donnees = json.load(json_file)
            chemin = contenu["chemin de la recherche"][1:]
            contenu_section = donnees[chemin[0]]
            for section in chemin[1:]:
                contenu_section = contenu_section[section]
                
            confirmation = input("\nConfirmation de la modification #Cela écrasera le texte initial# (O/N) ?\n> ")
            if confirmation in ["o","O"]:
                contenu_section["text"] = modification # Ici on modifie bien la variable donnees
                with open(directory_data + filename, "w") as json_file:
                    json.dump(donnees, json_file)
                continuer = input("\nVotre modification a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
            else :
                continuer = input("\nVotre tentative de modification n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                
    def ajout_section(self, contenu, contenu_precedent):
        if not self.est_connecte:
            continuer = input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        else:
            choix = input("\nVoulez vous ajouter une Section ou un Texte ? (S/T) ?\nAppuyez sur une autre touche si vous voulez ne rien modifier.\n> ")
            if choix in ["s", "S"]:
                nouvelle_section = input("\nEntrez le nom de la nouvelle section :\n> ")
                with open(directory_data + filename) as json_file:
                    donnees = json.load(json_file)
                chemin = contenu["chemin de la recherche"][1:]
                contenu_section = donnees[chemin[0]]
                for section in chemin[1:]:
                    contenu_section = contenu_section[section]
                if nouvelle_section in contenu_section.keys() or nouvelle_section in ["AJOUTER OU RENOMMER","RETOUR","QUITTER"]:
                    continuer = input("\nCette section existe déjà !\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu)
                confirmation = input("\nConfirmation de la création de la section (O/N) ?\n> ")
                if confirmation in ["o","O"]:
                    contenu_section[nouvelle_section] = {}
                    with open(directory_data + filename, "w") as json_file:
                        json.dump(donnees, json_file)
                    continuer = input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                else :
                    continuer = input("\nVotre tentative d'ajout n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu)
                
                tampon = contenu["chemin de la recherche"].pop()
                if len(contenu["chemin de la recherche"]) == 1:
                    contenu["chemin de la recherche"].pop()
                return self.afficher_section(tampon, contenu_precedent)
            
            elif choix in ["t", "T"]:
                with open(directory_data + filename) as json_file:
                    donnees = json.load(json_file)
                chemin = contenu["chemin de la recherche"][1:]
                contenu_section = donnees[chemin[0]]
                for section in chemin[1:]:
                    contenu_section = contenu_section[section]
                
                if len(contenu_section) != 0:
                    continuer = input("\nL'ajout d'un texte ne peut se faire que dans une section vide !\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu)
                else:
                    nouveau_texte = input("\nEntrez le texte à ajouter :\n> ")
                    confirmation = input("\nConfirmation de l'ajout du texte (O/N) ?\n> ")
                    if confirmation in ["o","O"]:
                        contenu_section["text"] = nouveau_texte
                        with open(directory_data + filename, "w") as json_file:
                            json.dump(donnees, json_file)
                        continuer = input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                contenu["chemin de la recherche"].pop()
                tampon = contenu["chemin de la recherche"].pop()
                if len(contenu["chemin de la recherche"]) == 1:
                    contenu["chemin de la recherche"].pop()
                return self.afficher_section(tampon, contenu_precedent)
            else:
                return Ouvert(contenu)
            
    def ajout_pays(self, contenu, contenu_precedent):
        if not self.est_connecte:
            continuer = input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu_precedent)
        else:
            nom_pays = input("\nEntrez le nom du pays à ajouter :\n> ")
            with open(directory_data + filename) as json_file:
                donnees = json.load(json_file)
            liste_des_pays = []
            for num_pays in range(len(donnees)):
                if num_pays not in [41, 67, 173, 203, 253, 254, 255, 258, 260]:
                    liste_des_pays.append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
            if nom_pays not in liste_des_pays:
                confirmation = input("\nConfirmation de l'ajout du pays (O/N) ?\n> ")
                if confirmation in ["o","O"]:
                    donnees.append({'Government' : {'Country name' : {'conventional short form' : {'text' : nom_pays}}}})
                    with open(directory_data + filename, "w") as json_file:
                        json.dump(donnees, json_file)
                    continuer = input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                    return self.afficher_pays(contenu)
                else:
                    continuer = input("\nVotre tentative d'ajout n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu_precedent)
            else:
                continuer = input("\nCe pays existe déjà !\nAppuyez sur entrer pour continuer.")
                return Ouvert(contenu_precedent)
