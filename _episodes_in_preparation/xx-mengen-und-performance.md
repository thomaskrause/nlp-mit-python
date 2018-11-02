---
title: "Mengen und Performance und Listen"
teaching: 0
exercises: 0
questions:
objectives:
keypoints:
---

## Mengen und der  `in` Operator

Es kann mit `in` auch überprüft werden, ob ein Element in einer Liste vorhanden ist.

~~~python
nachspeisen = ["Obst", "Quark", "Eis"]
if "Obst" in nachspeisen:
  print("Heute mal gesund.")
else:
  print("Esst mehr Obst!")
~~~

Neben Listen gibt es in Python auch Mengen, oder sogenannte *Sets*.
Eine Menge enthält keine Duplikate, kann aber aus Listen mit der `set(...)` Funktion erstellt werden.
Außerdem ist die Reihenfolge einer Menge nicht festgelegt.

~~~python
original = ["Eis", "Obst", "Quark", "Eis"]
nachspeisen = set(original)
print(len(original), len(nachspeisen))
~~~
~~~
4 3
~~~
{: .output}

Im Vergleich zur originalen Liste wurde in der Menge das doppelte `"Eis"` entfernt und daher ist die Länge nur 3 anstatt 4.

~~~python
print(nachspeisen)
~~~
~~~
{'Eis', 'Obst', 'Quark'}
~~~
{: .output}

Da Mengen keine Reihenfolge haben, werden neue Element mit der Funktion `add(v)` hinzugefügt.
Mit `remove(v)` können sie entfernt werden.

~~~python
l = set() # leere Menge
l.add(1) # wir fügen der Menge Elemente hinzu
l.add("Piano")
l.add(1.42)
l.add(1.43)
l.add(1.42)
print(l)
~~~
~~~
{1, 1.43, 1.42, 'Piano'}
~~~
{: .output}

~~~python
l.remove("Piano")
print(l)
~~~
~~~
{1, 1.43, 1.42}
~~~
{: .output}


Die Funktionen `in` funktioniert auch auf Mengen: 
~~~python
1 in l
~~~
~~~
True
~~~
{: .output}

Ebenso gibt es die Funktion `not in` um zu überprüfen ob etwas nicht in der Menge enthalten ist:
~~~python
13 not in l
~~~
~~~
True
~~~
{: .output}

> ## Geschwindigkeit von Sets .vs Listen
> Die Überprüfung, ob ein Wert Teil eines Sets ist kann deutlich schneller geschehen
als in einer Liste.
> Während in einer Liste wirklich jedes Element angeschaut werden muss,
> gibt es für Sets Indexstrukturen, die annähernd konstant und unabhängig von 
> der Länge der Liste die (Nicht)-Zugehörigkeit eines Werts überprüfen können. 
> Insbesondere bei großen Datenmengen kann es also von Vorteil sein ein Set zu nutzen, soweit es semantisch Sinn macht.
{: .callout}

> ## Frage(n)
> Ist der Ausdruck `"1.42" in l` für die Menge `{1, 1.43, 1.42}` wahr?
>> ## Lösung
>> Nein, denn `"1.42"` ist ein String und das Element in der Menge ist eine Ganzkommazahl.
>> Elemente müssen vom Typ gleich sein um verglichen werden zu können.
>> Mit Hilfe der Typumwandlungsfunktion (`str(v)`,`int(v)`,`float(v)`, etc.) können solche Umwandlungen vorgenommen werden.
>> Für einige Typen geschieht die Umwandlung automatisch, so ist z.B. `1.0 in l` wahr, da ein Float zu einem Integer automatisch umgewandelt wird.
> {: .solution}
{: .discussion}