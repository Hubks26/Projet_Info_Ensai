import menu.open_menu



class DataManipulation():

    def __init__(self, memory):
        """construction du menu

        :param memory: mémoire stockant les données de la session
        :type memory: Dictionnaire
        """
        self.memory = memory

    def add_data(self):
        """lancement du menu"""
        # récupération de la valeure à ajouter
        print("Quelle valeur désirez-vous ajouter ?")
        while True:
            value = input("> ")
            try:
                value = float(value)
            except ValueError:
                print("La réponse attendu doit être un nombre réel")
                continue
            break
        # ajout de la valeur
        self.memory["data"].append(value)
        return menu.open_menu.Menu(self.memory)


    def remove_last_data(self):
        """lancement du menu"""
        # retrait (si possible)
        if len(self.memory["data"]) == 0:
            print("ATTENTION : Il n'y a pas de données à retirer")
        else:
            self.memory["data"].pop()
            print("retrait effectué")
        # retour au menu d'acceuil
        return menu.open_menu.Menu(self.memory)

    def print_statistics(self):
        """lancement du menu"""
        # affiche les statistiques (si possible)
        if len(self.memory["data"]) == 0:
            print("ATTENTION : Il n'y a pas de données à afficher")
        else:
            print("plus petite valeur", min(self.memory["data"]))
            print("plus grande valeur", max(self.memory["data"]))
        # retour au menu d'acceuil
        return menu.open_menu.Menu(self.memory)
    
