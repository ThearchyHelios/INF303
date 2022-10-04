############################################################################################
### TP2 - Prise en main de la classe Graphe, Parcours, Graphes eulériens et hamiltoniens ###
############################################################################################

import random
import copy

from lib.graphe import Graphe

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

Pour toute remarque sur le TP en lui-même (indications pas suffisamment
claires, bug, code qui fonctionne en local mais pas sur Caseine, jeux de tests
insuffisants, questions intéressantes à ajouter, orthographe...), contactez
Florian Fontan florian.fontan@grenoble-inp.fr

Attention : les tests fournis ne peuvent être exhaustifs. Qu'une fonction passe
tous les tests ne garantie pas qu'elle soit correcte. Gardez cela en tête
lorsque vous réutilisez vos fonctions dans d'autres fonctions.

---

Pour ce TP, une classe pour manipuler les graphes vous est fournie. Vous
n'avaez pas besoin de comprendre comment elle est implémentée, mais vous
devez comprendre comment l'utiliser. Pour cela, lisez les docstrings et les
exemples donnés dans le fichier graphe.py. La première partie du TP sert en
partie à se familiariser avec la classe Graphe.
"""


########################################
### Manipulation de la classe Graphe ###
########################################

def graphe_1():
    """Retourne le graphe G1.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

           4
         /   \
        0 --- 1    G1
        |     |
        3 --- 2

        :Examples:

        >>> graphe_1()
        {5: 0--1 0--3 0--4 1--2 1--4 2--3}

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    return Graphe(5, [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3)])

    # À COMPLÉTER FIN


def graphe_2():
    """Retourne le graphe G2.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

             2
        3---/-\---1
         \ 4   0 /    G2
          \ \ / /
           \ 6 /
            \ /
             5

        :Examples:

        >>> graphe_2()
        {7: 0--2 0--6 1--3 1--5 2--4 3--5 4--6}

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    return Graphe(7, [(0, 2), (0, 6), (1, 3), (1, 5), (2, 4), (3, 5), (4, 6)])

    # À COMPLÉTER FIN


def graphe_complet(n):
    """Retourne un graphe complet à n sommet.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: Nombre de sommets, entier naturel

        :Examples:

        >>> graphe_complet(3)
        {3: 0--1 0--2 1--2}
        >>> graphe_complet(4)
        {4: 0--1 0--2 0--3 1--2 1--3 2--3}

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    return Graphe(n, [(i, j) for i in range(n) for j in range(i+1, n)])

    # À COMPLÉTER FIN


def cycle(n):
    """Retourne un cycle à n sommet.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: Nombre de sommets, entier naturel >= 3

        :Examples:

        >>> cycle(4)
        {4: 0--1 0--3 1--2 2--3}
        >>> cycle(5)
        {5: 0--1 0--4 1--2 2--3 3--4}

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    return Graphe(n, [(i, (i+1)%n) for i in range(n)])

    # À COMPLÉTER FIN


def graphe_complementaire(g: Graphe):
    """Retourne le graphe complémentaire de g.

        Retourne un graphe g_comp tel que toute arête de g n'est pas une arête
        de g_comp et toute arête de g_comp n'est pas une arête de g.

        :param g: un graphe (Graphe)

        :Examples:

        >>> graphe_complementaire(graphe_complet(4))
        {4:}
        >>> graphe_complementaire(graphe_1())
        {5: 0--2 1--3 2--4 3--4}

    """

    # À COMPLÉTER DÉBUT (6 ligne(s))

    return Graphe(g.nombre_sommets, [(i, j) for i in range(g.nombre_sommets) for j in range(i+1, g.nombre_sommets) if (i, j) not in g.__aretes and (j, i) not in g.__aretes])

    # À COMPLÉTER FIN


def degre_max(g: Graphe):
    """Retourne le degré maximum du graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)

        :Examples:

        >>> degre_max(Graphe(10))
        0
        >>> degre_max(graphe_1())
        3
        >>> degre_max(graphe_2())
        2
        >>> degre_max(graphe_complet(5))
        4
        >>> degre_max(cycle(10))
        2

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))
    
    degre = 0
    for i in range(g.nombre_sommets):
        temp = g.degre(i)
        if temp > degre:
            degre = temp
    return degre

    # À COMPLÉTER FIN


def afficher_matrice(mat):
    """

    """

    for l in mat:
        print(*l)


def matrice_adjacence(g):
    """Retourne la matrice d'adjacence du graphe g.

        :param g: Un graphe (Graphe)
        :return: Une matrice (liste de listes)

        :Examples:

        >>> afficher_matrice(matrice_adjacence(Graphe(3)))
        0 0 0
        0 0 0
        0 0 0
        >>> afficher_matrice(matrice_adjacence(graphe_1()))
        0 1 0 1 1
        1 0 1 0 1
        0 1 0 1 0
        1 0 1 0 0
        1 1 0 0 0
        >>> afficher_matrice(matrice_adjacence(graphe_2()))
        0 0 1 0 0 0 1
        0 0 0 1 0 1 0
        1 0 0 0 1 0 0
        0 1 0 0 0 1 0
        0 0 1 0 0 0 1
        0 1 0 1 0 0 0
        1 0 0 0 1 0 0
        >>> afficher_matrice(matrice_adjacence(graphe_complet(4)))
        0 1 1 1
        1 0 1 1
        1 1 0 1
        1 1 1 0
        >>> afficher_matrice(matrice_adjacence(cycle(5)))
        0 1 0 0 1
        1 0 1 0 0
        0 1 0 1 0
        0 0 1 0 1
        1 0 0 1 0

    """

    # Aide : pour créer une liste de i liste comportant j 0.
    # >>> mat = [[0]*j for _ in range(i)]

    # À COMPLÉTER DÉBUT (6 ligne(s))

    # À COMPLÉTER FIN


def matrice_incidence(g):
    """Retourne la matrice d'incidence du graphe g.

        :param g: Un graphe (Graphe)
        :return m: Une matrice (liste de listes)

        :Examples:

        >>> afficher_matrice(matrice_incidence(Graphe(3)))
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> afficher_matrice(matrice_incidence(graphe_1()))
        1 1 1 0 0 0
        1 0 0 1 1 0
        0 0 0 1 0 1
        0 1 0 0 0 1
        0 0 1 0 1 0
        >>> afficher_matrice(matrice_incidence(graphe_2()))
        1 1 0 0 0 0 0
        0 0 1 1 0 0 0
        1 0 0 0 1 0 0
        0 0 1 0 0 1 0
        0 0 0 0 1 0 1
        0 0 0 1 0 1 0
        0 1 0 0 0 0 1
        >>> afficher_matrice(matrice_incidence(graphe_complet(4)))
        1 1 1 0 0 0
        1 0 0 1 1 0
        0 1 0 1 0 1
        0 0 1 0 1 1
        >>> afficher_matrice(matrice_incidence(cycle(5)))
        1 1 0 0 0
        1 0 1 0 0
        0 0 1 1 0
        0 0 0 1 1
        0 1 0 0 1

    """

    # À COMPLÉTER DÉBUT (12 ligne(s))

    # À COMPLÉTER FIN


################
### Parcours ###
################

def parcours_postfixe(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours postfixé du graphe g en partant du sommet u.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)

        :Examples:

        >>> parcours_postfixe(graphe_1(), 0) # doctest: +NORMALIZE_WHITESPACE
        3 2 4 1 0
        >>> parcours_postfixe(graphe_1(), 1) # doctest: +NORMALIZE_WHITESPACE
        2 3 4 0 1
        >>> parcours_postfixe(graphe_2(), 0) # doctest: +NORMALIZE_WHITESPACE
        6 4 2 0
        >>> parcours_postfixe(graphe_2(), 1) # doctest: +NORMALIZE_WHITESPACE
        5 3 1
        >>> parcours_postfixe(graphe_complet(5), 0) # doctest: +NORMALIZE_WHITESPACE
        4 3 2 1 0
        >>> parcours_postfixe(cycle(7), 1) # doctest: +NORMALIZE_WHITESPACE
        2 3 4 5 6 0 1

    """

    # Indication : vous devriez avoir besoin d'une fonction auxiliaire.

    # À COMPLÉTER DÉBUT (8 ligne(s))

    # À COMPLÉTER FIN

# Pour le parcours en largeur, il est nécessaire d'utiliser une file.
# Vous devez donc implémenter les fonctions creer_file, enfiler, defiler et
# est_vide.
# La file est implémentée sous forme d'un tableau avec deux compteurs, un qui
# mémorise le début de la file, l'autre la fin.
# C'est donc une liste de 3 éléments [[e1, e2], debut, fin].
# Notez que les éléments ne sont en pratique pas supprimés de la file. Seul le
# compteur de début est incrémenté lors de l'opération defiler.

# Représentation d'une file contenant 2, 7 et 4
# -----------------------------------------
# f    ...    | 2 | 7 | 4 | -1 |    ...
#               ^       ^
#             debut    fin
# -----------------------------------------

# On enfile 5 :
# -----------------------------------------
# f    ...    | 2 | 7 | 4 | 5 |    ...
#               ^           ^
#             debut        fin
# -----------------------------------------

# On défile, c'est 2 qui sort :
# -----------------------------------------
# f    ...    | 2 | 7 | 4 | 5 |    ...
#                   ^       ^
#                 debut    fin
# -----------------------------------------


def creer_file(n):
    """Retourne une file (File) dont le nombre d'éléments est <= n.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: nombre maximum d'éléments ajoutés à la file.

        :Examples:

        >>> creer_file(3)
        [[-1, -1, -1], 0, -1]

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def enfiler(f, e):
    """Ajoute un élément à la fin de la file f.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file
        :param e: élément à ajouter à la file

        :Examples:

        >>> f = creer_file(3)
        >>> f
        [[-1, -1, -1], 0, -1]

        >>> enfiler(f, 2)
        >>> f
        [[2, -1, -1], 0, 0]

        >>> enfiler(f, 3)
        >>> f
        [[2, 3, -1], 0, 1]

    """

    tab = f[0]

    # À COMPLÉTER DÉBUT (2 ligne(s))

    # À COMPLÉTER FIN


def defiler(f):
    """Supprime et retourne le premier élément de la file f.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file

        :Examples:

        >>> f = creer_file(4)
        >>> enfiler(f, 2)
        >>> enfiler(f, 3)
        >>> enfiler(f, 5)
        >>> f
        [[2, 3, 5, -1], 0, 2]

        >>> defiler(f)
        2
        >>> defiler(f)
        3
        >>> defiler(f)
        5
        >>> f
        [[2, 3, 5, -1], 3, 2]

    """

    tab = f[0]

    # À COMPLÉTER DÉBUT (2 ligne(s))

    # À COMPLÉTER FIN


def est_vide(f):
    """Renvoie True si la file f est vide.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file

        :Examples:

        >>> f = creer_file(2)
        >>> est_vide(f)
        True
        >>> enfiler(f, 2)
        >>> enfiler(f, 3)
        >>> est_vide(f)
        False
        >>> defiler(f)
        2
        >>> est_vide(f)
        False
        >>> defiler(f)
        3
        >>> est_vide(f)
        True

    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def parcours_largeur(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours en largeur du graphe g en partant du sommet u.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)
        :param u: Indice d'un sommet de g, entier naturel compris entre 0 et n-1

        :Examples:

        >>> parcours_largeur(graphe_1(), 0) # doctest: +NORMALIZE_WHITESPACE
        0 1 3 4 2
        >>> parcours_largeur(graphe_1(), 1) # doctest: +NORMALIZE_WHITESPACE
        1 0 2 4 3
        >>> parcours_largeur(graphe_2(), 0) # doctest: +NORMALIZE_WHITESPACE
        0 2 6 4
        >>> parcours_largeur(graphe_2(), 1) # doctest: +NORMALIZE_WHITESPACE
        1 3 5
        >>> parcours_largeur(graphe_complet(5), 0) # doctest: +NORMALIZE_WHITESPACE
        0 1 2 3 4
        >>> parcours_largeur(cycle(7), 1) # doctest: +NORMALIZE_WHITESPACE
        1 0 2 6 3 5 4

    """

    # À COMPLÉTER DÉBUT (11 ligne(s))

    # À COMPLÉTER FIN


def parcours_prefixe(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours préfixé du graphe g en partant du sommet u.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> parcours_prefixe(graphe_1(), 0) # doctest: +NORMALIZE_WHITESPACE
        0 1 2 3 4
        >>> parcours_prefixe(graphe_1(), 1) # doctest: +NORMALIZE_WHITESPACE
        1 0 3 2 4
        >>> parcours_prefixe(graphe_2(), 0) # doctest: +NORMALIZE_WHITESPACE
        0 2 4 6
        >>> parcours_prefixe(graphe_2(), 1) # doctest: +NORMALIZE_WHITESPACE
        1 3 5
        >>> parcours_prefixe(graphe_complet(5), 0) # doctest: +NORMALIZE_WHITESPACE
        0 1 2 3 4
        >>> parcours_prefixe(cycle(7), 1) # doctest: +NORMALIZE_WHITESPACE
        1 0 6 5 4 3 2

    """

    # Aide : cette fonction peut être implémtentée au choix de manière
    # récursive (comme le parcours postfixé) ou de manière itérative (comme le
    # parcours en largeur).
    # Si vous choisissez la version itérative, vous pouvez utiliser une liste
    # comme pile avec les méthodes 'append' et 'pop' pour ajouter et retirer
    # des éléments.
    # Vous aurez aussi besoin de parcourir les voisins en sens inverse pour
    # obtenir le même affichage que dans les tests. Pour cela il suffit de
    # faire :
    # >>> for v in reversed(g.voisins(u)):
    # ...     ...

    # Récursif
    # À COMPLÉTER DÉBUT (9 ligne(s))

    # À COMPLÉTER FIN

    # Itératif
    # À COMPLÉTER DÉBUT (9 ligne(s))

    # À COMPLÉTER FIN


def est_connexe(g):
    """Retourne True si g est connexe, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> est_connexe(graphe_1())
        True
        >>> est_connexe(graphe_2())
        False
        >>> est_connexe(graphe_complet(5))
        True
        >>> est_connexe(Graphe(1))
        True
        >>> est_connexe(Graphe(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]))
        True
        >>> est_connexe(Graphe(6, [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5)]))
        True
        >>> est_connexe(Graphe(2))
        False
        >>> est_connexe(Graphe(5))
        False
        >>> est_connexe(Graphe(4, [(0, 1), (2, 3)]))
        False
        >>> est_connexe(Graphe(5, [(0, 1), (1, 2), (2, 3)]))
        False
        >>> est_connexe(Graphe(5, [(i, j) for i in range(0, 4) for j in range(i+1, 4)]))
        False
        >>> est_connexe(Graphe(6, [(i, j) for i in range(0, 5) for j in range(i+1, 5)]))
        False
        >>> est_connexe(Graphe(6, [(0, 1), (0, 2), (1, 2), (3, 4), (4, 5), (3, 5)]))
        False
        >>> est_connexe(Graphe(8,
        ...     [(i, j) for i in range(0, 4) for j in range(i+1, 4)] +
        ...     [(i, j) for i in range(4, 8) for j in range(i+1, 8)]))
        ...
        False

    """

    # À COMPLÉTER DÉBUT (15 ligne(s))

    # À COMPLÉTER FIN


def nombre_composantes_connexes(g):
    """Retourne le nombre de composantes connexes de g.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> nombre_composantes_connexes(graphe_1())
        1
        >>> nombre_composantes_connexes(graphe_2())
        2
        >>> nombre_composantes_connexes(graphe_complet(5))
        1
        >>> nombre_composantes_connexes(Graphe(1))
        1
        >>> nombre_composantes_connexes(Graphe(5))
        5
        >>> nombre_composantes_connexes(Graphe(6, [(0, 1), (2, 3), (4, 5)]))
        3

    """

    # À COMPLÉTER DÉBUT (20 ligne(s))

    # À COMPLÉTER FIN


###################################
### Chemins et cycles eulériens ###
###################################

def a_cycle_eulerien(g):
    """Retourne True si g admet un cycle eulérien, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> a_cycle_eulerien(graphe_1())
        False
        >>> a_cycle_eulerien(graphe_2())
        False
        >>> a_cycle_eulerien(graphe_complet(4))
        False
        >>> a_cycle_eulerien(graphe_complet(5))
        True
        >>> a_cycle_eulerien(cycle(4))
        True
        >>> a_cycle_eulerien(Graphe(5))
        False

    """

    # À COMPLÉTER DÉBUT (6 ligne(s))

    # À COMPLÉTER FIN


def a_chemin_eulerien(g):
    """Retourne True si g admet un chemin eulérien, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> a_chemin_eulerien(graphe_1())
        True
        >>> a_chemin_eulerien(graphe_2())
        False
        >>> a_chemin_eulerien(graphe_complet(2))
        True
        >>> a_chemin_eulerien(graphe_complet(4))
        False
        >>> a_chemin_eulerien(graphe_complet(5))
        True
        >>> a_chemin_eulerien(cycle(4))
        True
        >>> a_chemin_eulerien(Graphe(5))
        False

    """

    # À COMPLÉTER DÉBUT (7 ligne(s))

    # À COMPLÉTER FIN


def promenade(g, u):
    """Retourne le chemin élémentaire obtenu en parcourant g depuis le sommet
    d'indice u en choisissant la première arête disponible jusqu'à ce qu'il n'y
    en aie plus de disponible.
    Les arêtes parcourues sont supprimées de g.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> g = graphe_1()
        >>> promenade(g, 0)
        [0, 1, 2, 3, 0, 4, 1]
        >>> g
        {5:}

        >>> g = graphe_1()
        >>> promenade(g, 4)
        [4, 0, 1, 2, 3, 0]
        >>> g
        {5: 1--4}

        >>> g = graphe_2()
        >>> promenade(g, 0)
        [0, 2, 4, 6, 0]
        >>> g
        {7: 1--3 1--5 3--5}

        >>> g = graphe_2()
        >>> promenade(g, 1)
        [1, 3, 5, 1]
        >>> g
        {7: 0--2 0--6 2--4 4--6}

    """

    # À COMPLÉTER DÉBUT (9 ligne(s))

    # À COMPLÉTER FIN


def graphe_3(n):
    """Retourne un graphe G3 à 3+2n sommets tel que pour tout i<n, G contient
    les arètes :
        * (i, 2i+1)
        * (i, 2i+2)
        * (2i+1, 2i+2)

        :param n: entier naturel

              7
             /|
            3-8
           /|
          1-4-9
         /|  \|
        0 |  10     G3(4)
         \|
          2-5
           \|
            6

        :Examples:

        >>> graphe_3(0)
        {3: 0--1 0--2 1--2}
        >>> graphe_3(1)
        {5: 0--1 0--2 1--2 1--3 1--4 3--4}
        >>> graphe_3(2)
        {7: 0--1 0--2 1--2 1--3 1--4 2--5 2--6 3--4 5--6}

    """

    g = Graphe(2*n+3)
    for i in range(n+1):
        g.ajouter_arete(i, 2*i+1)
        g.ajouter_arete(i, 2*i+2)
        g.ajouter_arete(2*i+1, 2*i+2)
    return g


def cycle_eulerien(g, u=0):
    """Retourne un cycle eulérien de g en partant du sommet u.

        :param g: Un graphe (Graphe) eulérien
        :param u: L'indice d'un sommet de g, entier naturel compris entre 0 et
        g.nombre_sommets()-1

        :Examples:

        >>> cycle_eulerien_verifier(graphe_3(0))
        True
        >>> cycle_eulerien_verifier(graphe_3(1))
        True
        >>> cycle_eulerien_verifier(graphe_3(2))
        True
        >>> cycle_eulerien_verifier(graphe_3(3))
        True
        >>> cycle_eulerien_verifier(graphe_3(4))
        True
        >>> cycle_eulerien_verifier(graphe_3(5))
        True
        >>> cycle_eulerien_verifier(graphe_3(6))
        True
        >>> cycle_eulerien_verifier(graphe_3(7))
        True
        >>> cycle_eulerien_verifier(graphe_3(8))
        True
        >>> cycle_eulerien_verifier(graphe_3(32))
        True
        >>> cycle_eulerien_verifier(graphe_3(128))
        True
        >>> cycle_eulerien_verifier(cycle(4))
        True
        >>> cycle_eulerien_verifier(graphe_complet(5))
        True
        >>> cycle_eulerien_verifier(graphe_complet(7))
        True

    """

    # Indication : Que se passe-t-il si on exécute la fonction 'promenade' sur
    # un graphe eulérien ?

    # À COMPLÉTER DÉBUT (8 ligne(s))

    # À COMPLÉTER FIN


def cycle_eulerien_verifier(g):
    g_copy1 = copy.copy(g)
    g_copy2 = copy.copy(g)
    c = cycle_eulerien(g_copy1)
    if c == None or c[0] != c[-1]:
        return False
    g_copy2.supprimer_chemin(c)
    return g_copy2.nombre_aretes() == 0


def graphe_4():
    """Retourne le graphe G4.

        2      4
        |\    /|
        | 0--1 |  G4
        |/    \|
        3      5

        :Examples:

        >>> graphe_4()
        {6: 0--1 0--2 0--3 1--4 1--5 2--3 4--5}

    """

    return Graphe(6, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 3), (4, 5)])


def chemin_eulerien(g):
    """Retourne un chemin eulérien de g en partant du sommet u.

        :param g: Un graphe (Graphe) contenant un chemin eulérien

        :Examples:

        >>> chemin_eulerien_verifier(graphe_1())
        True
        >>> chemin_eulerien_verifier(graphe_3(0))
        True
        >>> chemin_eulerien_verifier(graphe_3(1))
        True
        >>> chemin_eulerien_verifier(graphe_3(2))
        True
        >>> chemin_eulerien_verifier(graphe_3(3))
        True
        >>> chemin_eulerien_verifier(graphe_3(4))
        True
        >>> chemin_eulerien_verifier(graphe_3(5))
        True
        >>> chemin_eulerien_verifier(graphe_3(6))
        True
        >>> chemin_eulerien_verifier(graphe_3(7))
        True
        >>> chemin_eulerien_verifier(graphe_3(8))
        True
        >>> chemin_eulerien_verifier(graphe_3(32))
        True
        >>> chemin_eulerien_verifier(graphe_3(128))
        True
        >>> chemin_eulerien_verifier(graphe_4())
        True
        >>> chemin_eulerien_verifier(graphe_complet(5))
        True
        >>> chemin_eulerien_verifier(graphe_complet(7))
        True
        >>> chemin_eulerien_verifier(graphe_4())
        True

    """

    # À COMPLÉTER DÉBUT (10 ligne(s))

    # À COMPLÉTER FIN


def chemin_eulerien_verifier(g):
    """

    """

    g_copy1 = copy.copy(g)
    g_copy2 = copy.copy(g)
    c = cycle_eulerien(g_copy1)
    g_copy2.supprimer_chemin(c)
    return g_copy2.nombre_aretes() == 0


######################################
### Chemins et cycles hamiltoniens ###
######################################

def cycle_hamiltonien(g):
    """Retourne un cycle hamiltonien de g en utilisant un algorithme de
    backtracking.

        :param g: un graphe (Graphe)
        :return: un cycle hamiltonien de g sous forme de liste de sommets s'il
        en possède un, sinon None.

        :Example:

        >>> cycle_hamiltonien_verifier(graphe_1(), cycle_hamiltonien(graphe_1()))
        True
        >>> cycle_hamiltonien_verifier(graphe_complet(5), cycle_hamiltonien(graphe_complet(5)))
        True
        >>> cycle_hamiltonien_verifier(graphe_3(0), cycle_hamiltonien(graphe_3(0)))
        True
        >>> cycle_hamiltonien(graphe_2())
        >>> cycle_hamiltonien(graphe_3(1))
        >>> cycle_hamiltonien(graphe_3(2))
        >>> cycle_hamiltonien(graphe_3(3))
        >>> cycle_hamiltonien(graphe_3(4))
        >>> cycle_hamiltonien(graphe_3(8))
        >>> cycle_hamiltonien(graphe_4())

    """

    s = cycle_hamiltonien_rec(g, cycle_hamiltonien_initiale(g))
    return cycle_hamiltonien_formater(g, s)


def cycle_hamiltonien_rec(g, s):
    """
    """

    if cycle_hamiltonien_rejeter(g, s):
        return None
    if cycle_hamiltonien_accepter(g, s):
        return s
    for s_suiv in cycle_hamiltonien_suivantes(g, s):
        sol = cycle_hamiltonien_rec(g, s_suiv)
        if sol != None:
            return sol


def cycle_hamiltonien_initiale(g):
    """
    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def cycle_hamiltonien_rejeter(g, s):
    """
    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def cycle_hamiltonien_accepter(g, s):
    """
    """

    # À COMPLÉTER DÉBUT (2 ligne(s))

    # À COMPLÉTER FIN


def cycle_hamiltonien_suivantes(g, s):
    """
    """

    # À COMPLÉTER DÉBUT (12 ligne(s))

    # À COMPLÉTER FIN


def cycle_hamiltonien_formater(g, s):
    """
    """

    # À COMPLÉTER DÉBUT (1 ligne(s))

    # À COMPLÉTER FIN


def cycle_hamiltonien_verifier(g, cycle):
    """Retourne True ssi cycle est un cycle hamiltonien du graphe g.

        Cette fonction n'est pas utilisée par la fonction 'cycle_hamiltonien',
        mais est utilisée pour la tester.

    """

    n = g.nombre_sommets()
    if len(cycle) != n + 1:
        return False
    if cycle[0] != cycle[-1]:
        return False
    deja_vu = [False]*n
    for i in range(n):
        u = cycle[i]
        v = cycle[i+1]
        if deja_vu[u]:
            return False
        deja_vu[u] = True
        if v not in g.voisins(u):
            return False
    return True


def graphe_eulerien(n):
    """Retourne un graphe (Graphe) eulérien à n sommets.

    """

    g = Graphe(n)
    d_max = n-1 if n % 2 == 1 else n-2
    m_min = (n-1)*(n-2) / 2  # => G connexe
    while g.nombre_aretes() < m_min:  # On tire des arêtes au hazard.
        u = random.randint(0, n-1)
        while g.degre(u) > d_max:
            u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        while g.degre(v) > d_max or v == u:
            v = random.randint(0, n-1)
        if v not in g.voisins(u):
            g.ajouter_arete(u, v)

    for u in range(n):  # On ajoute des arêtes pour rendre le graphe eulérien.
        if g.degre(u) % 2 == 1:
            for v in range(u+1, n):
                if g.degre(v) % 2 == 1 and v not in g.voisins(u):
                    g.ajouter_arete(u, v)
                    break
    return g


def graphe_non_hamiltonien(n):
    """Retourne un graphe (Graphe) non hamiltonien à n sommets.

    """

    g = Graphe(n)
    for u in range(n-1):
        for v in range(u+1, n-1):
            g.ajouter_arete(u, v)
    g.ajouter_arete(n-2, n-1)
    return g

# Pour les problèmes de cycles/chemins hamiltoniens, on ne connait pas
# d'algorithmes 'rapides'. Décommentez les lignes suivantes et observer la
# différences de temps d'exécution entre les fonctions chemin_eulerien et
# chemin_hamiltonien.


"""
i = 10
while True:
    print("i", i)
    chemin_eulerien(graphe_eulerien(i))
    i += 10
quit()
"""

"""
i = 3
while True:
    b = cycle_hamiltonien(graphe_non_hamiltonien(i))
    print("i", i, b)
    i += 1
quit()
"""


if __name__ == "__main__":
    import doctest
    fonctions = [
        graphe_1,
        graphe_2,
        graphe_complet,
        cycle,
        graphe_complementaire,
        degre_max,
        matrice_adjacence,
        matrice_incidence,
        parcours_postfixe,
        creer_file,
        enfiler,
        defiler,
        est_vide,
        parcours_largeur,
        parcours_prefixe,
        est_connexe,
        nombre_composantes_connexes,
        a_cycle_eulerien,
        a_chemin_eulerien,
        promenade,
        cycle_eulerien,
        chemin_eulerien,
        cycle_hamiltonien,
    ]
    for f in fonctions:
        print("**********************************************************************")
        print(f.__name__)
        doctest.run_docstring_examples(
            f, globals(), optionflags=doctest.FAIL_FAST)
