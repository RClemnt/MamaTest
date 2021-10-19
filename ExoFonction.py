def condition(nombre) : 

    if nombre == 11 : 

        print("je veux 11")

    elif nombre == 20 : 

        print("je veux 20")

    else : 

        print("je ne sais pas")

    return



def positif (nombre) :
    if nombre > 0 :
        return "positif"
    
    elif nombre == 0 : 
        return "nul"
        
    else : 
        return "negatif"

 

def pair(a) : 

    if a%2 == 0 :
        if positif(a) == "positif" : 

            return "pair et positif"
        elif positif(a) == "nul" :

            return "pair et nul"

        else :

            return "pair et négatif"    
    else :

     return "impair"



def jour(semaine) : 
    if semaine == "Lundi"  : 
        return "c'est reparti"
        
    elif semaine == "Mercredi" : 
         return "jour des enfants"
         
    elif semaine == "Vendredi" : 
        return "bientôt le week-end"
        
    elif semaine == "Samedi" or jour == "Dimanche" : 
        return "bon Week-end" 
        
    else : 
        return "Bonne semaine"



     







