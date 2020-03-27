from acteurs.individu import Individu
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"


class Consultant(Individu):
    def __init__(self):
        pass
    
    def afficher_section(self, section, sections_dispo, contenu):
        
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        
            choix_section = {}
            choix_section["chemin de la recherche"] = contenu["chemin de la recherche"]
            
            if isinstance(section, int):
                choix_section["chemin de la recherche"].append(sections_dispo['Government']['Country name']['conventional short form']['text'])
                
            choix_section["chemin de la recherche"].append(section)
            
            if "text" in list(sections_dispo):
                print("\n")
                print("PAYS : {}\n".format(choix_section["chemin de la recherche"][0]))
                print(sections_dispo["text"])
                rep = input("\nVoulez vous proposer une correction (O/N) ?\n> ")
                if rep in ["o","O"]:
                    self.proposer_correction(choix_section)
                choix_section["chemin de la recherche"].pop()
                return Ouvert(contenu)

            choix_section["question"] = "Choisissez une option."
            choix_section["individu"] = contenu["individu"]
            choix_section["options"] = list(sections_dispo)
            choix_section["actions"] = []
            
            for sec in list(sections_dispo):
                tampon1 = sec
                tampon2 = sections_dispo[sec]
                choix_section["actions"].append((lambda contenu, tampon1=tampon1, tampon2=tampon2 : self.afficher_section(tampon1, tampon2, contenu)))
                
            choix_section["options"].append("RETOUR")
            choix_section["actions"].append((lambda var : self.retour_section(contenu)))
            choix_section["options"].append("QUITTER")
            choix_section["actions"].append(Individu().quitter)
        
        return Ouvert(choix_section)
    
    def retour_section(self, contenu):
        contenu["chemin de la recherche"].pop()
        if len(contenu["chemin de la recherche"]) == 1:
            contenu["chemin de la recherche"].pop()
        return Ouvert(contenu)
    
    def afficher_pays(self, contenu):
        
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        
            choix_pays = {}
            choix_pays["question"] = "Choisissez un pays."
            choix_pays["individu"] = contenu["individu"]
            choix_pays["options"] = []
            choix_pays["actions"] = []
            choix_pays["chemin de la recherche"] = []
            
            for num_pays in range(len(donnees)):
                if num_pays not in [41, 67, 173, 203, 253, 254, 255, 258, 260]:  # Trouver un moyen propre de faire ça
                    choix_pays["options"].append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
                    tampon1 = num_pays
                    tampon2 = donnees[num_pays]
                    choix_pays["actions"].append((lambda var, tampon1=tampon1, tampon2=tampon2 : self.afficher_section(tampon1, tampon2, contenu)))
                    
            choix_pays["options"].append("RETOUR")
            choix_pays["actions"].append((lambda var : Ouvert(contenu)))
            choix_pays["options"].append("QUITTER")
            choix_pays["actions"].append(Individu().quitter)
        
        return Ouvert(choix_pays)
    
    def proposer_correction(self, contenu):
        correction = input("\nEntrez la proposition de correction :\n> ")
        
        with open("../files/prop_corrections.txt", "a") as cor:
            cor.write(correction + '\n' + str(contenu["chemin de la recherche"][1:]) + '\n')
        
        continuer = input("\nVotre proposition de correction a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
        
        
