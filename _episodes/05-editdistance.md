---
title: "Levenshtein-Distanz"
teaching: 0
exercises: 0
questions:
- Wie kann man die Levenshtein-Distanz selbst in Python berechnen?
objectives:
- Anwenden vom Wissen zur Organisation von Quelltext
- Implementierung eines gegebenen Algorithmus
keypoints:
- Man sollte versuchen größere Aufgaben in kleinere, einfache zu handhabene Teilaufgaben aufzuteilen
- Funktionen sind nützlich, um diese kleineren Teilaufgaben abzubilden
---

## Nutzung von NLTK zur Berechnung der Levenshtein-Distanz

NLTK ist eine Python-Bibliothek zur Umsetzung vieler NLP-Standard-Aufgaben.
NLTK ist in Untermodulen organisiert.
Für Metriken wie die Levenshtein-Distanz, gibt es das Untermodul `nltk.distance` 
([Dokumentation](http://www.nltk.org/api/nltk.metrics.html#module-nltk.metrics.distance))

NLTK kann mit
~~~python3
import nltk
~~~
importiert werden.

> ## Paketnamen und NLTK
> Paketnamen in NLTK sind nicht unbedingt Modulnamen. So gibt es zwar das Paket `nltk.metrics`, aber nach dem
> Importieren ist der Name des Moduls `nltk.distance`. Das liegt an der etwas verwirrenden internen Modulstruktur von
> NLTK. Zudem gibt es ein anderes Modul mit dem Namen `metrics`, aber aus dem `nltk.translate` Paket und für Konflikte in den Modulnamen sorgt.
> Nutzen Sie einfach `nltk.distance` als Modulenamen, auch wenn die Dokumentation von `nltk.metrics.distance` spricht.
{: .callout}

Die Levenshtein-Distanz ist als Funktion mit der Signatur `edit_distance(s1, s2)` implementiert.
~~~python3
nltk.distance.edit_distance("Geisterbahn", "Achterbahn")
~~~
~~~
4
~~~
{: .output}

## Eigene Implementierung der Levenshtein-Distanz

Wie kann man nun selbst eine Funktion schreiben, die die Levenshtein-Distanz berechnet?

Die Beschreibung des Algorithmus ist folgende:
Man berechnet die Distanz
- vom längeren Wort zum kürzeren
- von jedem Buchstaben aus
- und wählt dann das Minimum

Das allein gibt uns noch keine gute Beschreibung zur eigentlichen Umsetzung, deswegen versuchen wir, das Problem in kleinere Teilprobleme
aufzuteilen, die einfacher zu fassen zu sind.
Diese Teillösungen kombinieren wir dann zur ganzen Lösung.

### „vom längeren Wort zum kürzeren“

> ## Frage(n)
> Was bedeutet der Punkt „vom längeren Wort zum kürzeren“ für die eigentliche Berechnung? Was sind die einfachsten Fälle für diesen Teil der Berechnung?
{: .discussion}

> ## Übung
> Schreiben Sie eine Funktion für den einfachen Fall, dass einer der Strings leer ist.
> Die Funktion soll überprüfen ob der Fall zutrifft und die Levenshtein-Distanz in diesem Fall zurückgeben.
>> ## Lösung
>> ~~~python
>> def levenshtein_distance_add(a, b):
    # Basisfall: leere Zeichenketten bei einem der beiden Strings
    # --> man muss die Zeichen des anderen Strings hinzufügen
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    # Basisfall ist nicht eingetreten
    return None
>> ~~~
>{: .solution}
{: .challenge}

### „von jedem Buchstaben aus“

> ## Frage(n)
> Was bedeutet der Punkt „von jedem Buchstaben aus“ für die eigentliche Berechnung? Was sind die einfachsten Fälle für diesen Teil der Berechnung?
{: .discussion}

> ## Übung
> Schreiben Sie eine Funktion für den einfachen Fall, dass nur eine Zeichen beider Strings verglichen werden muss. Welches Zeichenposition für die Strings bietet sich an?
> Die Funktion soll die Levenshtein-Distanz in diesem Fall zurückgeben.
>> ## Lösung
>> ~~~python
>> def levenshtein_distance_modify(a, b):
    if a[-1] == b[-1]:
        # Keine Änderung des letzten Zeichens notwendig
        return 0
    else:
        # Änderung des letzten Zeichens notwendig
        return 1
>> ~~~
>{: .solution}
{: .challenge}

### „und wählt dann das Minimum“

> ## Frage(n)
> Was bedeutet der Punkt „und wählt dann das Minimum“ für die eigentliche Berechnung? Minimum von was?
{: .discussion}

Sie werden für die Lösung eine Funktion schreiben müssen, die stich rekursiv für immer kleiner werdene Teilzeichenketten selbst aufruft
und die das Minimum der Levenshtein-Distanz für diese Teilzeichenketten auswählt.
Im Basisfall, dass einer der beiden String leer ist, wird die Rekursion abgebrochen.

> ## Übung
> Schreiben Sie eine Funktion, die die Fälle vorher kombiniert und immer eine Levenshtein-Distanz für zwei gegebene Strings ausgibt.
>> ## Lösung
>> ~~~python
>> def levenshtein_distance(a, b):
>>     add_cost = levenshtein_distance_add(a, b)
>>     if add_cost != None:
>>         # Basisfall traf zu, der rekursive Aufruf wird abgebrochen
>>         return add_cost
>> 
>>     cost = levenshtein_distance_modify(a,b)
>> 
>>     # Gebe das Mimimum der Einzelfälle zurück:
>>     # - entferne letztes Zeichen von a
>>     # - entferne letztes Zeichen von b
>>     # - entferne letztes Zeichen von beiden Strings
>>     return min(
>>     levenshtein_distance(a[:-1], b) + 1, 
>>     levenshtein_distance(a, b[:-1]) + 1, 
>>     levenshtein_distance(a[:-1], b[:-1]) + cost
>>     )
>> ~~~
>{: .solution}
{: .challenge}



### Vollständige Implementierung (mit Rekursion)

~~~python
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

def levenshtein_distance(a, b):
    cost = 0

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
~~~

> ## Frage(n)
> Sie werden bemerken, dass die Funktion viel Zeit für die Berechnung der Distanz für längere Strings braucht.
> Warum ist das so und wie könnte man das beheben?
> Vergleichen Sie diese Implementierung mit der von NLTK oder der, die im Rosetta Code Projekt gegeben ist: [https://rosettacode.org/wiki/Levenshtein_distance#Python](https://rosettacode.org/wiki/Levenshtein_distance#Python)
{: .discussion}