from acteurs.individu import Individu
from acteurs.data import donnees
from menu.menu_ouvert import Ouvert
from menu.menu_ferme import Ferme
from correction.correction import Correction


class Consultant(Individu):
    def __init__(self):
        pass
    
    def afficher_section(self, sections_dispo, contenu):
        
        choix_section = {}
        choix_section["question"] = "Choisissez une option."
        choix_section["individu"] = contenu["individu"]
        choix_section["options"] = list(sections_dispo)
        choix_section["actions"] = [(lambda contenu : self.afficher_section(sections_dispo[section], contenu)) for section in list(sections_dispo)]
        
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
                choix_pays["actions"].append((lambda var : self.afficher_section(donnees[num_pays], contenu)))
                choix_pays["options"].append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
        choix_pays["options"].append("RETOUR")
        choix_pays["actions"].append((lambda var : Ouvert(contenu)))
        choix_pays["options"].append("QUITTER")
        choix_pays["actions"].append(Individu().quitter)
        
        return Ouvert(choix_pays)
        
        """
        print("\nDonnez le numéro du pays que vous souhaiter afficher :")
        
        while True:
            num_pays = input("> ")
            try:
                num_pays = int(num_pays)
            except ValueError:
                print("\nVotre réponse doit être un entier\n")
                continue
            if num_pays not in [i for i in range(len(donnees))] or num_pays in [41, 67, 173, 203, 253, 254, 255, 258, 260]:
                print("\nVotre réponse ne correspond à aucun pays.\n")
                continue
            break
        nom_pays = donnees[num_pays]['Government']['Country name']['conventional short form']['text']
        print("\nLe pays que vous avez sélectionné est '{}'.".format(nom_pays))
        continuer = input("Appuyez sur entrer pour continuer.")
        return Ouvert(contenu)
        """
    
