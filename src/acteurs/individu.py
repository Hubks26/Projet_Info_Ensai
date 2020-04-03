from menu.menu_ferme import Ferme
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"

class Individu:
    def __init__(self):
        self.statut = "i"
        self.contenu_du_menu_initial = {}
    
    def quitter(self, contenu):
        confirmation = input("\nVoulez-vous vraiment quitter (O/N) ? ")
        if confirmation in ['o', 'O']:
            return Ferme()
        else:
            return Ouvert(contenu)

    def afficher_section(self, section, contenu):
        
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        
            choix_section = {}
            choix_section["chemin de la recherche"] = contenu["chemin de la recherche"]
            
            if isinstance(section, int):
                choix_section["chemin de la recherche"].append(donnees[section]['Government']['Country name']['conventional short form']['text'])
                
            choix_section["chemin de la recherche"].append(section)
            
            chemin = contenu["chemin de la recherche"][1:]
            sections_dispo = donnees[chemin[0]]
            for sec in chemin[1:]:
                sections_dispo = sections_dispo[sec]
            
            if "text" in list(sections_dispo):
                if self.statut == "g" or self.statut == "a":
                    print("\n")
                    print("PAYS : {}\n".format(choix_section["chemin de la recherche"][0]))
                    print(sections_dispo["text"])
                    rep = input("\nVoulez vous modifier le texte (O/N) ?\n> ")
                    if rep in ["o","O"]:
                        self.modifier_texte(choix_section)
                    choix_section["chemin de la recherche"].pop()
                    return Ouvert(contenu)
                else:
                    print("\n")
                    print("PAYS : {}\n".format(choix_section["chemin de la recherche"][0]))
                    print(sections_dispo["text"])
                    rep = input("\nVoulez vous proposer une correction (O/N) ?\n> ")
                    if rep in ["o","O"]:
                        self.proposer_correction(choix_section)
                    choix_section["chemin de la recherche"].pop()
                    return Ouvert(contenu)
            
            if len(list(sections_dispo)) == 0:
                choix_section["question"] = "Cette section est vide."
            else :
                choix_section["question"] = "Choisissez une option."
            choix_section["individu"] = contenu["individu"]
            choix_section["options"] = list(sections_dispo)
            choix_section["actions"] = []
            
            for sec in list(sections_dispo):
                tampon1 = sec
                choix_section["actions"].append((lambda contenu, tampon1=tampon1 : self.afficher_section(tampon1, contenu)))
                
            if self.statut == "g" or self.statut == "a":
                if len(list(sections_dispo)) == 0:
                    choix_section["options"].append("AJOUTER UNE SECTION OU UN TEXTE")
                else:
                    choix_section["options"].append("AJOUTER UNE SECTION")
                choix_section["actions"].append(lambda var : self.ajout_section(var, contenu))
            if self.statut == "a":
                choix_section["options"].append("SUPPRIMER UNE SECTION")
                choix_section["actions"].append(lambda var : self.supprimer_section(var, contenu))
            choix_section["options"].append("RETOUR")
            choix_section["actions"].append(lambda var : self.retour_section(contenu))
            choix_section["options"].append("RETOUR AU MENU DE L'ACTEUR")
            choix_section["actions"].append(lambda var : Ouvert(self.contenu_du_menu_initial))
            choix_section["options"].append("QUITTER")
            choix_section["actions"].append(Individu().quitter)
        
        return Ouvert(choix_section)
    
    def retour_section(self, contenu):
        if len(contenu["chemin de la recherche"]) <= 2:
            contenu["chemin de la recherche"] = []
            return self.afficher_pays(contenu)
        else:
            contenu["chemin de la recherche"].pop()
            if len(contenu["chemin de la recherche"]) == 1:
                contenu["chemin de la recherche"].pop()
            tampon = contenu["chemin de la recherche"].pop()
            if len(contenu["chemin de la recherche"]) == 1:
                contenu["chemin de la recherche"].pop()
            return self.afficher_section(tampon, contenu)
    
    def afficher_pays(self, contenu):
        
        if self.contenu_du_menu_initial == {}:
            self.contenu_du_menu_initial = contenu
        self.contenu_du_menu_initial["chemin de la recherche"] = []
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        
            choix_pays = {}
            choix_pays["question"] = "Choisissez un pays."
            choix_pays["individu"] = contenu["individu"]
            choix_pays["options"] = []
            choix_pays["actions"] = []
            choix_pays["chemin de la recherche"] = []
            
            with open("../files/liste_pays_sans_nom.txt", "r") as liste:
                liste_pays_sans_nom0 = liste.readlines()
            liste_pays_sans_nom = []
            for elm in liste_pays_sans_nom0:
                liste_pays_sans_nom.append(int(elm[:-1]))
            
            for num_pays in range(len(donnees)):
                if num_pays not in liste_pays_sans_nom:
                    choix_pays["options"].append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
                    tampon1 = num_pays
                    choix_pays["actions"].append(lambda var, tampon1=tampon1 : self.afficher_section(tampon1, contenu))
                    
            if self.statut == "g" or self.statut == "a":
                choix_pays["options"].append("AJOUTER UN PAYS")
                choix_pays["actions"].append(lambda var : self.ajout_pays(contenu, var))
            if self.statut == "a":
                choix_pays["options"].append("SUPPRIMER UN PAYS")
                choix_pays["actions"].append(lambda var : self.supprimer_pays(contenu, var))
            choix_pays["options"].append("RETOUR AU MENU DE L'ACTEUR")
            choix_pays["actions"].append(lambda var : Ouvert(self.contenu_du_menu_initial))
            choix_pays["options"].append("QUITTER")
            choix_pays["actions"].append(Individu().quitter)
        
        return Ouvert(choix_pays)
    
    def proposer_correction(self, contenu):
        pass
        
    def modifier_texte(self,contenu):
        pass
        
    def ajout_section(self, contenu, contenu_precedent):
        pass
    
    def ajout_pays(self, contenu, contenu_precedent):
        pass
    
    def supprimer_section(self, contenu, contenu_precedent):
        pass
    
    def supprimer_pays(self, contenu, contenu_precedent):
        pass
