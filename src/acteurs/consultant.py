from acteurs.individu import Individu
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"


class Consultant(Individu):
    def __init__(self):
        self.statut = "c"
        self.contenu_du_menu_initial = {}
    
    def proposer_correction(self, contenu):
        while True:
            correction = input("\nEntrez la proposition de correction :\n> ")
            if len(correction) > 1:
                break
            print("\nVotre texte doit contenir au moins 1 caractère\n")
        with open("../files/prop_corrections.txt", "a") as cor:
            chemin = contenu["chemin de la recherche"][0]
            for elm in contenu["chemin de la recherche"][1:]:
                chemin += "//" + str(elm)
            cor.write(correction + '\n' + chemin + '\n')
        
        continuer = input("\nVotre proposition de correction a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
