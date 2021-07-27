import random
# j'ai eu l'idée de poser les differents stages d'une potence comme constantes de la vidéo : https://www.youtube.com/watch?v=wmSysRui0cI
#contantes
PENDU0=[''' 
  --------
  |      |
  |
  |
  |
  |
__|     ''',''' 
  --------
  |      |
  |      O
  |
  |
  |
__|     ''','''
  --------
  |      |
  |      O
  |      |
  |
  |
__|    ''',''' 
  --------
  |      |
  |     \O
  |      |
  |
  |
__|     ''','''
 ---------
  |      |
  |     \O/
  |      |
  |
  |
__|      ''',''' 
 --------
  |     |
  |    \O/
  |     |
  |    / 
  |
__|      ''','''
 --------
  |     |
  |    \O/
  |     |
  |    / \
  |
__|         ''']

pendu_1=[''' 
  --------
  |      |
  |
  |
  |
  |
__|     ''',''' 
  --------
  |      |
  |      O
  |
  |
  |
__|     ''','''
  --------
  |      |
  |      O
  |      |
  |
  |
__|    ''',''' 
  --------
  |      |
  |     \O
  |      |
  |
  |
__|     ''','''
 ---------
  |      |
  |     \O/
  |      |
  |
  |
__|      ''',''' 
 --------
  |     |
  |    \O/
  |     |
  |    / 
  |
__|      ''','''
 --------
  |     |
  |    \O/
  |     |
  |    / \
  |
__|         ''']
#choisir le mot
mots_0=['CHAT','DATE','LUNE','PORC'] #4 lettres 
mots_1=['fruit','chien','terre','pomme','table','panda','aigle','singe','faune'] #5 lettres 
mots_2=['loisir','python','minute','maison','bureau','renard','tortue'] #6 lettres 
mots_3=['miracle','bonjour','horloge','boisson','fromage','abeille','serpent'] #7 lettres 
mots_4=['portable','courrier','synonyme','attentif','mouchoir','abstract','adorable'] #8 lettres 
mots_5=['ABDOMINAL','adoration','crocodile','alimenter','allemande','angelique','ascenseur'] #9 lettres 

def niveau_0(values):
    mot = random.choice(mots_0)
    print("  -------- " )
    print("  |     |  " )
    print("  |    {}".format(values[0]))
    print("  |  {}{}{}".format(values[1], values[2], values[3]))
    print("  |   {}{}".format(values[4], values[5]))
    print("__|        " ) 
def niveau_1():
    mot = random.choice(mots_1)
def niveau_2():
    mot = random.choice(mots_2)
def niveau_3():
    mot = random.choice(mots_3)
def niveau_4():
    mot = random.choice(mots_4)
def niveau_5():
    mot = random.choice(mots_5)     

lettres = []
#Introduction
print("JEU DU PENDU")
print("------------ ")

#

#Choix de difficulté
#https://www.daniweb.com/programming/software-development/threads/463762/python-guessing-game-changing-difficulty
difficulté=int(input('Choisissez votre difficulté: de 0 (facile) à 5 (difficile)'))
#https://www.daniweb.com/programming/software-development/threads/442157/guessing-generator-with-difficulty-levels#post1903074
if difficulté == 0:
    top = 100
    tries = 3
elif difficulté == 1:
    top = 500
    tries = 6
elif difficulté == 2:
    top = 500
    tries = 6
elif difficulté == 3:
    top = 500
    tries = 6
elif difficulté == 4:
    top = 500
    tries = 6
elif difficulté == 5:
    top = 500
    tries = 6
else:
    print("Votre choix doit être compris entre 0 et 5. Faites un autre choix.")

try:

        level_choice = int(input())   

except ValueError:

        print("Wrong Input! Try Again\n")


#https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
def main():
    play(mot)
    while input("Un nouveau tour ? (O/X) ") == "O":
        play(mot)


if __name__ == "__main__":
    main()
