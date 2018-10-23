---
title: "Kontrollstrukturen und Listen"
teaching: 0
exercises: 0
questions:
- Wie können Sequenzen von Werten gespeichert werden?
- Wie kann ich Code mehrfach ausführen?
- Wie kann ich Code nur unter einer bestimmten Bedingung ausführen?
objectives:
- Verständnis von wichtigen Hilfsdatentypen und Methoden für Kontrollstrukturen
- Verstehen von Kontrollstrukturen wie Schleifen und Bedingungen
- Ausdrücken von logischen Bedingungen
keypoints:

---

## Listen

Eine Liste ist eine veränderbare Sequenz von Werte. 
Sie kann gleiche Elemente mehrmals enthalten. 
Zudem sind die einzelnen Elemente in einer festen Reihenfolge angeordnet, jedes Element hat einen Index, der dessen Platz in der Liste entspricht. 
Die Elemente einer Liste mit der Länge L können über die Indizes 0..L-1 angesprochen werden.
Das kennen wir bereits von Strings.

~~~python
l = [] # wir initialisieren eine leere Liste
l.append(1) # wir fügen der Liste Elemente hinzu
l.append("Piano")
l.append(1.42)
print(l)
~~~
~~~
[1, 'Piano', 1.42]
~~~
{: .output}

Länge einer Liste:
~~~python
print(len(l))
~~~
~~~
3
~~~
{: .output}

Abruf eines einzelnen Elements:
~~~python
print(l[0])
~~~
~~~
1
~~~
{: .output}

Abruf einer Unterliste:
~~~python
print(l[0:len(l)-1])
~~~
~~~
[1, 'Piano']
~~~
{: .output}

> ## Frage(n)
> - Welchen Typ hat `l`?
> - Welchen Typ hat `l[0:2]`?
> - Welchen Typ haben `l[0]`,`l[1]` und `l[2]`?
{: .discussion}

Es können nicht nur neue Elemente hinzugefügt, sondern auch bestehende Elemente entfernt werden.

~~~python
l.remove("Piano") # wir entfernen ein Element aus der Liste (nach Wert)
l.pop(0) # wir entfernen ein Element aus der Liste (nach Index)
print(l)
~~~
~~~
[1.42]
~~~
{: .output}

Es gibt auch weitere nützliche Methoden auf Listen.

Umgekehrte Reihenfolge mit `reverse`:
~~~python
a = [1,7,3,4]
a.reverse()
print(a)
~~~
~~~
[4, 3, 7, 1]
~~~
{: .output}

Sortierung mit `sort`:
~~~python
a.sort()
print(a)
~~~
~~~
[1, 3, 4, 7]
~~~
{: .output}

Einfügen an angebenen Index (und nicht nur anhängen):
~~~python
a.insert(2,10)
print(a)
~~~
~~~
[1, 3, 10, 4, 7]
~~~
{: .output}

Entfernen des letzten Elements mit `pop()` (ohne Argument):
~~~python
e = a.pop()
print("popped", e, ", list is", a)
~~~
~~~
popped 7 , list is [1, 3, 10, 4]
~~~
{: .output}

Löschen des Inhalts einer Liste:
~~~python
a.clear()
print(a)
~~~
~~~
[]
~~~
{: .output}

## For-Schleifen

Mit dem Ausdruck `for x in var:` kann man den gleichen Code-Block auf jedem Element `x` der Liste `var` ausführen.
Ein Code-Block sind Anweisungen, die mit der gleichen Anzahl Leerzeichen eingerückt sind.
Der Code-Block wird also wiederholt.

~~~python
l = [1, 2, 3, 4, 5]
for x in l:
  print("Element")
  print(x)
~~~
~~~
Element
1
Element
2
Element
3
Element
4
Element
5
~~~
{: .output}

> ## Einrückung mit Leerzeichen oder Tabs?
> Für die Einrückung eines Codeblocks können entweder Leerzeichen oder Tabs verwendet werden.
> Viele Texteditoren ersetzen eine Eingabe mit der <kbd>Tab</kbd> Taste auf der Tastatur automatisch mit einer bestimmten Anzahl Leerzeichen.
> Da Tabs ebenfalls als „Whitespace“ angezeigt werden, ist es schwierig diese auseinanderzuhalten.
> In alten Python-Versionen konnten Leerzeichen und Tabs im selben Skript gemischt werden, was zu Verwirrung und Fehlern bei unterschiedlich tief eingerückten
> Code-Blöcken geführt hat.
> In Python 3 ist das Mischen verboten.
>
> Es bleibt natürlich die Frage, was besser ist.
> Darauf gibt es keine wirklich ultimative Antwort und diese Frage wird in entsprechenden Foren immer wieder stark diskutiert.
> Die „Style Guide for Python Code“ empfielt in neuem Code Leerzeichen zu verwenden: 
> [https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
{: .callout}

Anstatt über eine Liste, können `for`-Schleifen auf sogenannten *Iteratoren* ausgeführt werden.
Iteratoren sind Datenstrukturen, die basierend auf einem aktuellen Zustand einen neuen Zustand berechnen und zurückgeben können.

Die Funktion `range(a,b)` liefert einen Iterator zurück, der nacheinander alle Zahlen von `a` bis `b` (exklusive `b`) ausgibt.

> ## Übung
> Formulieren Sie `for`-Schleife von weiter oben so um, dass sie die `range` Funktion anstatt der Liste benutzt, aber die gleiche Ausgabe erzeugt.
>> ## Lösung
>> ~~~python
>> for x in range(1,6):
>>   print("Element")
>>   print(x)
>> ~~~
> {: .solution}
{: .challenge}

Iteratoren haben gegüben von Listen den Vorteil, dass sie nicht alle Element speichern müssen.
Wenn wir z.B. alle Zahlen von 1 bis 1.000.000 aufaddieren wollen, würde das viel Speicher belegen, wenn wir eine Liste
mit einer Million Zahlen anlegen müssten.
Mit einem Iterator wird immer nur ein kleiner Zustand (die aktuelle Zahl und das Ende des Bereichs) gespeichert.

~~~python
summe = 0
for i in range(1,1_000_001):
  summe = summe + i
print("Summe ist: " + str(summe))
~~~
~~~
Summe ist: 500000500000
~~~
{: .output}

> ## Tausendertrennzeichen im Code
> Um große Zahlen übersichtlicher eingeben zu können, ist seit Python 3.6 im Python-Code `_` als Tausendertrennzeichen erlaubt.
{: .callout}

## Logische Bedingungen

## If-else

## While-Schleifen