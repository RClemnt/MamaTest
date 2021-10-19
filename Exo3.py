
list1 = [1,2,3,4]
list2 = [45,34,21,14,98]
list3 = [32,67,78,21,67]



def cal_liste() : 

    b=0

    for a in list1 : 

        b=b+a 

    return b  

print(cal_liste())





def moy_liste() : 
    v=0
    r=len(list2)

    for all_values in list2 : 

        v=v+all_values/r

    return v 



print(moy_liste())



def maximun_list3 (list) : 

    maxi = list[0]

    for i in list3 : 

        if i >= maxi : 

            maxi = i

    return maxi

print(maximun_list3(list3))
print(list3.index(maximun_list3(list3)))



listtext = ("je","suis","bastien","e")

def carac (phrase,caractere) :

    rence = phrase.count(caractere)

    for ocu in phrase : 

        if ocu == caractere : 
            
            return rence


print(carac(listtext,"e"))


def posilist (list) : 

    posi = list[0]

    for x in list :

        if posi == 0 :

            print(x,"est nul ") 

        elif posi < 0 : 

            print(x,"est négatif")

        else : 

            return x,"est positif"


            
print(posilist(list3))














