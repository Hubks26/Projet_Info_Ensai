from acteurs.consultant import Consultant
from menu.menu_ouvert import Ouvert

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
        "Quitter"
    ],
    "action_options": 
    [
        (lambda contenu : indices_taches_permises([2, 3, 9, 10])),
        (lambda contenu : Ouvert(menus[1])),
        (lambda contenu : Ouvert(menus[1])),
        (lambda contenu : Ouvert(menus[1])),
        Consultant().quitter
    ]
},
{
    "question" : 
        "Que voulez vous faire ?",
    "options" : 
    [   
        "Se connecter",
        "Se déconnecter",
        "Afficher les données d'un pays",
        "Proposer une correction",
        "Acceder aux résumés statistiques",
        "Décider de valider ou de refuser une correction",
        "Ajouter ou modifier un pays",
        "Supprimer un pays",
        "Créer ou Supprimer un compte",
        "Retourner au menu de choix du statut",
        "Quitter"
    ],
    "action_options": 
    [
        'fonction0',
        'fonction1',
        Consultant().afficher_pays,
        'fonction2',
        'fonction3',
        'fonction4',
        'fonction5',
        'fonction6',
        'fonction7',
        'fonction8',
        Consultant().quitter
    ]
}]

def indices_taches_permises(indices_taches):
        
    menu_acteur = {}
    menu_acteur["question"] = menus[1]["question"]
    menu_acteur["options"] = [menus[1]["options"][i] for i in indices_taches]
    menu_acteur["action_options"] = [menus[1]["action_options"][i] for i in indices_taches]
        
    return Ouvert(menu_acteur)
