def levenshtein_distance(s1, s2):
    cost = 0

    # Basisfall: leere Zeichenketten
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # Teste ob das letzte Zeichen übereinstimmt
    if s1[-1] == s2[-1]:
        cost = 0
    else:
        # Änderung des letzten Zeichens notwendig
        cost = 1

    # Gebe das Mimimum der Einzelfälle zurück:
    # - entferne erstes Zeichen von s1
    # - entferne erstes  Zeichen von s2
    # - entferne erstes Zeichen von beiden Strings
    return min(
    levenshtein_distance(s1, s2[1:]) + 1, 
    levenshtein_distance(s1, s2[1:]) + 1, 
    levenshtein_distance(s1[1:], s2[1:]) + cost
    )
