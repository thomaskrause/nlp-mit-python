---
title: "Levenshtein-Distanz"
teaching: 15
exercises: 90
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
~~~bash
pip3 install nltk
~~~
im Systemterminal einmalig installiert werden und mit
~~~python
import nltk
~~~
in einem Python-Skript importiert werden.

> ## Paketnamen und NLTK
> Paketnamen in NLTK sind nicht unbedingt Modulnamen. So gibt es zwar das Paket `nltk.metrics`, aber nach dem
> Importieren ist der Name des Moduls `nltk.distance`. Das liegt an der etwas verwirrenden internen Modulstruktur von
> NLTK. Zudem gibt es ein anderes Modul mit dem Namen `metrics`, aber aus dem `nltk.translate` Paket und für Konflikte in den Modulnamen sorgt.
> Nutzen Sie einfach `nltk.distance` als Modulenamen, auch wenn die Dokumentation von `nltk.metrics.distance` spricht.
{: .callout}

Die Levenshtein-Distanz ist als Funktion mit der Signatur `edit_distance(s1, s2)` implementiert.
~~~python
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


FIXME: Wird fortgesetzt
