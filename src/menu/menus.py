from acteurs.consultant import Consultant, Individu, Ouvert

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
        (lambda contenu : Ouvert(menus[1])),
        'fonction1()',
        'fonction2()',
        'fonction3()',
        Individu().quitter
    ]
},
{
    "question" : 
        "Que voulez vous faire ?",
    "options" : 
    [
        "Afficher les données d'un pays", 
        "Quitter"
    ],
    "action_options": 
    [
        Consultant().afficher_pays,
        Consultant().quitter
    ]
}]
    
