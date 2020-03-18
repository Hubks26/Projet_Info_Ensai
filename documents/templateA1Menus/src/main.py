"""Lance l'application
"""
from management.manager import Manager
from menu.close_menu import Close
from menu.start import Start
import numpy as np

if __name__ == '__main__':

    mng = Manager()

    menu_acteurs, menu_actions = mng.preparer_contexte()
    memory_premier_vue = menu_acteurs


    # on démarre l'application avec une liste vide
    data = []
    memory_actions = {}
    memory_actions["question"] = menu_actions["question"]
    memory_actions.update({"data": []})


    continuer = True

    # affiche le message de bienvenue
    mng.bienvenu()

    while continuer:
        # Premier menu à afficher
        premier_vue = mng.creat_menu(memory_premier_vue)
        indices_actions = premier_vue.run()
        if isinstance(indices_actions, Close):
            mng.aurevoir()
            break

        memory_actions.update({"options": np.array(menu_actions["options"])[indices_actions]})
        memory_actions.update({"action_options": np.array(menu_actions["action_options"])[indices_actions]})

        # Deuxième menu
        second_vue = mng.creat_menu(memory_actions, auto_iter=True)

        continuer = input("Voulez-vous continuer (O/N) ? ")
        if continuer not in ['o', 'O']:
            # affiche le message de "Au revoir"
            mng.aurevoir()
            continuer = False
        else:
            mng.bordure()

