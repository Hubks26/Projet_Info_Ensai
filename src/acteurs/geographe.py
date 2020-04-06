from acteurs.individu import Individu
from menu.menu_ouvert import Ouvert
import json
filename = "data.json"
directory_data = "../files/"

class Geographe(Individu):
    def __init__(self):
        self.est_connecte = False
        self.statut = "g"
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
                input("Appuyez sur entrer pour continuer.")

        if not self.est_connecte:
            print("\nVotre connexion a échouée.")
            input("Appuyez sur entrer pour continuer.")
            
        return self.est_connecte
    
    def modifier_texte(self, contenu):
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
        else:
            while True:
                modification = input("\nEntrez le nouveau texte :\n> ")
                if len(modification) > 1:
                    break
                print("\nVotre texte doit contenir au moins 1 caractère\n")
            with open(directory_data + filename) as json_file:
                donnees = json.load(json_file)
            chemin = contenu["chemin de la recherche"][1:]
            contenu_section = donnees[chemin[0]]
            for section in chemin[1:]:
                contenu_section = contenu_section[section]
                
            confirmation = input("\nConfirmation de la modification #Cela écrasera le texte initial# (O/N) ?\n> ")
            if confirmation in ["o","O"]:
                contenu_section["text"] = modification # Ici on modifie bien la variable donnees
                with open(directory_data + filename, "w") as json_file:
                    json.dump(donnees, json_file)
                input("\nVotre modification a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
            else :
                input("\nVotre tentative de modification n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                
    def ajout_section(self, contenu, contenu_precedent): # Il doit y avoir un moyen plus simple de faire cette fonction
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        else:
            with open(directory_data + filename) as json_file:
                donnees = json.load(json_file)
            chemin = contenu["chemin de la recherche"][1:]
            contenu_section = donnees[chemin[0]]
            for section in chemin[1:]:
                contenu_section = contenu_section[section]
                
            if len(contenu_section) == 0:
                choix = input("\nVoulez vous ajouter une Section ou un Texte ? (S/T) ?\nAppuyez sur une autre touche si vous voulez ne rien modifier.\n> ")
                if choix in ["s", "S"]:
                    while True:
                        nouvelle_section = input("\nEntrez le nom de la nouvelle section :\n> ")
                        if len(nouvelle_section) <= 1 or len(nouvelle_section) > 50 or "//" in nouvelle_section:
                            print("\nLe nom de la section doit contenir entre 1 et 50 caractères.\nL'usage de // dans un nom de section est interdit")
                            continue
                        if (nouvelle_section == "Government") or (nouvelle_section == "Country name") or (nouvelle_section == "conventional short form") or (nouvelle_section == "conventional long form"):
                            print("\nLa section ne peut pas porter de nom tel que Government, Country name, conventional short form ou conventional long form.")
                            continue
                        break
                    if nouvelle_section in contenu_section.keys() or nouvelle_section in ["AJOUTER OU RENOMMER","RETOUR","QUITTER"]:
                        input("\nCette section existe déjà !\nAppuyez sur entrer pour continuer.")
                        return Ouvert(contenu)
                    confirmation = input("\nConfirmation de la création de la section (O/N) ?\n> ")
                    if confirmation in ["o","O"]:
                        contenu_section[nouvelle_section] = {}
                        with open(directory_data + filename, "w") as json_file:
                            json.dump(donnees, json_file)
                        input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                    else :
                        input("\nVotre tentative d'ajout n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                        return Ouvert(contenu)
                    
                    tampon = contenu["chemin de la recherche"].pop()
                    if len(contenu["chemin de la recherche"]) == 1:
                        contenu["chemin de la recherche"].pop()
                    return self.afficher_section(tampon, contenu_precedent)
                
                elif choix in ["t", "T"]:
                    nouveau_texte = input("\nEntrez le texte à ajouter :\n> ")
                    confirmation = input("\nConfirmation de l'ajout du texte (O/N) ?\n> ")
                    if confirmation in ["o","O"]:
                        contenu_section["text"] = nouveau_texte
                        with open(directory_data + filename, "w") as json_file:
                            json.dump(donnees, json_file)
                        input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                        contenu["chemin de la recherche"].pop()
                    tampon = contenu["chemin de la recherche"].pop()
                    if len(contenu["chemin de la recherche"]) == 1:
                        contenu["chemin de la recherche"].pop()
                    return self.afficher_section(tampon, contenu_precedent)
                else:
                    return Ouvert(contenu)
            else:
                while True:
                    nouvelle_section = input("\nEntrez le nom de la nouvelle section :\n> ")
                    if len(nouvelle_section) <= 1 or len(nouvelle_section) > 50 or "//" in nouvelle_section:
                        print("\nLe nom de la section doit contenir entre 1 et 50 caractères.\nL'usage de // dans un nom de section est interdit")
                        continue
                    if (nouvelle_section == "Government") or (nouvelle_section == "Country name") or (nouvelle_section == "conventional short form") or (nouvelle_section == "conventional long form"):
                        print("\nLa section ne peut pas porter de nom tel que Government, Country name, conventional short form ou conventional long form.")
                        continue
                    break
                if nouvelle_section in contenu_section.keys() or nouvelle_section in ["AJOUTER OU RENOMMER","RETOUR","QUITTER"]:
                    input("\nCette section existe déjà !\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu)
                confirmation = input("\nConfirmation de la création de la section (O/N) ?\n> ")
                if confirmation in ["o","O"]:
                    contenu_section[nouvelle_section] = {}
                    with open(directory_data + filename, "w") as json_file:
                        json.dump(donnees, json_file)
                    input("\nVotre ajout a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                else :
                    input("\nVotre tentative d'ajout n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu)
                
                tampon = contenu["chemin de la recherche"].pop()
                if len(contenu["chemin de la recherche"]) == 1:
                    contenu["chemin de la recherche"].pop()
                return self.afficher_section(tampon, contenu_precedent)
            
    def ajout_pays(self, contenu, contenu_precedent): # Il doit y avoir un moyen plus simple de faire cette fonction. / À Améliorer
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu_precedent)
        else:
            nom_pays = input("\nEntrez le nom du pays à ajouter :\n> ")
            
            if nom_pays == 'none':
                input("\nVous ne pouvez pas nommer un pays 'none'.\nAppyez sur entrer pour continuer.")
                return Ouvert(contenu_precedent)
            
            with open(directory_data + filename) as json_file:
                donnees = json.load(json_file)
            liste_des_pays = []
            
            with open("../files/liste_pays_sans_nom.txt", "r") as liste:
                liste_pays_sans_nom0 = liste.readlines()
            liste_pays_sans_nom = []
            for elm in liste_pays_sans_nom0:
                liste_pays_sans_nom.append(int(elm[:-1]))
                
            for num_pays in range(len(donnees)):
                if num_pays not in liste_pays_sans_nom:
                    liste_des_pays.append(donnees[num_pays]['Government']['Country name']['conventional short form']['text'])
            if nom_pays not in liste_des_pays:
                confirmation = input("\nConfirmation de l'ajout du pays (O/N) ?\n> ")
                if confirmation in ["o","O"]:
                    donnees.append({'Government' : {'Country name' : {'conventional short form' : {'text' : nom_pays}, 'conventional long form' : {'text' : nom_pays}}}})
                    ajout_info = input("\nVoulez vous ajouter des informations de base sur le pays (O/N) ?\n> ")
                    if ajout_info in ["o","O"]:
                        superficie = input("\nEntrez la superficie du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if superficie != "pass":
                            donnees[-1]['Geography'] = {'Area' : {'total' : {'text' : superficie}}}
                            input("\nVotre réponse a bien été enregistrée")
                        population = input("\nEntrez la population du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if population != "pass":
                            donnees[-1]['People and Society'] = {'Population' : {'text' : population}}
                            input("\nVotre réponse a bien été enregistrée")
                        croissance_dem = input("\nEntrez le taux de croissance démographique du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if croissance_dem != "pass":
                            if 'People and Society' in donnees[-1]:
                                donnees[-1]['People and Society']['Population growth rate'] = {'text' : croissance_dem}
                            else:
                                donnees[-1]['People and Society'] = {'Population growth rate' : {'text' : croissance_dem}}
                            input("\nVotre réponse a bien été enregistrée")
                        inflation = input("\nEntrez le taux d'inflation du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if inflation != "pass":
                            donnees[-1]['Economy'] = {'Inflation rate (consumer prices)' : {'text' : inflation}}
                            input("\nVotre réponse a bien été enregistrée")
                        dette = input("\nEntrez la dette du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if dette != "pass":
                            if 'Economy' in donnees[-1]:
                                donnees[-1]['Economy']['Debt - external'] = {'text' : dette}
                            else:
                                donnees[-1]['Economy'] = {'Debt - external' : {'text' : dette}}
                            input("\nVotre réponse a bien été enregistrée")
                        chomage = input("\nEntrez le taux de chômage du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if chomage != "pass":
                            if 'Economy' in donnees[-1]:
                                donnees[-1]['Economy']['Unemployment rate'] = {'text' : chomage}
                            else:
                                donnees[-1]['Economy'] = {'Unemployment rate' : {'text' : chomage}}
                            input("\nVotre réponse a bien été enregistrée")
                        dep_sante = input("\nEntrez le taux de dépense en santé du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if dep_sante != "pass":
                            if 'People and Society' in donnees[-1]:
                                donnees[-1]['People and Society']['Health expenditures'] = {'text' : dep_sante}
                            else:
                                donnees[-1]['People and Society'] = {'Health expenditures' : {'text' : dep_sante}}
                            input("\nVotre réponse a bien été enregistrée")
                        dep_education = input("\nEntrez le taux de dépense en éducation du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if dep_education != "pass":
                            if 'People and Society' in donnees[-1]:
                                donnees[-1]['People and Society']['Education expenditures'] = {'text' : dep_education}
                            else:
                                donnees[-1]['People and Society'] = {'Education expenditures' : {'text' : dep_education}}
                            input("\nVotre réponse a bien été enregistrée")
                        dep_militaires = input("\nEntrez le taux de dépense militaires du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
                        if dep_militaires != "pass":
                            donnees[-1]['Military and Security'] = {'Military expenditures' : {'text' : dep_militaires}}
                            input("\nVotre réponse a bien été enregistrée")
                       
                    with open(directory_data + filename, "w") as json_file:
                        json.dump(donnees, json_file)
                    input("\nVotre nouveau pays a bien été enregistrée.\nAppuyez sur entrer pour continuer.")
                    return self.afficher_pays(contenu)
                else:
                    input("\nVotre tentative d'ajout de pays n'a pas abouti.\nAppuyez sur entrer pour continuer.")
                    return Ouvert(contenu_precedent)
            else:
                input("\nCe pays existe déjà !\nAppuyez sur entrer pour continuer.")
                return Ouvert(contenu_precedent)
            
    def gestion_corrections(self, contenu):
        if not self.est_connecte:
            input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
            return Ouvert(contenu)
        
        if self.contenu_du_menu_initial == {}:
            self.contenu_du_menu_initial = contenu
        
        with open("../files/prop_corrections.txt","r") as fichier:
            tampon1 = fichier.readlines()
        props_et_chemins = []
        for elm in tampon1:
            props_et_chemins.append(elm[:-1])
        n = len(props_et_chemins)
        propositions = [props_et_chemins[i] for i in range(0,n,2)]
        chemins = [props_et_chemins[i].split("//") for i in range(1,n,2)]
        options = []
        for chemin in chemins:
            tampon2 = ""
            for i in range(len(chemin)):
                if i != 1:
                    tampon2 += chemin[i] + "/"
            options.append(tampon2)
        
        choix_prop = {}
        
        if len(options) == 0:
            choix_prop["question"] = "Il n'y a pas de propositions à examiner."
        else:
            choix_prop["question"] = "Choisissez une proposition de correction.\nLe chemin indiqué est celui de l'emplacement du texte suceptible d'être modifié."
        choix_prop["individu"] = contenu["individu"]
        choix_prop["chemin de la recherche"] = []
        choix_prop["options"] = options
        choix_prop["actions"] = []
        
        for i in range(len(options)):
            choix_prop["actions"].append(lambda var, i=i : self.decider_correction(contenu, propositions[i], chemins[i], props_et_chemins, i))
        
        choix_prop["options"].append("RETOUR AU MENU DE L'ACTEUR")
        choix_prop["actions"].append(lambda var : Ouvert(self.contenu_du_menu_initial))
        choix_prop["options"].append("QUITTER")
        choix_prop["actions"].append(Individu().quitter)
        
        return Ouvert(choix_prop)
            
    def decider_correction(self, contenu, proposition, chemin, liste_des_propositions, num_proposition):
        
        with open(directory_data + filename) as json_file:
            donnees = json.load(json_file)
        section_du_texte = donnees[int(chemin[1])]
        for section in chemin[2:]:
            section_du_texte = section_du_texte[section]
        print("\nTexte actuel :\n")
        print(section_du_texte["text"] + "\n")
        print("Proposition de correction :\n")
        print(proposition + "\n")
        while True:
            validation = input("Voulez-vous valider cette proposition de correction (V : valider / R : refuser / P : aucune action) ?\n> ")
            if validation in ["v","V","r","R","p","P"]:
                break
            else :
                input("\nVotre réponse doit être V, R ou P.\nAppyez sur entrer pour continuer.\n")
        if validation in ["v","V"]:
            confirmation = input("\nConfirmation de la validation du nouveau texte (O/N) ? #Cela supprimera l'ancien texte#\n> ")
            if confirmation in ["o","O"]:
                section_du_texte["text"] = proposition
                with open(directory_data + filename, "w") as json_file:
                    json.dump(donnees, json_file)
                nouvelle_liste_des_propositions = []
                for i in range(len(liste_des_propositions)):
                    if i not in [2*num_proposition, 2*num_proposition+1]:
                        nouvelle_liste_des_propositions.append(liste_des_propositions[i])
                with open("../files/prop_corrections.txt","w") as fichier:
                    for line in nouvelle_liste_des_propositions:
                        fichier.write(line+"\n")
                input("\nLe texte a bien été modifié !\nAppuyez sur entrer pour continuer.")
            else :
                input("\nVotre tentative de validation n'a pas abouti.\nAppuyez sur entrer pour continuer.")
        if validation in ["r","R"]:
            confirmation = input("\nConfirmation du refus de la proposition (O/N) ? #Cela supprimera la proposition#\n> ")
            if confirmation in ["o","O"]:
                nouvelle_liste_des_propositions = []
                for i in range(len(liste_des_propositions)):
                    if i not in [2*num_proposition, 2*num_proposition+1]:
                        nouvelle_liste_des_propositions.append(liste_des_propositions[i])
                with open("../files/prop_corrections.txt","w") as fichier:
                    for line in nouvelle_liste_des_propositions:
                        fichier.write(line+"\n")
                input("\nLa proposition a bien été supprimée\nAppuyez sur entrer pour continuer.")
            else :
                input("\nVotre tentative de refus n'a pas abouti.\nAppuyez sur entrer pour continuer.")
        return self.gestion_corrections(contenu)
