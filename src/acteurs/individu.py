from menu.menu_ferme import Ferme
from menu.menu_ouvert import Ouvert
from gestion_des_donnees.donnees import donnees

class Individu:
    def __init__(self):
        pass
    
    def quitter(self, contenu):
        continuer = input("Voulez-vous vraiment quitter (O/N) ? ")
        if continuer in ['o', 'O']:
            return Ferme()
        else:
            return Ouvert(contenu)
        
    def afficher_section(self, sections_dispo, contenu):
        
        if "text" in list(sections_dispo):
            print("\n")
            print(sections_dispo["text"])
            continuer = input("\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        
        choix_section = {}
        choix_section["question"] = "Choisissez une option."
        choix_section["individu"] = contenu["individu"]
        choix_section["options"] = list(sections_dispo)
        choix_section["actions"] = []
        
        for section in list(sections_dispo):
            tampon = sections_dispo[section]
            choix_section["actions"].append((lambda contenu, tampon=tampon : self.afficher_section(tampon, contenu)))
        
        choix_section["options"].append("RETOUR")
        choix_section["actions"].append((lambda var : Ouvert(contenu)))
        choix_section["options"].append("QUITTER")
        choix_section["actions"].append(Individu().quitter)
        
        return Ouvert(choix_section)
    
    def afficher_pays(self, contenu):
        
        choix_pays = {}
        choix_pays["question"] = "Choisissez une option."
        choix_pays["individu"] = contenu["individu"]
        choix_pays["options"] = []
        choix_pays["actions"] = []
        
        for num_pays in range(len(donnees)):
            if num_pays not in [41, 67, 173, 203, 253, 254, 255, 258, 260]:  # Trouver un moyen propre de faire ça
                choix_pays["options"].append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
                tampon = donnees[num_pays]
                choix_pays["actions"].append((lambda var, tampon=tampon : self.afficher_section(tampon, contenu)))
        choix_pays["options"].append("RETOUR")
        choix_pays["actions"].append((lambda var : Ouvert(contenu)))
        choix_pays["options"].append("QUITTER")
        choix_pays["actions"].append(Individu().quitter)
        
        return Ouvert(choix_pays)
