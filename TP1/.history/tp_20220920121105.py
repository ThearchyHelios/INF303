############################################################################
### TP1 - Prise en main de Caseine, Récursion, Énumération, Backtracking ###
############################################################################

"""
Les fonctions dont la documentation contient OBLIGATOIRE sont nécessaires pour
avoir le point du TP.  Les exemples donnés servent aussi de tests unitaires si
le fichier est exécuté.

Comment faire les TP :
* Téléchargez et décompressez l'archive du TP.
* Ouvrez le fichier « tp.py » dans votre éditeur de texte favori.
* Complétez une par une les fonctions entre les lignes « ### À COMPLÉTER DÉBUT » (0 ligne(s))

et « ### À COMPLÉTER FIN »
* Lorsque vous pensez avoir terminé une fonction, exécutez le fichier sur votre
machine et vérifiez que les tests unitaires passent. Si ce n'est pas le cas,
corrigez votre fonction.
* Lorsque les tests unitaires passent pour une fonction, faites un
copier-coller du fichier complet sur Caseine dans l'onglet "Edit", sauvegardez
et vérifiez que cela fonctionne sur Caseine avec le bouton "Evaluate".


Attention : les tests fournis ne peuvent être exhaustifs. Qu'une fonction passe
tous les tests ne garantit pas qu'elle soit correcte. Gardez cela en tête
lorsque vous réutilisez vos fonctions dans d'autres fonctions.

---

Pour certaines fonctions, plusieurs implémentations sont possibles :
récursive, itérative ou explicite. Vous n'avez besoin d'en implémenter qu'une.
"""

##############
### Sommes ###
##############


from symbol import return_stmt


def somme_entiers(n):
    """Calcule et renvoie la somme des entiers de 0 à n.

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param n: Un entier naturel

            :Example:

            >>> somme_entiers(0)
            0
            >>> somme_entiers(1)
            1
            >>> somme_entiers(3)
            6
            >>> somme_entiers(4)
            10
            >>> somme_entiers(10)
            55

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # if n <= 0:
    #     return 0
    # else:
    #     for i in range(n):
    #         return n + somme_entiers(n-1)
    # À COMPLÉTER FIN
    # OK

    # Itératif
    # À COMPLÉTER DÉBUT (4 ligne(s))

    return_value_somme_entier_interatif = 0
    for i in range(n+1):
        return_value_somme_entier_interatif += i
    return return_value_somme_entier_interatif
    # OK

    # À COMPLÉTER FIN

    # Explicite
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # TODO: à compléter

    # À COMPLÉTER FIN


def somme_impairs(n):
    """Calcule et renvoie la somme des entiers impairs de 0 à n.

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param n: Un entier naturel

            :Example:

            >>> somme_impairs(0)
            0
            >>> somme_impairs(1)
            1
            >>> somme_impairs(2)
            1
            >>> somme_impairs(3)
            4
            >>> somme_impairs(4)
            4
            >>> somme_impairs(5)
            9

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))
    # TODO: A verifier si il est une fonction recursive

    # if n == 0:
    #     return 0
    # for i in range(n):
    #     if n % 2 == 0:
    #         return 0 + somme_impairs(n-1)
    #     else:
    #         return n + somme_impairs(n-1)
    # OK

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (4 ligne(s))

    if n == 0:
        return 0
    else:
        return_value_somme_impairs_interatif = 0
        for i in range(n+1):
            if i % 2 != 0:
                return_value_somme_impairs_interatif += i
        return return_value_somme_impairs_interatif
    # OK

    # À COMPLÉTER FIN

    # Explicite
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # TODO: A completer

    # À COMPLÉTER FIN


def somme_carres(n):
    """Calcule et renvoie la somme de tous les carrés des entiers de 0 à n.

            :param n: Un entier naturel

            :Example:

            >>> somme_carres(0)
            0
            >>> somme_carres(1)
            1
            >>> somme_carres(2)
            5
            >>> somme_carres(3)
            14
            >>> somme_carres(5)
            55

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # if n == 0:
    #     return 0
    # else:
    #     for i in range(n):
    #         return n**2 + somme_carres(n-1)
    # OK

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (4 ligne(s))

    return_value_somme_carres_interatif = 0
    for i in range(n+1):
        return_value_somme_carres_interatif += i**2
    return return_value_somme_carres_interatif
    # OK

    # À COMPLÉTER FIN

    # Explicite
    # À COMPLÉTER DÉBUT (1 ligne(s))

    #TODO: A completer

    # À COMPLÉTER FIN

    ###################################
    ### Autres fonctions récursives ###
    ###################################


def factorielle(n):
    """Retourne n!

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: Un entier naturel

        :Example:

        >>> factorielle(0)
        1
        >>> factorielle(1)
        1
        >>> factorielle(2)
        2
        >>> factorielle(3)
        6
        >>> factorielle(5)
        120

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))

    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (4 ligne(s))

    # À COMPLÉTER FIN


def binome(k, n):
    """Retourne k parmi n.

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param k: Un entier naturel
            :param n: Un entier naturel

            :Example:

            >>> binome(3,5)
            10
            >>> binome(4,6)
            15

            >>> binome(0,0)
            1

            >>> binome(1,0)
            0
            >>> binome(2,1)
            0
            >>> binome(100,10)
            0

            >>> binome(1,1)
            1
            >>> binome(1,2)
            2
            >>> binome(1,10)
            10

    """

    # Aide :
    # >>> 12 /  4  # division flottante
    # 3.0
    # >>> 12 // 4  # division euclidienne
    # 3

    # Explicite
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN

    # Récursif
    # À COMPLÉTER DÉBUT (8 ligne(s))

    # À COMPLÉTER FIN


def fibonacci(n):
    """Calcule et renvoie la valeur du nieme terme de la suite de Fibonacci.

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param n: Un entier naturel

            :Example:

            >>> fibonacci(0)
            0
            >>> fibonacci(1)
            1
            >>> fibonacci(2)
            1
            >>> fibonacci(3)
            2
            >>> fibonacci(4)
            3
            >>> fibonacci(5)
            5
            >>> fibonacci(6)
            8

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (6 ligne(s))

    # À COMPLÉTER FIN

    # Explicite
    # À COMPLÉTER DÉBUT (4 ligne(s))

    # À COMPLÉTER FIN


def pgcd(a, b):
    """Renvoie le PGCD de a et b.

            :param a: Un entier naturel
            :param b: Un entier naturel

            >>> pgcd(12, 18)
            6
            >>> pgcd(51, 13)
            1
            >>> pgcd(39, 65)
            13

    """

    # Récursif
    # À COMPLÉTER DÉBUT (3 ligne(s))

    # À COMPLÉTER FIN


def syracuse_temps_vol(n):
    """Renvoie le plus petit k tel que u_k = 1.

            La suite u est défini ainsi :
            u_0 = n
            u_{k+1} = u_k / 2    si u_k pair
                              3*u_k + 1  si u_k impair

            :param n: Un entier naturel

            :Example:

            >>> syracuse_temps_vol(1)
            0
            >>> syracuse_temps_vol(15)
            17
            >>> syracuse_temps_vol(127)
            46

    """

    # Récursif
    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (5 ligne(s))

    # À COMPLÉTER FIN


def tours_de_hanoi(n):
    """Affiche la liste des mouvements à effectuer pour déplacer une pile de n
    disque de la tour 0 à la tour 2 en utilisant la tour 1 avec le nombre
    minimum de mouvements.

            Les règles à respecter sont :
            * on ne peut déplacer plus d'un disque à la fois ;
            * on ne peut placer un disque que sur un autre disque plus grand que
            lui ou sur un emplacement vide.

            :param n: Un entier naturel non nul

            :Example:

            >>> tours_de_hanoi(1)
            [[1], [], []]
            DISQUE 1 : 0 -> 2 [[], [], [1]]
            >>> tours_de_hanoi(2)
            [[2, 1], [], []]
            DISQUE 1 : 0 -> 1 [[2], [1], []]
            DISQUE 2 : 0 -> 2 [[], [1], [2]]
            DISQUE 1 : 1 -> 2 [[], [], [2, 1]]
            >>> tours_de_hanoi(3)
            [[3, 2, 1], [], []]
            DISQUE 1 : 0 -> 2 [[3, 2], [], [1]]
            DISQUE 2 : 0 -> 1 [[3], [2], [1]]
            DISQUE 1 : 2 -> 1 [[3], [2, 1], []]
            DISQUE 3 : 0 -> 2 [[], [2, 1], [3]]
            DISQUE 1 : 1 -> 0 [[1], [2], [3]]
            DISQUE 2 : 1 -> 2 [[1], [], [3, 2]]
            DISQUE 1 : 0 -> 2 [[], [], [3, 2, 1]]

    """

    def deplacer(jeu, depart, arriv):
        """Déplace le disque au dessus de la tour depart au dessus de la tour
        arriv.

                La fonction vérifie si le déplacement est valide et affiche un
                message d'erreur si ce n'est pas le cas.

        """

        if len(jeu[depart]) == 0:
            print("ERREUR, PAS DE DISQUE SUR LA TOUR", depart)
            print(jeu)
        disque = jeu[depart][-1]
        if len(jeu[arriv]) > 0 and jeu[arriv][-1] < disque:
            print("ERREUR, LE DISUQE", disque,
                  "NE PEUT PAS ÊTRE POSÉ SUR LE DISQUE", jeu[arriv][-1])
            print(jeu)
        jeu[arriv].append(jeu[depart].pop())
        print("DISQUE", disque, ":", depart, "->", arriv, jeu)

    def tours_de_hanoi_rec(jeu, disque_max, depart, inter, arriv):
        """Déplace les disques 1 à disque_max de la tour depart à la tour arriv
        en utilisant le tour inter.

                Utilise la fonction 'deplacer' pour effectuer le déplacement d'un
                disque.

                :param jeu: liste de 3 listes représentant l'état des 3 tours du jeu.

        """

        # À COMPLÉTER DÉBUT (6 ligne(s))

        # À COMPLÉTER FIN

    jeu = [[n-i for i in range(n)], [], []]
    print(jeu)
    tours_de_hanoi_rec(jeu, n, 0, 1, 2)


"""
tours_de_hanoi(7)
quit()
"""


######################
### Sous-ensembles ###
######################

def sousens_nonord_2(n):
    """Affiche la liste de tous les sous-ensembles non ordonnés à 2
    éléments de {1 à n} et renvoie le nombre de sous-ensembles affichés

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param n: Un entier naturel non nul

            :Example:

            >>> sousens_nonord_2(1)
            0
            >>> sousens_nonord_2(2)
            {1,2}
            1
            >>> sousens_nonord_2(3)
            {1,2}
            {1,3}
            {2,3}
            3
            >>> sousens_nonord_2(4)
            {1,2}
            {1,3}
            {1,4}
            {2,3}
            {2,4}
            {3,4}
            6
    """

    # Aide : vous pourriez avoir besoin d'utiliser le paramètre "sep" de la
    # fonction "print" :
    # >>> print(1, 2)
    # 1 2
    # >>> print(1, 2, sep="")
    # 12

    # À COMPLÉTER DÉBUT (6 ligne(s))

    # À COMPLÉTER FIN


def sousens_ord_2(n):
    """Affiche la liste de tous les sous-ensembles ordonnés à 2
    éléments de {1 à n} et renvoie le nombre de sous-ensembles affichés

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param n: Un entier naturel non nul

            :Example:

            >>> sousens_ord_2(1)
            0
            >>> sousens_ord_2(2)
            {1,2}
            {2,1}
            2
            >>> sousens_ord_2(3)
            {1,2}
            {1,3}
            {2,1}
            {2,3}
            {3,1}
            {3,2}
            6
    """

    # À COMPLÉTER DÉBUT (7 ligne(s))

    # À COMPLÉTER FIN


def sousens_nonord_3(n):
    """Affiche la liste de tous les sous-ensembles non ordonnés à 3
    éléments de {1 à n} et renvoie le nombre de sous-ensembles affichés.

            :param n: Un entier naturel non nul

            :Example:

            >>> sousens_nonord_3(1)
            0
            >>> sousens_nonord_3(2)
            0
            >>> sousens_nonord_3(3)
            {1,2,3}
            1
            >>> sousens_nonord_3(4)
            {1,2,3}
            {1,2,4}
            {1,3,4}
            {2,3,4}
            4
            >>> sousens_nonord_3(5)
            {1,2,3}
            {1,2,4}
            {1,2,5}
            {1,3,4}
            {1,3,5}
            {1,4,5}
            {2,3,4}
            {2,3,5}
            {2,4,5}
            {3,4,5}
            10
    """

    # À COMPLÉTER DÉBUT (7 ligne(s))

    # À COMPLÉTER FIN


def sousens_ord_3(n):
    """Affiche la liste de tous les sous-ensembles ordonnés à 3
    éléments de {1 à n} et renvoie le nombre de sous-ensembles affichés.

            :param n: Un entier naturel non nul

            :Example:

            >>> sousens_ord_3(1)
            0
            >>> sousens_ord_3(2)
            0
            >>> sousens_ord_3(3)
            {1,2,3}
            {1,3,2}
            {2,1,3}
            {2,3,1}
            {3,1,2}
            {3,2,1}
            6
    """

    # À COMPLÉTER DÉBUT (11 ligne(s))

    # À COMPLÉTER FIN


def sousens_nonord_k(k, n):
    """Affiche la liste de tous les sous-ensembles à k éléments de {1 à n} et
    renvoie le nombre de sous-ensembles affichés

            :param k: Un entier naturel
            :param n: Un entier naturel non nul

            :Example:

            >>> sousens_nonord_k(0,1)
            0
            >>> sousens_nonord_k(0,2)
            0
            >>> sousens_nonord_k(0,10)
            0

            >>> sousens_nonord_k(1,1)
            {1}
            1
            >>> sousens_nonord_k(1,2)
            {1}
            {2}
            2

            >>> sousens_nonord_k(2,1)
            0
            >>> sousens_nonord_k(2,2)
            {1,2}
            1
            >>> sousens_nonord_k(2,3)
            {1,2}
            {1,3}
            {2,3}
            3
            >>> sousens_nonord_k(2,4)
            {1,2}
            {1,3}
            {1,4}
            {2,3}
            {2,4}
            {3,4}
            6

            >>> sousens_nonord_k(3,1)
            0
            >>> sousens_nonord_k(3,2)
            0
            >>> sousens_nonord_k(3,3)
            {1,2,3}
            1
            >>> sousens_nonord_k(3,4)
            {1,2,3}
            {1,2,4}
            {1,3,4}
            {2,3,4}
            4
            >>> sousens_nonord_k(3,5)
            {1,2,3}
            {1,2,4}
            {1,2,5}
            {1,3,4}
            {1,3,5}
            {1,4,5}
            {2,3,4}
            {2,3,5}
            {2,4,5}
            {3,4,5}
            10

            >>> sousens_nonord_k(4,1)
            0
            >>> sousens_nonord_k(4,2)
            0
            >>> sousens_nonord_k(4,3)
            0
            >>> sousens_nonord_k(4,4)
            {1,2,3,4}
            1
    """

    # Aide :
    # >>> vec = [1, 4, 5, 6]
    # >>> print("{" + ','.join(str(x) for x in vec) + "}")
    # {1,4,5,6}

    # À COMPLÉTER DÉBUT (28 ligne(s))

    # À COMPLÉTER FIN


##########################
### Mots de longueur n ###
##########################

def mots_de_longueur_4(k):
    """Affiche la liste de tous les mots de quatre lettres utilisant les k
    premières lettres de l’alphabet et renvoie le nombre de mots affichés

            -------------------
            --- OBLIGATOIRE ---
            -------------------

            :param k: Un entier naturel non nul

            :Example:

            >>> mots_de_longueur_4(2)
            aaaa
            aaab
            aaba
            aabb
            abaa
            abab
            abba
            abbb
            baaa
            baab
            baba
            babb
            bbaa
            bbab
            bbba
            bbbb
            16
            >>> mots_de_longueur_4(1)
            aaaa
            1
    """

    # À COMPLÉTER DÉBUT (8 ligne(s))

    # À COMPLÉTER FIN


def mots_de_longueur_4_avec_max_2_a(k):
    """Affiche la liste de tous les mots de quatre lettres utilisant les k
    premières lettres de l’alphabet contenant au plus deux fois la lettre ’a’;
    et renvoie le nombre de mots affichés

            :param k: Un entier naturel non nul

            :Example:

            >>> mots_de_longueur_4_avec_max_2_a(2)
            aabb
            abab
            abba
            abbb
            baab
            baba
            babb
            bbaa
            bbab
            bbba
            bbbb
            11
            >>> mots_de_longueur_4_avec_max_2_a(1)
            0
    """

    # À COMPLÉTER DÉBUT (17 ligne(s))

    # À COMPLÉTER FIN


def mots_de_longueur_n_sur_k_lettres(n, k):
    """Affiche tous les mots de longueur n utilisant les k premières lettres de
    l’alphabet et renvoie le nombre de mots affichés

            :param n: Un entier naturel
            :param k: Un entier naturel non nul

            :Example:

            >>> mots_de_longueur_n_sur_k_lettres(0, 3)
            0
            >>> mots_de_longueur_n_sur_k_lettres(1, 3)
            a
            b
            c
            3
            >>> mots_de_longueur_n_sur_k_lettres(2, 3)
            aa
            ab
            ac
            ba
            bb
            bc
            ca
            cb
            cc
            9
            >>> mots_de_longueur_n_sur_k_lettres(3, 2)
            aaa
            aab
            aba
            abb
            baa
            bab
            bba
            bbb
            8

    """

    # À COMPLÉTER DÉBUT (16 ligne(s))

    # À COMPLÉTER FIN


####################
### Backtracking ###
####################

# Le schéma d'un algorithme de backtracking est le suivant :
# Soit un problème P avec une entrée I.

# fonction P(I):
#     Soit S la solution courante initiale.
#     Retourner P_rec(I, S)

# fonction P_rec(I, S):
#     Si la solution courante S peut être rejetée, on s'arrète.
#     Si la solution courante S résoud le problème, on la retourne.
#     Sinon, pour chaque solution S' suivante de S
#         S'' = P_rec(I, S')
#         Si S'' != None, retourner S''

# Il faut donc choisir comment représenter une solution puis en déduire les
# sous-fonctions.
# Par exemple pour les n reines, une solution courante peut-être un vecteur
# s = [(x0, y0), (x1, y1), ..., (xk-1, yk-1)]
# tel que s[i] sont les coordonnées de la reine i. k reines sont alors placées.
# La solution initiale est []
# Une solution peut être rejetée si 2 reines sont sur la même ligne, colone ou
# diagonale.
# Une solution est acceptée ssi toutes les reines ont été placées.
# Les solutions suivantes de s sont
# * Si k = n : aucune, toutes les reines ont déjà été placées
# * Si k < n : pour tout (xk, yk) dans {0,n-1}×{0,n-1},
# [(x0, y0), (x2, y2), ..., (xk-1, yk-1), (xk, yk)]

# Mais peut-être peut-on faire un peu mieux...

def reines(n):
    """Résoud le problème des n reines en utilisant un algorithme de
    backtracking.

            Le jeu de n reines consiste à placer n reines sur un plateau de n×n de
            sorte à ce que deux reines ne soient jamais sur la même ligne, la même
            colone ou la même diagonale.

            :param n: Un entier naturel non nul
            :return: si une configuration existe, un vecteur s tel que s[i] est la
            colone sur laquelle est la reine qui est sur la ligne i. Sinon, None.

            :Example:

            >>> reines_verifier(1, reines(1))
            True
            >>> reines(2)
            >>> reines(3)
            >>> reines_verifier(4, reines(4))
            True
            >>> reines_verifier(5, reines(5))
            True

    """

    s = reines_rec(n, reines_initiale(n))
    return reines_formater(n, s)


def reines_rec(n, s):
    """
    """

    if reines_rejeter(n, s):
        return None
    if reines_accepter(n, s):
        return s
    for s_suiv in reines_suivantes(n, s):
        sol = reines_rec(n, s_suiv)
        if sol != None:
            return sol


def reines_initiale(n):
    """
    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def reines_rejeter(n, s):
    """
    """

    # À COMPLÉTER DÉBUT (26 ligne(s))

    # À COMPLÉTER FIN


def reines_accepter(n, s):
    """
    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def reines_suivantes(n, s):
    """
    """

    # Aide : Utilisez yield pour créer des générateurs :
    # https://www.python-course.eu/python3_generators.php

    # À COMPLÉTER DÉBUT (8 ligne(s))

    # À COMPLÉTER FIN


def reines_formater(n, s):
    """Mets la solution retournée par 'reines_rec' au format de la solution que
    doit retourner 'reines'.

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def reines_verifier(n, s):
    """Retourne True ssi s est une solution valide pour le problème des n reines.

            Cette fonction n'est pas utilisée dans par la fonction 'reines', mais
            est utilisée pour la tester.

    """

    if len(s) != n:
        return False
    for i in range(n):
        for j in range(i+1, n):
            si, sj = s[i], s[j]
            if si == sj or sj == si + (j - i) or sj == si - (j - i):
                return False
    return True


def reines_afficher(n, s):
    """
    """

    if s == None:
        print(None)
    else:
        for i in range(n):
            for k in range(n):
                print("|X" if s[i] == k else "| ", end="")
            print("|")

# Jusqu'à combien de reines votre algorithme arrive-il à résoudre le problème en une minute ?
# Décommentez les lignes ci-dessous et exécuter le fichier.
# (Prévenez-moi si vous réussissez à résoudre le problème jusqu'à au moins 33
# reines en une minute)

# time_limit = 60 # en secondes
# import signal
# class TimeoutException(Exception):
    # pass
# def timeout_handler(signum, frame):
    # raise TimeoutException
# signal.signal(signal.SIGALRM, timeout_handler)
# signal.alarm(time_limit)
# try:
    # n = 1
    # while True:
        # s = reines(n)
        # print("REINES", n)
        # reines_afficher(n, s)
        # n += 1
# except TimeoutException:
    # pass
# quit()


if __name__ == "__main__":
    import doctest
    fonctions = [
        somme_entiers,
        somme_impairs,
        somme_carres,
        factorielle,
        binome,
        fibonacci,
        pgcd,
        syracuse_temps_vol,
        tours_de_hanoi,
        sousens_nonord_2,
        sousens_ord_2,
        sousens_nonord_3,
        sousens_ord_3,
        sousens_nonord_k,
        mots_de_longueur_4,
        mots_de_longueur_4_avec_max_2_a,
        mots_de_longueur_n_sur_k_lettres,
        reines,
    ]
    for f in fonctions:
        print("**********************************************************************")
        print(f.__name__)
        doctest.run_docstring_examples(
            f, globals(), optionflags=doctest.FAIL_FAST)
