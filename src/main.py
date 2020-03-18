from derouleur.derouleur import Derouleur
from menu.menus import menus

if __name__ == '__main__':
    
    der = Derouleur()
    der.bienvenue()
    der.creer_menu(menus[0])
    der.aurevoir()
