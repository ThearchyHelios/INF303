#########################################################
### TP5 - Flots maximum, Graphes bipartis, Coloration ###
#########################################################

from lib.graphe import Graphe
try:
    from lib.sortedcontainers import SortedDict
except:
    from sortedcontainers import SortedDict

import copy
import time

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
tous les tests ne garantit pas qu'elle soit correcte. Gardez cela en tête
lorsque vous réutilisez vos fonctions dans d'autres fonctions.
"""

#####################
### Flots maximum ###
#####################

# On considère des graphes orientés tel que pour chaque arc (uv) d'un graphe G,
# G contient aussi l'arc (vu) (possiblement avec capacité 0).

def ajouter_arete(g, u, v, c):
    g.ajouter_arete(u, v, c)
    g.ajouter_arete(v, u, 0)

def graphe_1():
    """Retourne le graphe G1.

       4
    0-->--1  G1

    """

    g = Graphe(2, oriente=True)
    ajouter_arete(g, 0, 1, 4)
    return g

def graphe_2():
    """Retourne le graphe G2.

          1
         ^ \
     10 /   \ 8
       /     v
      0       3
       \     ^
      7 \   / 9
         v /
          2

    """

    g = Graphe(4, oriente=True)
    ajouter_arete(g, 0, 1, 10)
    ajouter_arete(g, 1, 3, 8)
    ajouter_arete(g, 0, 2, 7)
    ajouter_arete(g, 2, 3, 9)
    return g

def graphe_3():
    """Retourne le graphe G3.

          1
         ^|\
     10 / | \ 10
       /  |  v
      0  1|   3
       \  |  ^
     10 \ | / 10
         vv/
          2

    """

    g = Graphe(4, oriente=True)
    ajouter_arete(g, 0, 1, 10)
    ajouter_arete(g, 1, 3, 10)
    ajouter_arete(g, 0, 2, 10)
    ajouter_arete(g, 2, 3, 10)
    ajouter_arete(g, 1, 2, 1)
    return g

def graphe_4():
    """Retourne le graphe G4.

             1     4
          1-->--4-->--7
         /             \
        /               \
     5 ^                 v 10
      /                   \
     / 8     6     8     5 \
    0-->--2-->--5-->--8-->--10
     \                     /
      \                   /
     2 v                 ^ 2
        \               /
         \             /
          3-->--6-->--9
             2     3

    """

    g = Graphe(11, oriente=True)

    ajouter_arete(g, 0, 1, 5)
    ajouter_arete(g, 1, 4, 1)
    ajouter_arete(g, 4, 7, 4)
    ajouter_arete(g, 7, 10, 10)

    ajouter_arete(g, 0, 2, 8)
    ajouter_arete(g, 2, 5, 6)
    ajouter_arete(g, 5, 8, 8)
    ajouter_arete(g, 8, 10, 5)

    ajouter_arete(g, 0, 3, 2)
    ajouter_arete(g, 3, 6, 2)
    ajouter_arete(g, 6, 9, 3)
    ajouter_arete(g, 9, 10, 2)

    return g

def graphe_5():
    """Retourne le graphe G5 (flot max 28).

             9
          1-->--4
         /|\    |\
        / | \15 | \
    10 ^  v  v  v  v 10
      /  4|   \ |15 \
     / 5  |  8 \| 10 \
    0-->--2-->--5-->--7    G5
     \    |\    |    /
      \  4| \6  |15 /
    15 v  v  ^  v  ^ 10
        \ |   \ | /
         \|    \|/
          3-->--6
            30

    """

    g = Graphe(8, oriente=True)

    ajouter_arete(g, 0, 1, 10)
    ajouter_arete(g, 0, 2, 5)
    ajouter_arete(g, 0, 3, 15)

    ajouter_arete(g, 1, 2, 4)
    ajouter_arete(g, 1, 4, 9)
    ajouter_arete(g, 1, 5, 15)
    ajouter_arete(g, 2, 3, 4)
    ajouter_arete(g, 2, 5, 8)
    ajouter_arete(g, 3, 6, 30)

    ajouter_arete(g, 4, 5, 15)
    ajouter_arete(g, 4, 7, 10)
    ajouter_arete(g, 5, 6, 15)
    ajouter_arete(g, 5, 7, 10)
    ajouter_arete(g, 6, 2, 6)
    ajouter_arete(g, 6, 7, 10)

    return g

# Dans cette partie, vous avez le droit d'utiliser la fonction suivante :

def capacite(g, u, v):
    """Retourne la capacité de l'arc (uv) dans le Graphe g.

        Si g ne contient pas l'arc (uv), retourne 0.

        :Examples:

        >>> g1 = graphe_1()
        >>> capacite(g1, 0, 1)
        4
        >>> capacite(g1, 1, 0)
        0

    """

    return g.voisins(u).get(v, 0)

# Un flot est stocké dans un dictionnaire dont les clefs sont des couples de
# sommets (u, v).
# Exemple :
# >>> flot = SortedDict({})
# >>> flot[(0, 1)] = 2 # On envoie 2 unités de flots sur l'arc (1,2)
# Pour récupérer une valeur, on utilise la méthode get.
# Le 1e paramètre est la clef dont on cherche la valeur.
# Le 2e paramètrs est la valeur à renvoyer si la clef n'est pas dans le
# dictionnaire.
# >>> flot.get((0, 1), 0)
# 2
# >>> flot.get((0, 2), 0)
# 0

# Un flot ne peut pas être strictement négatif.
# Le capacité résiduel d'un arc (uv) vaut cr = cuv - fuv + fvu où cuv est la
# capacité de l'arc et fuv (resp. fvu) la quantité de flot envoyé sur l'arc
# (uv) (resp. (vu)).

def chemin_residuel(g, flot, s, t):
    """Retourne un chemin de s à t dans le graphe RÉSIDUEL du Graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        Retourne None s'il n'y a pas de chemin de s à t.

        Le parcours est un parcours en profondeur.

        :Examples:

        >>> chemin_residuel(graphe_1(), {}, 0, 1)
        [0, 1]
        >>> chemin_residuel(graphe_1(), {(0, 1): 4}, 0, 1)
        >>> chemin_residuel(graphe_2(), {}, 0, 3)
        [0, 1, 3]
        >>> chemin_residuel(graphe_2(), {(0, 1): 7, (1, 3): 7}, 0, 3)
        [0, 1, 3]
        >>> chemin_residuel(graphe_2(), {(0, 1): 8, (1, 3): 8}, 0, 3)
        [0, 2, 3]
        >>> chemin_residuel(graphe_3(), {}, 0, 3)
        [0, 1, 2, 3]
        >>> chemin_residuel(graphe_3(), {(0, 1): 10, (1, 3): 9, (1, 2): 1, (2, 3): 1}, 0, 3)
        [0, 2, 1, 3]
        >>> chemin_residuel(graphe_4(), {}, 0, 10)
        [0, 1, 4, 7, 10]
        >>> chemin_residuel(graphe_5(), {}, 0, 7)
        [0, 1, 2, 3, 6, 7]

    """

    # Vous pouvez créer des fonctions auxiliaires si vous en sentez le besoin.

    # Implémentation récursive

    ### À COMPLÉTER DÉBUT (13 ligne(s))
    for v in g.voisins(s):
        if capacite(g, s, v) - flot.get((s, v), 0) + flot.get((v, s), 0) > 0:
            if v == t:
                return [s, v]
            else:
                chemin = chemin_residuel(g, flot, v, t)
                if chemin is not None:
                    return [s] + chemin
    return None

    ### À COMPLÉTER FIN

    # Implémentation itérative

    ### À COMPLÉTER DÉBUT (21 ligne(s))

    ### À COMPLÉTER FIN

def cout_residuel(g, flot, chemin):
    """Retourne la valeur maximum dont on peut augmenter le flot à l'aide
    du chemin de s à t stocké dans le tableau de prédécesseur pred.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :Examples:

        >>> cout_residuel(graphe_1(), SortedDict({}), [0, 1])
        4
        >>> cout_residuel(graphe_1(), SortedDict({(0, 1): 1}), [0, 1])
        3
        >>> cout_residuel(graphe_2(), SortedDict({}), [0, 1, 3])
        8
        >>> cout_residuel(graphe_2(), SortedDict({(0, 1): 2, (1, 3): 2}), [0, 1, 3])
        6
        >>> cout_residuel(graphe_3(), SortedDict({}), [0, 1, 2, 3])
        1
        >>> cout_residuel(graphe_3(), SortedDict({(0, 1): 10, (1, 3): 9, (1, 2): 1, (2, 3): 1}), [0, 2, 1, 3])
        1
        >>> f = SortedDict({
        ...     (0, 1): 10, (0, 2): 3, (1, 2): 1, (1, 4): 9, (2, 3): 4,
        ...     (3, 6): 4,  (4, 5): 9, (5, 6): 6, (5, 7): 3, (6, 7): 10})
        >>> cout_residuel(graphe_5(), f, [0, 2, 1, 5, 4, 7])
        1

    """

    ### À COMPLÉTER DÉBUT (5 ligne(s))
    cout = capacite(g, chemin[0], chemin[1]) - flot.get((chemin[0], chemin[1]), 0) + flot.get((chemin[1], chemin[0]), 0)
    for i in range(1, len(chemin) - 1):
        cout = min(cout, capacite(g, chemin[i], chemin[i + 1]) - flot.get((chemin[i], chemin[i + 1]), 0) + flot.get((chemin[i + 1], chemin[i]), 0))
    return cout
    ### À COMPLÉTER FIN

    ### À COMPLÉTER FIN

def mettre_a_jour_flot(g, flot, chemin):
    """Met à jour le flot sur le chemin chemin.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :Examples:

        >>> f1 = SortedDict({})
        >>> mettre_a_jour_flot(graphe_1(), f1, [0, 1])
        >>> f1
        SortedDict({(0, 1): 4})
        >>> f1_2 = SortedDict({(0, 1): 1})
        >>> mettre_a_jour_flot(graphe_1(), f1_2, [0, 1])
        >>> f1_2
        SortedDict({(0, 1): 4})
        >>> f2 = SortedDict({})
        >>> mettre_a_jour_flot(graphe_2(), f2, [0, 1, 3])
        >>> f2
        SortedDict({(0, 1): 8, (1, 3): 8})
        >>> f3 = SortedDict({})
        >>> mettre_a_jour_flot(graphe_3(), f3, [0, 1, 2, 3])
        >>> f3
        SortedDict({(0, 1): 1, (1, 2): 1, (2, 3): 1})
        >>> f3_2 = SortedDict({(0, 1): 10, (1, 3): 9, (1, 2): 1, (2, 3): 1})
        >>> mettre_a_jour_flot(graphe_3(), f3_2, [0, 2, 1, 3])
        >>> f3_2
        SortedDict({(0, 1): 10, (0, 2): 1, (1, 2): 0, (1, 3): 10, (2, 3): 1})

    """

    ### À COMPLÉTER DÉBUT (9 ligne(s))
    cout = cout_residuel(g, flot, chemin)
    for i in range(len(chemin) - 1):
        flot[(chemin[i], chemin[i + 1])] = flot.get((chemin[i], chemin[i + 1]), 0) + cout
        if (chemin[i + 1], chemin[i]) in flot:
            flot[(chemin[i + 1], chemin[i])] = flot[(chemin[i + 1], chemin[i])] - cout
            if flot[(chemin[i + 1], chemin[i])] == 0:
                del flot[(chemin[i + 1], chemin[i])]

    ### À COMPLÉTER FIN

def ford_fulkerson(g, s, t, debug=False):
    """Retourne un s,t-flot maximum du graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param debug: si True, affiche chaque chemin de s à t au moment où il
        est trouvé (None si pas de chemin) et chaque état du flot.

        :return: un flot (sous forme de SortedDict).

        :Examples:

        >>> ford_fulkerson(graphe_1(), 0, 1, True)
        SortedDict({})
        [0, 1]
        SortedDict({(0, 1): 4})
        None
        SortedDict({(0, 1): 4})
        >>> ford_fulkerson(graphe_2(), 0, 3, True)
        SortedDict({})
        [0, 1, 3]
        SortedDict({(0, 1): 8, (1, 3): 8})
        [0, 2, 3]
        SortedDict({(0, 1): 8, (0, 2): 7, (1, 3): 8, (2, 3): 7})
        None
        SortedDict({(0, 1): 8, (0, 2): 7, (1, 3): 8, (2, 3): 7})
        >>> ford_fulkerson(graphe_3(), 0, 3, True)
        SortedDict({})
        [0, 1, 2, 3]
        SortedDict({(0, 1): 1, (1, 2): 1, (2, 3): 1})
        [0, 1, 3]
        SortedDict({(0, 1): 10, (1, 2): 1, (1, 3): 9, (2, 3): 1})
        [0, 2, 1, 3]
        SortedDict({(0, 1): 10, (0, 2): 1, (1, 2): 0, (1, 3): 10, (2, 3): 1})
        [0, 2, 3]
        SortedDict({(0, 1): 10, (0, 2): 10, (1, 2): 0, (1, 3): 10, (2, 3): 10})
        None
        SortedDict({(0, 1): 10, (0, 2): 10, (1, 2): 0, (1, 3): 10, (2, 3): 10})
        >>> ford_fulkerson(graphe_4(), 0, 10, True)
        SortedDict({})
        [0, 1, 4, 7, 10]
        SortedDict({(0, 1): 1, (1, 4): 1, (4, 7): 1, (7, 10): 1})
        [0, 2, 5, 8, 10]
        SortedDict({(0, 1): 1, (0, 2): 5, (1, 4): 1, (2, 5): 5, (4, 7): 1, (5, 8): 5, (7, 10): 1, (8, 10): 5})
        [0, 3, 6, 9, 10]
        SortedDict({(0, 1): 1, (0, 2): 5, (0, 3): 2, (1, 4): 1, (2, 5): 5, (3, 6): 2, (4, 7): 1, (5, 8): 5, (6, 9): 2, (7, 10): 1, (8, 10): 5, (9, 10): 2})
        None
        SortedDict({(0, 1): 1, (0, 2): 5, (0, 3): 2, (1, 4): 1, (2, 5): 5, (3, 6): 2, (4, 7): 1, (5, 8): 5, (6, 9): 2, (7, 10): 1, (8, 10): 5, (9, 10): 2})
        >>> ford_fulkerson(graphe_5(), 0, 7, True)
        SortedDict({})
        [0, 1, 2, 3, 6, 7]
        SortedDict({(0, 1): 4, (1, 2): 4, (2, 3): 4, (3, 6): 4, (6, 7): 4})
        [0, 1, 4, 5, 6, 7]
        SortedDict({(0, 1): 10, (1, 2): 4, (1, 4): 6, (2, 3): 4, (3, 6): 4, (4, 5): 6, (5, 6): 6, (6, 7): 10})
        [0, 2, 1, 4, 5, 7]
        SortedDict({(0, 1): 10, (0, 2): 3, (1, 2): 1, (1, 4): 9, (2, 3): 4, (3, 6): 4, (4, 5): 9, (5, 6): 6, (5, 7): 3, (6, 7): 10})
        [0, 2, 1, 5, 4, 7]
        SortedDict({(0, 1): 10, (0, 2): 4, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 4, (3, 6): 4, (4, 5): 8, (4, 7): 1, (5, 6): 6, (5, 7): 3, (6, 7): 10})
        [0, 2, 5, 4, 7]
        SortedDict({(0, 1): 10, (0, 2): 5, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 4, (2, 5): 1, (3, 6): 4, (4, 5): 7, (4, 7): 2, (5, 6): 6, (5, 7): 3, (6, 7): 10})
        [0, 3, 2, 5, 4, 7]
        SortedDict({(0, 1): 10, (0, 2): 5, (0, 3): 4, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 0, (2, 5): 5, (3, 6): 4, (4, 5): 3, (4, 7): 6, (5, 6): 6, (5, 7): 3, (6, 7): 10})
        [0, 3, 6, 2, 5, 4, 7]
        SortedDict({(0, 1): 10, (0, 2): 5, (0, 3): 7, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 0, (2, 5): 8, (3, 6): 7, (4, 5): 0, (4, 7): 9, (5, 6): 6, (5, 7): 3, (6, 2): 3, (6, 7): 10})
        [0, 3, 6, 5, 7]
        SortedDict({(0, 1): 10, (0, 2): 5, (0, 3): 13, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 0, (2, 5): 8, (3, 6): 13, (4, 5): 0, (4, 7): 9, (5, 6): 0, (5, 7): 9, (6, 2): 3, (6, 7): 10})
        None
        SortedDict({(0, 1): 10, (0, 2): 5, (0, 3): 13, (1, 2): 0, (1, 4): 9, (1, 5): 1, (2, 3): 0, (2, 5): 8, (3, 6): 13, (4, 5): 0, (4, 7): 9, (5, 6): 0, (5, 7): 9, (6, 2): 3, (6, 7): 10})

    """

    ### À COMPLÉTER DÉBUT (10 ligne(s))

    ### À COMPLÉTER FIN

def coupe_min(g, flot, s):
    """Retourne une s,t-coupe minimum du graphe g à l'aide du s,t-flot maximum
    flot.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :return: un s,t-coupe minimum du graphe g sous forme de liste de
        sommets.

        :Examples:

        >>> g1 = graphe_1()
        >>> f1 = ford_fulkerson(g1, 0, 1)
        >>> coupe_min(g1, f1, 0)
        [0]
        >>> g2 = graphe_2()
        >>> f2 = ford_fulkerson(g2, 0, 3)
        >>> coupe_min(g2, f2, 0)
        [0, 1]
        >>> g3 = graphe_3()
        >>> f3 = ford_fulkerson(g3, 0, 3)
        >>> coupe_min(g3, f3, 0)
        [0]
        >>> g4 = graphe_4()
        >>> f4 = ford_fulkerson(g4, 0, 10)
        >>> coupe_min(g4, f4, 0)
        [0, 1, 2, 5, 8]
        >>> g5 = graphe_5()
        >>> f5 = ford_fulkerson(g5, 0, 7)
        >>> coupe_min(g5, f5, 0)
        [0, 2, 3, 6]

    """

    ### À COMPLÉTER DÉBUT (12 ligne(s))
    

    ### À COMPLÉTER FIN


########################
### Graphes bipartis ###
########################

def graphe_biparti_complet(a, b):
    """Retourne le graphe Kab.

        :Examples:

        >>> graphe_biparti_complet(1, 1)
        {2: 0--1}
        >>> graphe_biparti_complet(2, 1)
        {3: 0--2 1--2}
        >>> graphe_biparti_complet(1, 2)
        {3: 0--1 0--2}
        >>> graphe_biparti_complet(2, 2)
        {4: 0--2 0--3 1--2 1--3}
        >>> graphe_biparti_complet(3, 2)
        {5: 0--3 0--4 1--3 1--4 2--3 2--4}
        >>> graphe_biparti_complet(2, 3)
        {5: 0--2 0--3 0--4 1--2 1--3 1--4}

    """

    ### À COMPLÉTER DÉBUT (1 ligne(s))

    ### À COMPLÉTER FIN


def partitions(g):
    """Retourne la partition du graphe biparti g.

        :param g: un graphe (Graphe) biparti.
        :return: une liste l tel que
        * pour tout sommet u de g, l[u] = 0 ou 1
        * pour tout sommet u, v de g, si l[u] == l[v], alors (uv) n'est pas
        dans E(g).

        :Examples:

        >>> partitions_test(graphe_1())
        True
        >>> partitions_test(graphe_2())
        True
        >>> partitions_test(graphe_4())
        True
        >>> partitions_test(graphe_biparti_complet(1, 1))
        True
        >>> partitions_test(graphe_biparti_complet(2, 3))
        True
        >>> partitions_test(graphe_biparti_complet(5, 1))
        True
        >>> partitions_test(graphe_biparti_complet(5, 10))
        True
        >>> partitions_test(graphe_biparti_complet(10, 10))
        True
        >>> partitions_test(Graphe(5, [(4, 0), (0, 3), (3, 2), (2, 1)]))
        True
        >>> partitions_test(Graphe(4, [(0, 1), (2, 3)]))
        True

    """

    ### À COMPLÉTER DÉBUT (15 ligne(s))

    ### À COMPLÉTER FIN

def partitions_test(g):
    l = partitions(g)
    n = g.nombre_sommets()

    # On vérifie si l[u] == 0 ou 1.
    for u in range(n):
        if l[u] != 0 and l[u] != 1:
            print(l)
            print("u", u, "l[u]", l[u])
            return False

    # Pour toute arête (uv) de g, on vérifie si l[u] != l[v].
    for u in range(n):
        for v in g.voisins(u):
            if l[u] == l[v]:
                print(l)
                print("u", u, "l[u]", l[u], "v", v, "l[v]", l[v])
                return False

    return True



def couplage_maximum_biparti(g):
    """Retourne un couplage maximum du graphe g en utilisant l'algorithme
    de Ford-Fulkerson.

        :param g: un graphe (Graphe) biparti.
        :return: un ensemble d'arêtes formant un couplage maximum de g.

        :Examples:

        >>> couplage_maximum_biparti_test(graphe_1())
        1
        >>> couplage_maximum_biparti_test(graphe_2())
        2
        >>> couplage_maximum_biparti_test(graphe_4())
        5
        >>> couplage_maximum_biparti_test(graphe_biparti_complet(1, 1))
        1
        >>> couplage_maximum_biparti_test(graphe_biparti_complet(2, 3))
        2
        >>> couplage_maximum_biparti_test(graphe_biparti_complet(5, 1))
        1
        >>> couplage_maximum_biparti_test(graphe_biparti_complet(5, 10))
        5
        >>> couplage_maximum_biparti_test(graphe_biparti_complet(10, 10))
        10

    """

    # On crée un graphe g_flot orienté an ajoutant les sommets source et puit.
    # Aide : utilisez la fonction partition donnée plus haut.

    n = g.nombre_sommets()

    ### À COMPLÉTER DÉBUT (10 ligne(s))

    ### À COMPLÉTER FIN

    # On exécute l'algorithme de Ford-Fulkerson sur ce graphe.
    flot = ford_fulkerson(g_flot, s, t)

    # On récupère la liste des arêtes ayant un flot non nul
    e = [] # arêtes du couplage

    ### À COMPLÉTER DÉBUT (3 ligne(s))

    ### À COMPLÉTER FIN

    return e

def couplage_maximum_biparti_test(g):
    e = couplage_maximum_biparti(g)

    deja_vu = [False] * g.nombre_sommets()
    for u, v in e: # Pour chaque arête (uv) du couplage
        # On vérifie si (uv) est bien une arête de g.
        if v not in g.voisins(u):
            print(e)
            print(u, v)
            return False
        # On vérifie si u et v n'ont pas déjà été couverts.
        if deja_vu[u] == True:
            print(e)
            print(u)
            return False
        if deja_vu[v] == True:
            print(e)
            print(v)
            return False
        deja_vu[u] = True
        deja_vu[v] = True
    return len(e)


##################
### Coloration ###
##################

def est_biparti(g):
    """

    """

    # À VENIR...

def dsat(g):
    """

    https://fr.wikipedia.org/wiki/DSATUR

    """

    # À VENIR...

def welsh_powell(g):
    """

    https://fr.wikipedia.org/wiki/Coloration_de_graphe#Algorithme_de_Welsh_et_Powell

    """

    # À VENIR...

def coloration_min(g):
    """

    """

    # À VENIR...


if __name__ == "__main__":
    import doctest
    # doctest.testmod(verbose=True, optionflags=doctest.FAIL_FAST)
    fonctions = [
            chemin_residuel,
            cout_residuel,
            mettre_a_jour_flot,
            ford_fulkerson,
            coupe_min,
            graphe_biparti_complet,
            partitions,
            couplage_maximum_biparti,
    ]
    for f in fonctions:
        print("**********************************************************************")
        print(f.__name__)
        doctest.run_docstring_examples(f, globals(), optionflags=doctest.FAIL_FAST)

