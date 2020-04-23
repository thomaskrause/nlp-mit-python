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

NLTK ist eine Python-Bibliothek zur Umsetzung vieler NLP-Standard-Aufgaben und auch über pip verfügbar.
Mit aktivierter Conda-Umgebung kann es kann einfach im System-Terminal mit 
~~~bash
pip install nltk
~~~
installiert werden.

Die Bibliothek ist in Untermodulen organisiert.
Für Metriken wie die Levenshtein-Distanz, gibt es das Untermodul `nltk.distance` 
([Dokumentation](http://www.nltk.org/api/nltk.metrics.html#module-nltk.metrics.distance))

NLTK mit
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
Es ist zwar notwendig, das Problem in Teilprobleme aufzuteilen, aber dadurch wird es auch schwieriger die Motivation der Teilprobleme und Lösungsansätze zu verstehen.
Wenn Sie an einer Stelle nicht weiterkommen, schauen Sie sich die Lösung an und versuchen Sie diese zu verstehen.
Am Ende der Übung wird es hoffentlich klarer, wie die einzelnen Teilprobleme zusammenhängen.

### „vom längeren Wort zum kürzeren“

> ## Übung
> Überlegen Sie, was der Punkt „vom längeren Wort zum kürzeren“ für die eigentliche Berechnung bedeutet? Was sind die einfachsten Fälle für diesen Teil der Berechnung?
> Schreiben Sie eine Funktion für diese einfachen Fälle.
> Die Funktion soll überprüfen ob der Fall zutrifft und die Levenshtein-Distanz in diesem Fall zurückgeben.
>> ## Lösung
>> Der einfachste Fall ist, dass einer der beiden Strings leer ist.
>> In diesem Fall ist die Länge des anderen Strings die Anzahl der Edit-Schritte (hier Anzahl der zu hinzuzufügenden Zeichen) und damit die Levenshtein-Distanz.
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

> ## Übung
> Was bedeutet der Punkt „von jedem Buchstaben aus“ für die eigentliche Berechnung? Was sind die einfachsten Fälle für diesen Teil der Berechnung?
> Wie viele Zeichen müssen minimal zwischen beiden Strings verglichen werden und wenn ja welche(s)?
> Schreiben Sie eine Funktion für diesen einfachen Fall diedie Levenshtein-Distanz in diesem Fall zurückgibgt.
>> ## Lösung
>> 
>> In dieser Funktion wollen wir immer nur ein Zeichen zwischen zwei Strings vergleichen.
>> Es bietet sich an, das letzte Zeichen der Strings dafür zu nehmen.
>> Wenn die letzten Zeichen der Strings gleich sind, ist keine Änderung notwendig und die Distanz ist 0, ansonsten ist sie 1 (da ja nur genau ein Zeichen geändert werden muss).
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
>> ## Lösung
> Wir können bereits die Levenshtein-Distanz für bestimmte Basisfälle berechnen.
> Wenn wir die Levenshtein-Distanz für Teilstrings hätten, bei den wir bei einem der Strings ein Zeichen entfernen oder eines ändern, könnten wir die 
> Levenshtein-Distanz für diese neuen Teilstrings berechnen. 
> Die Levenshtein-Distanz plus die „Kosten“ für das Entfernen oder ändern des Zeichens ergibt die Distanz für beide Gesamtstrings.
> Wir können die Variante (also ob löschen von Zeichen oder Ändern), die am wenigsten Kosten verursacht auswählen und als Wert zurückgeben.
> {: .solution}
{: .discussion}


> ## Rekursion
> 
> Für die Lösung der dieser Aufgabe müssen Sie sich mit rekursiven Funktionsaufrufen beschäftigen.
> Rekursion beim Programmieren ist ein schwieriges Thema, das gerade am Anfang schwer zu greifen ist.
> Grundsätzlich können Funktionen andere Funktionen aufrufen und bilden dabei eine Art Ausführungsbaum.
>
> Wenn man z.B. im folgenden Beispiel die Funktion `main` aufruft, kann man anhand der Ausgabe die einzelnen Ausführungsschritte nachvollziehen.
> 
> ~~~python
> def a():
>   print("a")
> 
> def b():
>   print("b")
>   a()
>
> def main():
>   print("main")
>   a()
>   b()
>
> main()
> ~~~
>
> ~~~
> main
> a
> b
> a
> ~~~
> {: .output}
> Erst wird `main()` aufgerufen, dass erst `a()` aufruft, dann ruft `main()` `b()` auf, was wieder selbst die Funktion `a()` aufruft.
> ~~~
>   main
>  /    \
> a      b
>         \
>          a
> ~~~
>
> Rekursive Funktionen rufen sich selbst auf, was zu potentiell unendlich tiefen Ausführungsbäumen führen kann.
> Es ist daher wichtig, dass eine rekursive Funktion immer eine Art Abbruchbedingung hat, bei der sie sich nicht weiter rekursiv selbst aufruft.
{: .callout}

> ## Übung
> Schreiben Sie eine Funktion, die die Fälle vorher kombiniert und immer eine Levenshtein-Distanz für zwei gegebene Strings ausgibt.
> Diese Funktion soll sich rekursiv für immer kleiner werdende Teilzeichenketten selbst aufrufen
> und die das Minimum der Levenshtein-Distanz für diese Teilzeichenketten auswählen.
> Im Basisfall, dass einer der beiden String leer ist, wird die Rekursion abgebrochen.
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



> ## Vollständige Implementierung (mit Rekursion)
>> ## Lösung
>> ~~~python
>> def levenshtein_distance_add(a, b):
>>     # Basisfall: leere Zeichenketten bei einem der beiden Strings
>>     # --> man muss die Zeichen des anderen Strings hinzufügen
>>     if len(a) == 0:
>>         return len(b)
>>     if len(b) == 0:
>>         return len(a)
>>     # Basisfall ist nicht eingetreten
>>     return None
>> 
>> 
>> def levenshtein_distance_modify(a, b):
>>     if a[-1] == b[-1]:
>>         # Keine Änderung des letzten Zeichens notwendig
>>         return 0
>>     else:
>>         # Änderung des letzten Zeichens notwendig
>>         return 1
>> 
>> def levenshtein_distance(a, b):
>>     cost = 0
>> 
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
> {: .solution}
{: .challenge}

> ## Optimierung von rekursiven Funktionen(n)
> Sie werden bemerken, dass die Funktion `levenshtein_distance` viel Zeit für die Berechnung der Distanz für längere Strings braucht.
> Beim rekursiven Aufruf kann es vorkommen, dass verschiedene Rekursionsschritte die Funktion mit den gleichen Parametern aufrufen, aber jeweils neu berechnen.
> Das ist sehr aufwendig, kann aber vereinfacht werden, in dem man Python anweist, Aufrufe von `levenshtein_distance` mit den gleichen Parametern zu cachen.
> Beim Caching wird die Funktion nur beim ersten Aufruf mit den gleichen Argumentwerten wirklich ausgeführt.
> Der Python-Interpreter merkt sich dann den Rückgabewert für diese Funktion und Argumente.
> Wenn wir die Funktion noch einmal mit den gleichen Argumenten aufgerufen, wird dieser Wert direkt zurückgeben.
> Um den Cache für den Funktionsaufruf zu aktivieren, müssen Sie nur `@lru_cache` ([Dokumentation](https://docs.python.org/3.7/library/functools.html#functools.lru_cache)) als sogenannten „decorator“ vor die Funktionsdefinition schreiben.
> Damit werden die 128 zuletzt genutzten Rückgabewerte gecached („lru“ steht „last recently used“).
> 
> ~~~python
> @lru_cache
> def levenshtein_distance(a, b):
>    cost = 0
>
>    # [...] 
> ~~~
{: .callout}