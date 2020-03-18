from menu.menu_ferme import Ferme
from menu.menu_ouvert import Ouvert

class Individu:
    def __init__(self):
        pass
    
    def quitter(self, contenu):
        continuer = input("Voulez-vous continuer (O/N) ? ")
        if continuer not in ['o', 'O']:
            return Ferme()
        else:
            return Ouvert(contenu)
