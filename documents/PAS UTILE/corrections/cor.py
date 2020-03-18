"""Ici une classe pour définir les Correction"""

class Correction: #Cette class est peut-être inutile
    def __init__(self, contenu):
        self.contenu = contenu
        self.is_ok = False

    def __str__(self):
        return self.contenu
