
class Ouvert:
    def __init__(self, contenu):
        self.contenu = contenu
        
    def run(self):
        print(self.contenu["question"])
        print('\n')
        
        options = self.contenu["options"]
        nb_options = len(options)
        options_action =self.contenu["action_options"]
        
        for i, opt in enumerate(options):
            print("[{}] {}".format(i+1, opt))
            
        while True:
            choice = input("> ")
            print(choice)
            try:
                choice = int(choice)
            except ValueError:
                print("La réponse attendue doit être un entier")
                continue
            if choice <= 0 or choice > nb_options:
                print("La réponse attendue doit être comprise entre 1 et {}".format(nb_options))
                continue
            break
        return options_action[choice-1](self.contenu)
