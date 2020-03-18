"""
Classe d'acteur comprenant son nom et deux méthodes:

[1] __repr()__

[2] set_indices_taches
"""

class Acteur():
    """
    Classe d'acteur comprenant son nom et deux méthodes:
    [1] __repr()__ : sert à afficher des informations concernant l'acteur (soit en console
    soit en utilisant la méthode print())

    [2] set_indices_taches:  Cette fonction reçoit les indices des tâches autorisées et
    ajoute cette information dans un attribut de classe
    """

    def __init__(self, nom):
        """

        :param nom: nom de l'acteur
        """
        self.nom = nom

    def __repr__(self):
        """

        :return: affiche info de l'acteur
        """
        ch = "Le nom de l'acteur est {}".format(self.nom)
        return ch

    def set_indices_taches(self, indices_taches):
        """
        Cette fonction reçoit les indices des tâches autorisées et ajoute cette information dans un attribut de classe
        :param indices_taches: indices des taches autorisés dans le menu selon les droits de l'acteur
        :return: les indices des taches autorisés
        """
        self.indicess_taches = indices_taches
        return self.indicess_taches


