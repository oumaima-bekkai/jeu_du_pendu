import random
#choisir le mot
mots = ['chat', 'fruit', 'miracle', 'loisir','minute', 'chien','table', 'bonjour', 'terre', 'python', 'pomme', 'maison','bureau','portable','horloge','boisson','fromage' ]
mot = random.choice(mots)

#mot = print (random.choice(mots)) 
#lettres=list(mot)
#lettres = (mot.split(' ')).split(' ')
#print (lettres)
#letter=random.choice(mot)

#https://stackoverflow.com/questions/33904021/python-random-letter-from-specific-word
# take input for the word of player 1
target = input('Player 1 word: ')

# set guess to empty, but same length as 'target'
guess = '_'*len(target)
tries = 0

while (guess != target) and (tries < 3):
    # take input of player 2
    s = input('Now: "' + guess + '"; Player 2 can guess: ')

    # if guessed input is longer than 1 character, skip it
    if len(s) > 1:
        print('only 1 character allowed at a time')
        continue 

    # update guess with guessed letter if it hits
    guess = ''.join(s if target[i] == s else guess[i] for i in range(len(target)))

    # test if there were any correct guesses, otherwise tries += 1
    if not any(target[i] == s for i in range(len(target))):
        tries+=1

# print result after exiting loop
print('Player {} WINS: word was {}'.format('2' if tries < 2 else '1', target))


