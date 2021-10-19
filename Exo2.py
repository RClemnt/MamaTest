# Nom=input ("saisir son nom :")

# print ("Bonjour "+ Nom)


# Age=input("saisir année de naissance :")

# print(2021-int(Age))


# semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

# print(semaine)

# print(semaine[4])

# semaine[0]="dimanche"

# semaine[6]="lundi"

# print(semaine)






# stockmateriel=["Ordinateur de bureau", "Ordinateur portable", "Caméra","Haut-parleurs", "Télévision", "Cartes mères", "souris", "clavier","barrettes de mémoire",]
# #faire une autre fonction afin de pouvoir ajouter le valeur à enlever a une liste on peut ensuite faire del liste[x] et ensuite ajoute avec liste2.reverse(liste[x])
# stockmateriel.sort(key=str.lower)
# print(stockmateriel)
# stocknbr=[100,310.28, 27.00, 1000,500]

# print(len(stockmateriel))

# print(len(stocknbr))


# stocknbr.sort()

# print(stocknbr)


# numList = [1,2,3,4,5] 

# alphaList = ["a","b","c","d","e"] 

# print(numList)

# print(alphaList)

# print(numList is alphaList) 

# print(numList == alphaList) 



# liste = [17, 38, 10, 25, 72]


# liste.sort()
# print(liste)

# liste.append(12)
# print(liste)

# liste.reverse()
# print(liste)

# print(liste.index(17))

# del liste[2]
# print(liste)

# print(liste[1],liste[2])

# print(liste[:2])

# print(liste[-3:])

# print(liste[-1])

# dictionnaire = {"prénom":"quentin","nom":"dijoux"}

# print(dictionnaire)

# print(type(dictionnaire))

# dictionnaire["age"] = 45

# print(dictionnaire.get("age"))

# print(dictionnaire)

# del dictionnaire["nom"]

# dictionnaire["nom"] = "Wayne"

# print(dictionnaire)


# def indique_nom() :
#     return "Bruce"

# print(indique_nom())

# a=5 
# def indique_age() : 
#     return


# tu=0
# w=5

# try :
#     x=(w/tu)

# except : 
#     print(tu)


d = {"nom":"Dupuis", "prénom" : "Jacque", "Age" : 30}

print(d)



d["prénom"] = "Jacques"

for key in d.keys() : 
    print(key)

for valeur in d.values() : 
    print(valeur)

for key, valeur in d.items() : 
    print(key,valeur)


print(d["prénom"], d["nom"], "a", d["Age"], "ans")















