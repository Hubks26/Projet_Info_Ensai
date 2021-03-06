from acteurs.consultant import Consultant
from acteurs.individu import Individu
from acteurs.data_scientist import Data_Scientist
from acteurs.geographe import Geographe
from acteurs.admin import Admin
from menu.menu_ouvert import Ouvert

def connexion(contenu):
    
    menu_acteur = contenu
    
    if menu_acteur["individu"].se_connecter():
        del menu_acteur["options"][0]
        del menu_acteur["actions"][0]
        return Ouvert(menu_acteur)
    else:
        return Ouvert(contenu)

def indices_taches_permises(indices_taches, individu):
    
    menu_acteur = {}
    menu_acteur["individu"] = individu
    menu_acteur["question"] = menus[1]["question"]
    menu_acteur["options"] = [menus[1]["options"][i] for i in indices_taches]
    menu_acteur["actions"] = [menus[1]["actions"][i] for i in indices_taches]
    menu_acteur["chemin de la recherche"] = []
            
    return Ouvert(menu_acteur)

def ajouter_ou_supprimer_compte(contenu):
    menu_choix_ajouter_supprimer = {}
    menu_choix_ajouter_supprimer["individu"] = contenu["individu"]
    
    if menu_choix_ajouter_supprimer["individu"].est_connecte:
    
        menu_choix_ajouter_supprimer["question"] = "Voulez vous créer ou supprimer un compte ?"
        menu_choix_ajouter_supprimer["options"] = ["Créer","Supprimer","RETOUR","QUITTER"]
        menu_choix_ajouter_supprimer["chemin de la recherche"] = contenu["chemin de la recherche"]
        menu_choix_ajouter_supprimer["actions"] = [(lambda contenu : contenu["individu"].creer_compte(contenu)), (lambda contenu : contenu["individu"].supprimer_compte(contenu)), (lambda var : Ouvert(contenu)), Individu().quitter]
        return Ouvert(menu_choix_ajouter_supprimer)
    
    else:
        print("\nVEUILLEZ D'ABORD VOUS CONNECTER.")
        input("Appuyez sur entrer pour continuer.")
        return Ouvert(contenu)


# FONCTION TEMPORAIRE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def temporaire_function(contenu):                                                                                    #
    if not contenu["individu"].est_connecte:                                                                         #
        print("\nVEUILLEZ D'ABORD VOUS CONNECTER.")                                                                  #   
        input("Appuyez sur entrer pour continuer.")                                                                  #
    else:                                                                                                            #
        print("\nCette fonctionnalité n'a pas encore été codée...")                                                  #   
        input("Appuyez sur entrer pour continuer.")                                                                  #  
    return Ouvert(contenu)                                                                                           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

menus = [
{
    "question" : 
        "Quel est votre statut ?",
    "options" : 
    [
        "Consultant", 
        "Data Scientist", 
        "Géographe",
        "Administrateur",
        "QUITTER"
    ],
    "actions" : 
    [
        (lambda contenu : indices_taches_permises([1, 7, 8], Consultant())),
        (lambda contenu : indices_taches_permises([0, 1, 2, 3, 4, 7, 8], Data_Scientist())),
        (lambda contenu : indices_taches_permises([0, 1, 5, 7, 8], Geographe())),
        (lambda contenu : indices_taches_permises([0, 1, 2, 3, 4, 5, 6, 7, 8], Admin())),
        Individu().quitter
    ],
    "individu" :
        Individu(),
    "chemin de la recherche" :
        []
},
{
    "question" : 
        "Que voulez vous faire ?",
    "options" : 
    [   
        "Se connecter",
        "Afficher les données d'un pays",
        "Acceder aux résumés statistiques",
        "Représentations graphiques",
        "Recherche avancée",
        "Décider de valider ou de refuser une correction",
        "Créer ou supprimer un compte",
        "RETOUR AU MENU DE CHOIX DU STATUT",
        "QUITTER"
    ],
    "actions" : 
    [
        connexion,
        (lambda contenu : contenu["individu"].afficher_pays(contenu)), # C'est pour ça que le système de connexion marche ici.
        (lambda contenu : contenu["individu"].resume_stat(contenu)),
        (lambda contenu : contenu["individu"].representation_graphique(contenu)),
        temporaire_function,
        (lambda contenu : contenu["individu"].gestion_corrections(contenu)),
        ajouter_ou_supprimer_compte,
        (lambda contenu : Ouvert(menus[0])),
        Individu().quitter
    ],
    "individu" :
        Individu(),
    "chemin de la recherche" :
        []
}]

