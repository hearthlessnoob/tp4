#importer un module
import random

#fonction pour deemander les bornes du joueur et choisir un nb random entre les bornes, input: integer, ouput: integer
def new_nb():
    range_min = int(input("Qu'elle est le borne minimum:"))
    range_max = int(input("Qu'elle est le borne maximum:"))
    nb = random.randint(range_min, range_max)
    print("J’ai choisi un nombre au hasard entre %d et %d."%(range_min, range_max))
    print("À vous de le deviner...")
    print(nb)
    return nb
nb = new_nb()
nb_tries = 0
replay = True
#main loop pour que le joueur peut jouer plusieurs fois
while replay:
   guess = int(input("Entrez votre essai : "))
   nb_tries += 1
   #regarder si le nb que le joueur a entré est trop grand, trop petit ou si il a deviné le bon nb
   if guess == nb:
       print("Bravo! Bonne réponse.")
       print("Vous avez réussi en : %d essai(s)." % nb_tries)
       replay = input("Voulez-vous faire une autre partie (o/n) ? ")
       #demander si le joueur veut rejouer ou non
       if replay.lower() == "o":
           nb = new_nb()
           nb_tries = 0
       else:
           replay = False
   elif guess > nb:
       print("Mauvais choix, le nombre est plus petit que %d." % guess)
   else:
       print("Mauvais choix, le nombre est plus grand que %d." % guess)
print("Merci et au revoir...")
