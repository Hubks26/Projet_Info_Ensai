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
        correction = input("\nEntrez la proposition de correction :\n> ")
        
        with open("../files/prop_corrections.txt", "a") as cor:
            cor.write(correction + '\n' + str(contenu["chemin de la recherche"][1:]) + '\n')
        
        continuer = input("\nVotre proposition de correction a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
