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

MOTS0=['CHAT','DATE','LUNE','PORC'] #4 lettres 
ESSAIES = len(PENDU0) - 1 

#Variables
#choisir le mot
mot = random.choice(MOTS0)
# _ par lettre du mot choisi 
x = "_" * len(mot) 

# nombre d'essaies incorrects 
faux = 0

#lettres uilisés 
mes_lettres = []

# main loop
print("JEU DU PENDU")
print("------------ ")

while faux < ESSAIES and x != mot :
    print(PENDU0[faux])
    print("lettres utilisées", mes_lettres)
    print(x)

    essai = input("votre choix ? : ")
    # maybe get rid of this by making sure to give instructions to use miniscule letters 
    essai = essai.upper()
    #check if letter was already used 
    while essai in mes_lettres :



