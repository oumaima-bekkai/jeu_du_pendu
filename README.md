- choisir mot au hasard dans liste de mots
- créer un dico avec chaque lettre du mot en clé et True/False en valeur
- initialiser une liste de lettres déjà essayées à vide
- tant que au-moins un False dans le dico et taille(liste_lettres déjà essayées) < nb_max, Faire
    - boucler sur chaque lettre du mot et afficher un "-" si la lettre correspondante du dico est à False et la lettre elle-même si elle est à True
    - Tant que vrai, faire
        - demander une lettre au joueur
        - si lettre pas dans liste des lettres déjà essayées, ou bien si niveau difficulté (paramètre choisi au départ par le joueur) est à "strict" alors interrompre boucle
    - Fin faire
    - Rajouter lettre choisie dans liste des lettres déjà essayées
    - Si lettre est lettre du dico, alors placer sa valeur à Vrai
- Fin faire
- Ici le jouer a soit gagné, soit perdu

source : https://www.developpez.net/forums/i1520559/autres-langages/python/general-python/jeu-pendu-python/