import random
import time

print("Bienvenue sur DevineLeNombre!")
print("Trouve le chiffre entre 1 et 100")

numb = random.randint(1, 100)
typed = int(input())

while typed != numb:

    if typed < numb:
        print("Le nombre est plus grand!")
    elif typed > numb:
        print("Le nombre est plus petit!")
    
    typed = int(input())

print("Bravo vous avez trouvé le chiffre!")
print("Le programme se ferme dans 5 secondes...")
time.sleep(5)