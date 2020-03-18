"""menu de démarrage

* initialise les données,
* et lance le menu principal.
"""

from menu.abstract_vue import AbstractVue
from menu.open_menu import Menu

class Start(AbstractVue):
    """menu de démarrage
        lance le menu principal.
    """
    def __init__(self, memory):
        """construction du menu

        :param memory: mémoire stockant les données de la session
        :type memory: Dictionnaire
        """
        AbstractVue.__init__(self, memory)

    def run(self):
        """lancement du menu"""
        menu_principal = Menu(self.memory)
        return menu_principal
