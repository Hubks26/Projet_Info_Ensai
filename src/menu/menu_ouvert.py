
class Ouvert:
    def __init__(self, contenu):
        self.contenu = contenu
        
    def run(self):
        
        if self.contenu["pays"]:
            print("{} : {}\n".format(self.contenu["pays"], self.contenu["question"]))
        else : print("{}\n".format(self.contenu["question"]))
        
        options = self.contenu["options"]
        nb_options = len(options)
        actions = self.contenu["actions"]
        
        for i, opt in enumerate(options):
            print("[{}] {}".format(i+1, opt))
            
        while True:
            choix = input("\n> ")
            try:
                choix = int(choix)
            except ValueError:
                print("\nLa réponse attendue doit être un entier.")
                continue
            if choix <= 0 or choix > nb_options:
                print("\nLa réponse attendue doit être comprise entre 1 et {}.".format(nb_options))
                continue
            break
        return actions[choix-1](self.contenu)
