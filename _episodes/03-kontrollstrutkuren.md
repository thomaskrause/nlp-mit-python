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