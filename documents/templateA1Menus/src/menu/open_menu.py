"""menu principal
Affichage le menu principale et activer les actions associées
"""

from menu.abstract_vue import AbstractVue

class Menu(AbstractVue):
    """menu principal
    """
    def __init__(self, memory):
        """construction du menu

        :param memory: mémoire stockant les données de la session
        :type memory: Dictionnaire
        """
        AbstractVue.__init__(self, memory)

    def run(self):
        """lancement du menu"""
        # Afficher la question principale du mrnu
        print(self.memory["question"])

        options = self.memory["options"]
        nb_options = len(options)
        options_action =self.memory["action_options"]

        # afficher le menu
        for i, mes in enumerate(options):
            print("[{}] {}".format(i+1, mes))

        # l'utilisateur choisit une option
        while True:
            choice = input("> ")
            print(choice)
            try:
                choice = int(choice)
            except ValueError:
                print("La réponse attendu doit être un entier")
                continue
            if choice <= 0 or choice > nb_options:
                print("La réponse attendu doit être comprise entre 1 et {}".format(nb_options))
                continue
            break

        # on applique son choix
        return options_action[choice - 1](self.memory)

