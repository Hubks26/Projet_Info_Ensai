from acteurs.consultant import Consultant
from acteurs.individu import Individu
from acteurs.data_scientist import Data_Scientist
from acteurs.geographe import Geographe
from acteurs.admin import Admin
from menu.menu_ouvert import Ouvert

def connection(contenu):
    
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
    menu_acteur["pays"] = None
            
    return Ouvert(menu_acteur)

def ajouter_ou_supprimer_compte(contenu):
    menu_choix_ajouter_supprimer = {}
    menu_choix_ajouter_supprimer["individu"] = contenu["individu"]
    
    if menu_choix_ajouter_supprimer["individu"].est_connecte:
    
        menu_choix_ajouter_supprimer["question"] = "Voulez vous créer ou supprimer un compte ?"
        menu_choix_ajouter_supprimer["options"] = ["Créer","Supprimer","Retour","QUITTER"]
        menu_choix_ajouter_supprimer["pays"] = contenu["pays"]
        menu_choix_ajouter_supprimer["actions"] = [(lambda contenu : contenu["individu"].creer_compte(contenu)), (lambda contenu : contenu["individu"].supprimer_compte(contenu)), (lambda var : Ouvert(contenu)), Individu().quitter]
        return Ouvert(menu_choix_ajouter_supprimer)
    
    else:
            print("\nVEUILLEZ D'ABORD VOUS CONNECTER.")
            continuer = input("Appuyez sur entrer pour continuer.")
    
    return Ouvert(contenu)


# FONCTION TEMPORAIRE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def temporaire_function(contenu):                                                                                    #
    print("\nVEUILLEZ D'ABORD VOUS CONNECTER.")                                                                      #
    continuer = input("Appuyez sur entrer pour continuer.")                                                          #
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
        (lambda contenu : indices_taches_permises([0, 1, 2, 7, 8], Data_Scientist())),
        (lambda contenu : indices_taches_permises([0, 1, 3, 4, 7, 8], Geographe())),
        (lambda contenu : indices_taches_permises([0, 1, 2, 3, 5, 6, 7, 8], Admin())),
        Individu().quitter
    ],
    "individu" :
        Individu(),
    "pays" :
        None
},
{
    "question" : 
        "Que voulez vous faire ?",
    "options" : 
    [   
        "Se connecter",
        "Afficher les données d'un pays",
        "Acceder aux résumés statistiques",
        "Décider de valider ou de refuser une correction",
        "Ajouter un pays",
        "Ajouter ou supprimer un pays",
        "Créer ou supprimer un compte",
        "Retourner au menu de choix du statut",
        "QUITTER"
    ],
    "actions" : 
    [
        connection,
        Individu().afficher_pays,
        temporaire_function,
        temporaire_function,
        temporaire_function,
        temporaire_function,
        ajouter_ou_supprimer_compte,
        (lambda contenu : Ouvert(menus[0])),
        Individu().quitter
    ],
    "individu" :
        Individu(),
    "pays" :
        None
}]

