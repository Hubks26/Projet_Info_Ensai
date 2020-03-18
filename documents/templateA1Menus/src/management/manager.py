from menu.close_menu import Close
from menu.start import Start
from metiers.acteur import Acteur
from metiers.data_manimulation import DataManipulation
from metiers.super_acteur import SuperActeur
import numpy as np

class Manager:
    """
    Cette classe gère la relation entre les acteurs et leur taches autorisées
    """
    def __init__(self):
        pass

    def preparer_contexte(self):
        """
        On fait ici l'hypothèse que chaque menu comprenne au moins trois composante:
        -  question: La question à poser qui est une chaine de charactère
        -  options: la liste de possibilités qui est une liste de chaines de charactères
        -  action_options: la liste
        :return:
        """
        menu_actions = {
            "question": "Que désirez-vous faire ?",
            "options": ["Ajouter une donnée",
                        "Retirer la dernière donnée",
                        "Voir les statistiques sur les données",
                        "Quitter"],
            "action_options": [(lambda memory: DataManipulation(memory).add_data()),
                               (lambda memory: DataManipulation(memory).remove_last_data()),
                               (lambda memory: DataManipulation(memory).print_statistics()),
                               (lambda memory: Close(memory))]
        }

        nb_actions = len(menu_actions["options"])
        
        menu_acteurs = {
            "question": "Quel est votre statut?",
            "options": ["Consultant", "Data Scientist", "Géographe", "Administrateur", "Quitter"],
            "action_options": [lambda memory: Acteur("Un acteur").set_indices_taches([0, 3]),
                               lambda memory: SuperActeur("Super acteur").set_indices_taches(list(range(nb_actions))),
                               lambda memory: Close(memory)]
        }
            
        return menu_acteurs, menu_actions

    def bienvenu(self):
        # affiche le message de bienvenue
        with open('../files/assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def aurevoir(self):
        with open('../files/assets/cat.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def bordure(self):
        with open('../files/assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def creat_menu(self, info_menus , auto_iter=False):
        current_vue = Start(info_menus)
        if auto_iter:
            max_iter = np.inf
        else:
            max_iter = 1
        i = 0
        # tant qu'on a un écran à afficher et qu'on n'a pas dépassé le nb max d'iterations, on continue
        while current_vue and (i < max_iter):
            # on affiche une bordure pour séparer les menu
            self.bordure()

            # le menu agit (demande d'action à effectuer, réalisation de l'action, préparation du prochain menu, ...)
            current_vue = current_vue.run()
            i += 1
        return current_vue
