def levenshtein_distance_add(a, b):
    # Basisfall: leere Zeichenketten bei einem der beiden Strings
    # --> man muss die Zeichen des anderen Strings hinzufügen
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    # Basisfall ist nicht eingetreten
    return None


def levenshtein_distance_modify(a, b):
    if a[-1] == b[-1]:
        # Keine Änderung des letzten Zeichens notwendig
        return 0
    else:
        # Änderung des letzten Zeichens notwendig
        return 1

from functools import lru_cache
@lru_cache(maxsize=4095)
def levenshtein_distance(a, b):
    add_cost = levenshtein_distance_add(a, b)
    if add_cost != None:
        # Basisfall traf zu, der rekursive Aufruf wird abgebrochen
        return add_cost

    cost = levenshtein_distance_modify(a,b)

    # Gebe das Mimimum der Einzelfälle zurück:
    # - entferne letztes Zeichen von a
    # - entferne letztes Zeichen von b
    # - entferne letztes Zeichen von beiden Strings
    return min(
    levenshtein_distance(a[:-1], b) + 1, 
    levenshtein_distance(a, b[:-1]) + 1, 
    levenshtein_distance(a[:-1], b[:-1]) + cost
    )