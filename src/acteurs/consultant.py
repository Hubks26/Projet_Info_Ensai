from acteurs.individu import Individu, Ouvert
from acteurs.data import donnees

class Consultant(Individu):
    def __init__(self):
        pass
    
    def afficher_pays(self, contenu):
        print("Donnez le numéro du pays que vous souhaiter afficher :")
        while True:
            num_pays = input("> ")
            try:
                num_pays = int(num_pays)
            except ValueError:
                print("Votre réponse doit être un entier")
                continue
            try:
                assert num_pays in [i for i in range(len(donnees))]
            except AssertionError:
                print("Votre réponse ne correspond à aucun pays.")
                continue
            break
        
        nom_pays = donnees[num_pays]['Government']['Country name']['conventional short form']['text']
        print("Le pays que vous avez sélectionné est '{}'. Appuyez sur entrer pour continuer.".format(nom_pays))
        continuer = input("")
        return Ouvert(contenu)
