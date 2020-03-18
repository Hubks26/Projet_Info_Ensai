from menu.menu_ouvert import Ouvert
from menu.menu_ferme import Ferme

class Derouleur:
    def __init__(self):
        pass
    
    def bienvenue(self):
        # affiche le message de bienvenue
        with open('../files/assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def aurevoir(self):
        with open('../files/assets/error.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def bordure(self):
        with open('../files/assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def creer_menu(self, contenu):
        vue_actuelle = Ouvert(contenu)
        while vue_actuelle:
            self.bordure()
            vue_actuelle = vue_actuelle.run()
        return vue_actuelle
