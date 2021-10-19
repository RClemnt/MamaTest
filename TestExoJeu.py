print("Venez découvrir votre destin !")

nom = input("quel est votre nom :")
print("bonjour! ",nom)

age = 2021 - int(input("Votre année de naissance :"))
print("Vous avez ",age, "ans beau gosse !")

if age < 24 : 
    print("vous êtes encore jeune c'est bien vous avez encore du temp avant de crever")

elif age >= 24 and age <= 30  : 
    print("Vous commencez à veillir faites gaffe quand même")

elif age > 30 and age <= 50 : 
    print("Vous êtes vieux mais pas totalement on peut encore vous sauvez")

elif age > 50 and age <= 70 :
    print("Vous êtes vraiment vieux ça commence à être chaud pour vous ! ")

else : 
    print("Vous voulez vraiment connaitre votre avenir ?")


print ("pour connaitre vôtre avenir répondez à cette dernière question !")
print ("répondez en charactère minuscule c'est plus simple pour la divination.")
signe = input ("De quel signe astrologique êtes-vous ? :")



if signe == "poisson" : 
    print("Franchement la je préfère pas vous dire ce qu'il va arriver. Désolé.")

elif signe == "sagittaire" : 
    print("Vous allez très probablement déceder dans les prochaines heures d'une chutte de pierre!(Eviter la montagne) ")

elif signe == "capricorne" : 
    print("Vous serez couvert de gloire et d'argent mais seulement si vous partez vivre à concarneau")

elif signe == "cancer" : 
    print("L'amour de vôtre vie vous attend demain à auchan si vous pensez déjà l'avoir trouvé vous avez tord")

elif signe == "lion" : 
    print("Ne partez plus en vacance il va vous arrivez des bricoles ! (faites moi confaince")

elif signe == "scorpion" : 
    print("Vôtre prochain anniversaire sera surement le dernier vous serez tué par le tueur d'anniversaire")

elif signe == "taureau" : 
    print("Vous êtes déjà très heureux vous faites ce test juste pour vous amusez avoué le !")

elif signe == "verseau" : 
    print("Pourquoi avoir fait affaire avec la mafia italienne vous êtes fou !!!")

elif signe == "balance" : 
    print("Vous êtes évidemment le plus beau du monde je n'ai même pas besoin de la préciser")

elif signe == "vierge" : 
    print ("Vos enfants vont rater leur études à cause de vôtre éducation pitoyable ! Bravo !")

elif signe == "bélier" : 
    print ("Vôtre ex va vous rappelez demain et si vous n'avez pas d'ex ce sera l'ex de quelqu'un d'autre qui vous appelera. Peut-être une belle rencontre !")

elif signe == "gémeaux" : 
    print("Arrétez tout de suite ce que vous êtes entrain de faire et partez faire des courses le frigo est vide")

else : 
    print("Vous me prenez pour un con ou vous ne savez pas lire ce qu'on vous demande ", nom)

print("Ce test vous a ravi ",nom,"?")
