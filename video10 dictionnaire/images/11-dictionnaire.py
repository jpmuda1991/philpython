athlete = {
    "nom": "Daniels" ,
    "prenom": "John",
    "sport":  "Tennis",
    "pays": "Angleterre",
    "Date de naissance": "1990-01-29",
    "taille(cm)": "181",
    "poids(L)":   "175",
    "Nmbre_trophee" : "15"
        
}

#Imprimer tout le dictionnaire
print(athlete)
print("_ _ _ _ _ _ _")
print("nom:" + athlete["nom"])
print("prenom:" + athlete["prenom"])
print("sport:" + athlete["prenom"])
print("pays:" + athlete["pays"])
print("date de naiss:" + athlete["Date de naissance"])
print("taille:" + athlete["taille(cm)"])
print("poids:" + athlete["poids(L)"])
print("nombre de trophée:" + athlete["Nmbre_trophee"])

#Trouver la longueur d'un dictionnaire
print("_ _ _ _ _ _ _")
print("Il y a " + str(len(athlete)) + " elements dans ce dictionnaire")
print("_ _ _ _")
print(" ")
# Mettre les retour de fonctions dans des variables

nomdictionnaire = athlete["nom"]
prenomdictionnaire = athlete["prenom"]
sportdictionnaire = athlete["sport"]

print("nom: " + nomdictionnaire + " prenom: " + prenomdictionnaire + " sport: " + sportdictionnaire )

print("_ _ _ _")
print(" ")
print("la fonction get ")

sportathlete = athlete.get("sport")
tailleathlete = athlete.get("taille(cm)")

print("son sport est " + sportathlete + " et sa taille est " + tailleathlete )

print("_ _ _ _")
print(" ")

#Voir la liste de tout les clés d'un dictionnaire

allkeys = athlete.keys()

print("La liste de tout les clés " + str(allkeys))


print("_ _ _ _")
print(" ")

#Voir la liste de tout les valeurs d'un dictionnaire

allelements = athlete.values()

print(allelements)

print("_ _ _ _")
print(" ")

#Voir la liste des clés et des élements en meme temps

paire = athlete.items()

print(paire)