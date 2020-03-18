"""
Interface d'un Menu

(Cette classe est astraite, aucun objet de cette classe ne doit être crée)

Un menu est un objet qui implémente la fonction 'run()'
Cette fonction doit retourner un menu
"""

class AbstractVue():

    """inteface d'un menu"""

    def __init__(self, memory):
        """construction du menu

        :param memory: mémoire stockant les données de la session
        :type memory: Dictionnaire
        """
        self.memory = memory


    def run(self):
        """lancement du menu"""
        raise NotImplemented()




