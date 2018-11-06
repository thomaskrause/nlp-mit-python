def levenshtein_distance(a, b):
    cost = 0

    # Basisfall: leere Zeichenketten bei einem der beiden Strings
    # --> man muss die Zeichen des anderen Strings hinzufügen
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    # Teste ob das letzte Zeichen übereinstimmt
    if a[-1] == b[-1]:
        cost = 0
    else:
        # Änderung des letzten Zeichens notwendig
        cost = 1

    # Gebe das Mimimum der Einzelfälle zurück:
    # - entferne letztes Zeichen von a
    # - entferne letztes Zeichen von b
    # - entferne letztes Zeichen von beiden Strings
    return min(
    levenshtein_distance(a[:-1], b) + 1, 
    levenshtein_distance(a, b[:-1]) + 1, 
    levenshtein_distance(a[:-1], b[:-1]) + cost
    )