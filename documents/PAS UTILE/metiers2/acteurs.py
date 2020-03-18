"""Ici les classes définissant les acteurs"""

#A FAIRE : DEFINIR UN SYSTEME DE NOTATION PROPRE (VOIR LA VIDEO ENVOYE PAR LES PROFS SUR COMMENT APPELER NOS VARS)

import json
import cor
filename = "factbook-country-profiles.json"
directory_data = "../files/"
with open(directory_data + filename) as json_file:
    donnees = json.load(json_file)

class Consultant:
    
    def __init__(self):
        pass
    
    def afficher_pays(self, i): # Ici j'imagine qu'afficher un pays c'est afficher sa carte, mais on verra ça quand on fera la partie graphique, en attendant j'affiche juste son nom. On remarque qu'il est possible que cela retourne une erreur si donnees ne contient pas le nom du pays (Il faudra régler ce problème plus tard)
        Nom_Pays = donnees[i]['Government']['Country name']['conventional short form']['text']
        return Nom_Pays
    
    def proposer_correction(self, contenu):
        return prop.Correction(contenu)
    
class Data_Scientist(Consultant):
    
    def __init__(self, id_compte, pseudo, password): # Problème de clé primaire à corriger
        self.id_compte = id_compte
        self.pseudo = pseudo
        self.password = password
        self.is_connected = False
        
    def connexion(self, pseudo, password):
        if pseudo == self.pseudo and password == self.password:
            self.is_connected = True
    
    def deconnexion(self):
        self.is_connected = False
        
    def resume(self, i): # Faire ça plus proprement au niveau de l'affichage
        if self.is_connected:
            print(donnees[i]['Government']['Country name']['conventional short form']['text'])
            print(donnees[i]['Geography']['Area']['total']['text'])
            print(donnees[i]['People and Society']['Population']['text'])
            print(donnees[i]['People and Society']['Population growth rate']['text'])
            print(donnees[i]['Economy']['Inflation rate (consumer prices)']['text'])
            print(donnees[i]['Economy']['Debt - external']['text'])
            print(donnees[i]['Economy']['Unemployment rate']['text'])
            print(donnees[i]['People and Society']['Health expenditures']['text'])
            print(donnees[i]['People and Society']['Education expenditures']['text'])
            print(donnees[i]['Military and Security']['Military expenditures']['text'])
            print(donnees[i]['People and Society']['Age structure'])
        else:
            print("Veuillez d'abord vous connecter")

class Geographe: # C'est pas un peu con qu'un géographe n'ait pas le droit de proposer une correction ??? Je pense qu'à terme on en fera une classe fille de Consultant.
    
    def __init__(self, id_compte, pseudo, password):
        self.id_compte = id_compte
        self.pseudo = pseudo
        self.password = password
        self.is_connected = False
        
    def connexion(self, pseudo, password):
        if pseudo == self.pseudo and password == self.password:
            self.is_connected = True
    
    def deconnexion(self):
        self.is_connected = False
        
    def decider_cor(self, cor, is_accepted):
        if self.is_connected:
            self.is_ok == is_accepted
        else: print("Veuillez d'abord vous connecter")
        
    def ajouter_pays(self, Nom_Pays): # Peut-être devrions-nous faire une class pays ?
        if self.is_connected:
            donnees.append({'Government' : {'Country name' : {'conventional short form' : {'text' : Nom_Pays}}}})
        else: print("Veuillez d'abord vous connecter")
        
class Admin(Geographe):
    
    def supprimer_pays(self, id_pays): # Demander confirmation pour supprimer un pays.
        if self.is_connected:
            del(donnees[id_pays])
        else: print("Veuillez d'abord vous connecter")
            
    def supprimer_compte(self, id_compte): # A finir
        pass
    
    def resume(self, i): # Faire ça plus proprement au niveau de l'affichage  OUI c'est du copié collé mais tant pis.
        if self.is_connected:
            print(donnees[i]['Government']['Country name']['conventional short form']['text'])
            print(donnees[i]['Geography']['Area']['total']['text'])
            print(donnees[i]['People and Society']['Population']['text'])
            print(donnees[i]['People and Society']['Population growth rate']['text'])
            print(donnees[i]['Economy']['Inflation rate (consumer prices)']['text'])
            print(donnees[i]['Economy']['Debt - external']['text'])
            print(donnees[i]['Economy']['Unemployment rate']['text'])
            print(donnees[i]['People and Society']['Health expenditures']['text'])
            print(donnees[i]['People and Society']['Education expenditures']['text'])
            print(donnees[i]['Military and Security']['Military expenditures']['text'])
            print(donnees[i]['People and Society']['Age structure'])
        else:
            print("Veuillez d'abord vous connecter")
