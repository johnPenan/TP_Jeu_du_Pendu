

import random

liste_des_mots  = ["Republic","Antilles","MadameCe","Monsieur","GuineeGN","FranceFR","Celestin","Nathalie","Alphonse"]

mot_au_hasard = random.choice(liste_des_mots)

print(mot_au_hasard)


lettres_trouvees = []

erreurs = 0
letter = ""


while erreurs < 8:

    lettres = input("Proposez une lettre composant le mot: ").strip()
    
    while len(lettres) != 1:
        lettres = input("Proposez une nouvelle lettre: ").strip()
           

    lettres_trouvees.append(lettres)

    
    for lettre in mot_au_hasard:
        
        if (lettre.lower() in lettres_trouvees or lettre.upper() in lettres_trouvees):
                print(lettre, end ='')
        else:
            print("*", end = '')

    if lettres not in mot_au_hasard:
        erreurs += 1

    
point = 8 - erreurs
print("Vous avez un score de: ", point)
        


           

    
       
    
   

 