class Automobile:
    
    #Attributs par defaut
    compagnie = "inconnue"
    model = "inconnu"
    annee =  0000
    kilometrage = 0.0
    portes = 4
    couleur = "inconnu"
    prix = 0.0
    mode = "automatique"
    
    def __init__(self, comp,model,a,k,p,c,prix,m):
        self.compagnie = comp
        self.model = model 
        self.annee = a   
        self.kilometrage = k
        self.portes = p  
        self.couleur = c  
        self.prix = prix 
        self.mode = m
         
    #A faire methodes pour prochaine video



auto1 = Automobile("Toyota", "Corolla",2003, 25000,4,"blanc", 4000, "automatique" )
auto2 = Automobile("Mazda", "6",2008, 60000,4,"rouge", 9000, "manuel" )

print("Informations de l'auto 1: ")
print(" ")
print("Compagnie:" + auto1.compagnie)
print("model: " + auto1.model)
print("Annee: " , auto1.annee)
print("kilometrage: " , auto1.kilometrage)
print("portes: " ,auto1.portes)
print("Couleur: " + auto1.couleur)
print("prix: " ,auto1.prix)
print("mode: " + auto1.mode)
print(" ")
print("Informations de l'auto 2: ")
print(" ")
print("Compagnie:" + auto2.compagnie )
print("model: " + auto2.model)
print("annee: " ,auto2.annee)
print("kilometrage: " , auto2.kilometrage)
print("portes: " ,auto2.portes)
print("Couleur: " + auto2.couleur)
print("prix: ", auto2.prix)
print("mode: " + auto2.mode)