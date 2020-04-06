from acteurs.consultant import Consultant
from menu.menu_ouvert import Ouvert
import pandas
import json
filename = "data.json"
directory_data = "../files/"

class Data_Scientist(Consultant):
    def __init__(self):
        self.est_connecte = False
        self.statut = "d"
        self.contenu_du_menu_initial = {}
        
    def se_connecter(self):
        
        with open("../files/comptes.txt", "r") as comptes:
            liste_des_comptes = []
            tampon = comptes.readlines()
        for s in tampon:
            liste_des_comptes.append(s[:-1]) #Supprime le caractère responsable du retour à la ligne
        n = len(liste_des_comptes)
        liste_des_statuts = [liste_des_comptes[i] for i in range(0, n, 3)]
        liste_des_pseudos = [liste_des_comptes[i] for i in range(1, n, 3)]
        liste_des_mots_de_passe = [liste_des_comptes[i] for i in range(2, n, 3)]
        
        pseudo = input("\nEntrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        
        for i in range(len(liste_des_statuts)):
            if self.statut == liste_des_statuts[i] and pseudo == liste_des_pseudos[i] and mot_de_passe == liste_des_mots_de_passe[i]:
                self.est_connecte = True
                print("\nVous êtes connecté !")
                continuer = input("Appuyez sur entrer pour continuer.")

        if not self.est_connecte:
            print("\nVotre connexion a échouée.")
            continuer = input("Appuyez sur entrer pour continuer.")
            
        return self.est_connecte
    
    def resume_stat(self, contenu):
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        if self.contenu_du_menu_initial == {}:
            self.contenu_du_menu_initial = contenu
        self.contenu_du_menu_initial["chemin de la recherche"] = []
        
        choix_resume = {}
        choix_resume["question"] = "Choisissez une option d'affichage."
        choix_resume["individu"] = contenu["individu"]
        choix_resume["chemin de la recherche"] = []
        choix_resume["options"] = ["Afficher les critères usuels d'un ou plusieurs pays", "Afficher les premiers/derniers pays selon un certain critère", "Afficher les pays dont un critère dépasse un certain seuil", "Afficher le tableau des classes d'âge pour certains pays", "RETOUR AU MENU DE L'ACTEUR", "QUITTER"]
        choix_resume["actions"] = [(lambda var : self.criteres_usuels(contenu)), (lambda var : Ouvert(var)), (lambda var : Ouvert(var)), (lambda var : Ouvert(var)), (lambda var : Ouvert(self.contenu_du_menu_initial)), self.quitter]
        return Ouvert(choix_resume)
    
    def representation_graphique(self, contenu):
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        if self.contenu_du_menu_initial == {}:
            self.contenu_du_menu_initial = contenu
        self.contenu_du_menu_initial["chemin de la recherche"] = []
        
        choix_representaion = {}
        choix_representaion["question"] = "Choisissez le type de graphique."
        choix_representaion["individu"] = contenu["individu"]
        choix_representaion["chemin de la recherche"] = []
        choix_representaion["options"] = ["Diagramme en barres", "Boîte à moustache", "RETOUR AU MENU DE L'ACTEUR", "QUITTER"]
        choix_representaion["actions"] = [(lambda var : Ouvert(var)), (lambda var : Ouvert(var)), (lambda var : Ouvert(self.contenu_du_menu_initial)), self.quitter]
        return Ouvert(choix_representaion)
    
    def criteres_usuels(self, contenu, pays = [], add_pays = False, suppr_pays = False):
        self.contenu_du_menu_initial["chemin de la recherche"] = []
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
            
        def simplification_texte(num_pays,option):
            if option == 0:
                try:
                    txt = donnees[num_pays]['Geography']['Area']['total']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 1:
                try:
                    txt = donnees[num_pays]['People and Society']['Population']['text' ]
                except KeyError:
                    txt = 'NA'
            elif option == 2:
                try:
                    txt = donnees[num_pays]['People and Society']['Population growth rate']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 3:
                try:
                    txt = donnees[num_pays]['Economy']['Inflation rate (consumer prices)']['text']
                except KeyError:
                    txt = 'NA'    
            elif option == 4:
                try:
                    txt = donnees[num_pays]['Economy']['Debt - external']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 5:
                try:
                    txt = donnees[num_pays]['Economy']['Unemployment rate']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 6:
                try:
                    txt = donnees[num_pays]['People and Society']['Health expenditures']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 7:
                try:
                    txt = donnees[num_pays]['People and Society']['Education expenditures']['text']
                except KeyError:
                    txt = 'NA'
            elif option == 8:
                try:
                    txt = donnees[num_pays]['Military and Security']['Military expenditures']['text']
                except KeyError:
                    txt = 'NA'
            
            if not '++' in txt:
                return txt
            indice = 0
            for i in range(len(txt)):
                if txt[i] == '+':
                    if txt[i+1] == '+':
                        return txt[:i-1]
        
        if len(pays) == 0 or add_pays:
            with open("../files/liste_pays_sans_nom.txt", "r") as liste:
                liste_pays_sans_nom0 = liste.readlines()
            liste_pays_sans_nom = []
            for elm in liste_pays_sans_nom0:
                liste_pays_sans_nom.append(int(elm[:-1]))
                
            if len(pays) >= 10 or len(pays) >= len(donnees)-len(liste_pays_sans_nom):
                input("\nVous ne pouvez pas ajouter plus de pays à la table.\nAppuyez sur entrer pour continuer.")
                return self.criteres_usuels(contenu, pays)
            
            choix_pays = {}
            choix_pays["question"] = "Choisissez un pays."
            choix_pays["individu"] = contenu["individu"]
            choix_pays["options"] = []
            choix_pays["actions"] = []
            choix_pays["chemin de la recherche"] = []
                
            for num_pays in range(len(donnees)):
                if num_pays not in liste_pays_sans_nom and num_pays not in pays:
                    nom_pays = donnees[num_pays]['Government']['Country name']['conventional short form']['text']
                    choix_pays["options"].append(nom_pays)
                    choix_pays["actions"].append(lambda var, num_pays=num_pays : self.criteres_usuels(contenu, pays+[num_pays]))
                    
            return Ouvert(choix_pays)
        
        noms_pays = [donnees[num_pays]['Government']['Country name']['conventional short form']['text'] for num_pays in pays]
        
        if suppr_pays:
            if len(pays) == 1:
                input("\nIl doit y avoir au moins un pays dans la table.\nAppuyez sur entrer pour continuer.")
            else :
                choix_pays = {}
                choix_pays["question"] = "Choisissez un pays à retirer de la table."
                choix_pays["individu"] = contenu["individu"]
                choix_pays["options"] = noms_pays
                choix_pays["actions"] = []
                for nom_pays in noms_pays:
                    choix_pays["actions"].append(lambda var, nom_pays=nom_pays : self.criteres_usuels(contenu, pays[:noms_pays.index(nom_pays)]+pays[noms_pays.index(nom_pays)+1:]))

                choix_pays["chemin de la recherche"] = []
                return Ouvert(choix_pays)
        
        menu_affichage = {}
        menu_affichage["individu"] = contenu["individu"]
        menu_affichage["chemin de la recherche"] = []
        
        criteres = ["Superficie", "Population", "Croissance démographique", "Inflation", "Dette", "Taux de chômage", "Taux de dépenses en santé", "Taux de dépenses en éducation", "Taux de dépenses militaires"]
        
        valeurs_pays = [[simplification_texte(num_pays, 0) for num_pays in pays],
                        [simplification_texte(num_pays, 1) for num_pays in pays],
                        [simplification_texte(num_pays, 2) for num_pays in pays],
                        [simplification_texte(num_pays, 3) for num_pays in pays],
                        [simplification_texte(num_pays, 4) for num_pays in pays],
                        [simplification_texte(num_pays, 5) for num_pays in pays],
                        [simplification_texte(num_pays, 6) for num_pays in pays],
                        [simplification_texte(num_pays, 7) for num_pays in pays],
                        [simplification_texte(num_pays, 8) for num_pays in pays]]
        
        menu_affichage["question"] = pandas.DataFrame(valeurs_pays, index = criteres, columns = noms_pays)
        
        menu_affichage["options"] = ["Ajouter un pays à la table", "Retirer un pays de la table", "RETOUR", "RETOUR AU MENU DE L'ACTEUR", "QUITTER"]
        menu_affichage["actions"] = [(lambda var : self.criteres_usuels(var, pays, add_pays=True)),(lambda var : self.criteres_usuels(var, pays, suppr_pays=True)), (lambda var : self.resume_stat(var)), (lambda var : Ouvert(self.contenu_du_menu_initial)), self.quitter]
        
        return Ouvert(menu_affichage)
    
    def top_flop(self,contenu):
        pass
        
        
