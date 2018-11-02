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
- Sequenzen von beliebigen Werten können in Listen gespeichert und abgerufen werden.
- Logische Ausdrücke haben in Python den Datentyp `bool` und können unter anderem durch Vergleichsoperatoren erzeugt werden.
- Mit Schleifen (`for`, `while`) und bedingt ausgeführten Code-Blöcken (`if`-`elif`-`else`) kann der Programmablauf flexibel auf die Eingabe reagieren und komplexere Berechnungen durchführen.
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

Zählen der Anzahl der Elemente mit gegebenen Wert in einer Liste mit `count`:
~~~python
a = [1,4,7,3,4,4]
a.count(4)
~~~
~~~
3
~~~
{: .output}

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

Der Name der Schleifenvariable kann frei gewählt werden.
Für Indexe hat sich oft `i` eingebürgert, aber sollte möglichst sprechende Namen für Variablen verwenden.
~~~python
for hier_kann_wirklich_alles_stehen in range(0,11):
  print(hier_kann_wirklich_alles_stehen)
~~~
~~~
0
1
2
3
4
5
6
7
8
9
10
~~~
{: .output}

For-Schleifen und andere Kontrollstrukturen können verschachtelt werden, das heißt in einem `for`-Block können z.B. auch weitere `for`-Blöcke stehen.
Die tiefere Verschachtelung eines Code-Blocks wird durch die größere Anzahl an Leerzeichen/Tabs ausgedrückt:
~~~python
for i in range(1,4):
    for j in range(1,4):
        summe = i + j
        produkt = i * j
        print(i, "+", j, "=", summe)
        print(i, "*", j, "=", produkt)
~~~
~~~
1 + 1 = 2
1 * 1 = 1
1 + 2 = 3
1 * 2 = 2
1 + 3 = 4
1 * 3 = 3
2 + 1 = 3
2 * 1 = 2
2 + 2 = 4
2 * 2 = 4
2 + 3 = 5
2 * 3 = 6
3 + 1 = 4
3 * 1 = 3
3 + 2 = 5
3 * 2 = 6
3 + 3 = 6
3 * 3 = 9
~~~
{: .output}

## Ausführen von Code-Blöcken abhängig von logischen Bedingungen

### Einfache logische Bedingungen und der Datentyp `bool`

Neben Strings und Zahlen hat Python auch einen Datentyp für Wahrheitswerte.
Eine Variable mit Wahrheitswerten kann entweder den Wert `True` oder `False` haben.

~~~python
stimmt = False
type(stimmt)
~~~
~~~
<class 'bool'>
~~~
{: .output}

~~~python
stimmt = True
print(stimmt)
~~~
~~~
True
~~~
{: .output}

Man kann Wahrheitswerte durch den Vergleich von anderen Werte über bestimmte Operatoren erhalten.
Z.B. kann man zwei Zeichenketten mit dem `==` Operator vergleichen, ob sie identisch sind:

~~~python
"Haus" == "Haus"
~~~
~~~
True
~~~
{: .output}

Das Ergebnis eines Vergleichs kann auch wieder in einer Variablen gespeichert werden:
~~~python
gleiches_haus = "Haus" == "Haus"
print(gleiches_haus)
~~~
~~~
True
~~~
{: .output}


> ## `==` ist nicht gleich `=`
> Der Vergleichsoperator `==` ist nicht mit dem Zuweisungsoperator `=` zu verwechseln. 
> Letzerer weist einer Variable einen Wert zu und lieft nicht einen logischen Wert zurück.
> Z.B. ist folgender Ausdruck ein Fehler:
> ~~~python
> "Haus" = "Haus"
> ~~~
> ~~~
>  File "<stdin>", line 1
> SyntaxError: can't assign to literal
> ~~~
> {: .error}
{: .callout}

Bei einem Vergleich ist der Wert der Variablen oder des Ausdrucks entscheidend, nicht die Form.
Z.B. liefern auch alle folgenden Vergleiche `True` zurück.

~~~python
"Haus" == 'Haus'
~~~
~~~python
var = 'Haus'
"Haus" == var
~~~
~~~python
0.0000 == 0.0
~~~

Wertevergleiche sind exakt, dass heißt z.B. das bei Groß- und Kleinschreibung von Zeichenketten oder bei Whitespace (Leerzeichen, Tabs, Zeilenumbrüche etc.) unterschieden wird.

~~~python
"Haus" == "haus"
~~~
~~~
False
~~~
{: .output}

~~~python
"Haus" == "Haus "
~~~
~~~
False
~~~
{: .output}

> ## Übung
> Wie können die beiden Zeichenketten `"Haus"` und `"Haus "` mit `True` als Ergebnis verglichen werden?
>> ## Lösung
>> ~~~python
>> "Haus" == "Haus ".strip()
>> ~~~
>{: .solution}
{: .challenge}

Analog zum `==` Operator gibt es den `!=` Operator, der immer dann wahr ist wenn zwei Werte unterschiedlich sind.
~~~python
4 != 1
~~~
~~~
True
~~~
{: .output}



### If-Ausdrücke

Wir haben nur einfache logische Bedingungen mit dem `==` Operator kennengelernt.
Logische Bedingungen können genutzt werden, um Code-Blöcke basierend auf dem Wahrheitswert auszuführen, oder aber nicht.

~~~python
x = 5
if x == 4:
  print("x ist vier!")
~~~
Dieses Programm erzeugt keine Ausgabe, weil die Bedingung nicht wahr ist.
Wenn die Bedinung wahr ist, wird der Code-Block ausgeführt.
~~~python
if x == 5:
  print("x ist fünf!")
~~~
~~~
x ist fünf!
~~~
{: .output}

Die Ein Code-Block kann aus mehr als einer Anweisung bestehen und nach dem eingerückten `if`-Block wird der orginale Code-Block weiter ausgeführt, 
egal ob die Bedingung wahr oder falsch war.
~~~python
x = 5
if x == 4:
  x = x + 2
  print("x wahr vier, neuer Wert ist", x)
x = x - 1
print("x ist", x)
~~~
~~~
x ist 5
~~~
{: .output}

~~~python
x = 5
if x == 5:
  x = x + 2
  print("x wahr fünf, neuer Wert ist", x)
x = x - 1
print("x ist", x)
~~~
~~~
x wahr fünf, neuer Wert ist 7
x ist 6
~~~
{: .output}

### If-Else Ausdrücke

Diese Konstruktion erlaubt die Überprüfung einer Bedingung.
Falls die Bedingung wahr ist, wird der Code-Block hinter der `if`-Anweisung ausgeführt, ansonsten der Block hinter
der `else:` Anweisung:

~~~python
x = 5
if x == 4:
  print("x ist vier")
else:
  print("x ist ein anderer Wert")
~~~
~~~
x ist ein anderer Wert
~~~
{: .output}

### If-Elif(-Else)

Man kann beliebig viele Ausdrücke überprüfen, in dem man zusätzliche `elif` Bedingungen hinzufügt:

~~~python
x = 3
if x == 1:
  print("x ist eins")
elif x == 2:
  print("x ist zwei")
elif x == 3:
  print("x ist drei")
elif x == 4:
  print("x ist vier")
~~~
~~~
x ist drei
~~~
{: .output}

Auch an diese Ausdrücke kann ein `else` angehängt werden:
~~~python
x = 100
if x == 1:
  print("x ist eins")
elif x == 2:
  print("x ist zwei")
elif x == 3:
  print("x ist drei")
elif x == 4:
  print("x ist vier")
else:
  print("x ist ein anderer Wert")
~~~
~~~
x ist ein anderer Wert
~~~
{: .output}

Es wird immer der erste Ausdruck ausgewertet der wahr ist, die anderen werden ignoriert.
~~~python
if 2==1:
  print("Mathematik kaputt")
elif 1==1:
  print("Mathematik geht")
elif 2==2:
  print("Mathematik geht immer noch")
else:
  print("Zustand von Mathematik unbekannt")
~~~
~~~
Mathematik geht
~~~
{: .output}

### While-Schleifen

Man kann logische Bedingungen auch in While-Schleifen verwenden, um einen Block zu wiederholen, solange eine Bedingung erfüllt ist.

~~~python
x = 0
while x != 10:
  print(x)
  x = x + 1 
~~~
~~~
0
1
2
3
4
5
6
7
8
9
~~~
{: .output}

> ## Frage(n)
> Was passiert wenn die Bedingung immer wahr ist, z.B. in: 
> ~~~python
> while 1 == 1:
>   print("Mathematik in Ordnung")
> ~~~ 
{: .discussion}

> ## Programm im Terminal beenden
> Falls Sie ein Programm im Terminal beenden wollen, können Sie
> <kbd>Strg</kbd>+<kbd>C</kbd> drücken.
{: .callout}

> ## Übung
> Schreiben Sie ein kurzes Programm, das eine Liste aller Zahlen zwischen 1 und 999, die ohne Rest durch 13 teilbar sind, erstellt.
> Das Programm soll die Liste am Ende ausgeben.
>> ## Lösung
>> Mögliche Lösung:
>> ~~~python
>> zahl13 = []
>> for i in range(1,1000):
>>     if i % 13 == 0:
>>         zahl13.append(i)
>> print(zahl13)
>> ~~~
>{: .solution}
{: .challenge}

### Arithmetische Vergleichsoperatoren

Neben `==` und `!=` gibt es für Zahlen noch weitere Operatoren:
- `<` für „echt kleiner als“
- `<=` für „kleiner gleich“
- `>` für „echt größer als“
- `>=` für größer gleich“

~~~python
print(2 < 2)
print(2 <= 2)
print(10 > 1)
print(10 >= 1)
~~~
~~~
False
True
True
True
~~~
{: .output}

> ## Übung
> Schreiben Sie ein kurzes Programm, das eine Liste aller Zahlen zwischen 1 und 999, die ohne Rest durch 13 teilbar sind, erstellt.
> Nutzen Sie dafür den `<` Operator!
> Diskutieren Sie die Vor- und Nachteile im Vergleich zur Ihrer Version weiter oben.
>> ## Lösung
>> ~~~python
zahl13 = []
>> x = 13
>> while x < 1000:
>>     zahl13.append(x)
>>     x = x + 13
>> print(zahl13)
>> ~~~
>{: .solution}
{: .challenge}

### Logische Formeln

Logische Ausdrücke können wie auch logische Formeln mit `and`, `or` und `not` verknüpft werden

~~~python
a = True
b = False
implikation = not a or b
~~~

Klammern können genutzt werten um explizit die Reihenfolge der Vergleichsoperatoren anzugeben
~~~python
if (1 != 1 and 1 == 4) or ((2+1) == 4):
  print("Mathematik schon wieder kaputt")
else:
  print("Mathematik geht noch")
~~~

> ## Übung
> Bilden Sie aus den gegebenen den folgenden drei Variablen den komplexen Wahrheitswert `social_security`. Dieser sagt aus, ob wir noch Kindergeld erhalten. Hier die genauen Bedingungen:
> - Wenn wir minderjährig sind, gibt es Kindergeld
> - Wenn wir nicht mehr minderjährig, aber jünger als 25 sind und studieren, gibt es Kindergeld
> - Wenn wir älter als 24 sind und ein FSJ (freiwilliges soziales Jahr) absolviert haben, bekommen wir Kindergeld (wir ignorieren, dass das zeitlich begrenzt ist)
> 
> ~~~python
> age = 24
> studying = False
> fsj = True
>
> social_security = # TODO: logischer Ausdruck
> ~~~
>> ## Lösung
>> ~~~python
>> age = 24
>> studying = False
>> fsj = True
>>
>> social_security = (age < 18) or (age < 25 and studying) or (age > 24 and fsj)
>> ~~~
> {: .solution}
{: .challenge}

## Interaktive Eingabe

Wir kennen bereits `print(var)` um Informationen auszugeben.
Das Gegenstück dazu die Funktion `input()`. 
Sie erlaubt einem Python-Skript, Texteingaben vom Nutzer entgegenzunehmen.

~~~python
print("Hallo, meine Name ist Script!")
name = input("Wie heißen Sie? ")
print("Hallo " +  name + "!")
~~~

Dieses Script erzeugt erst die Ausgabe
~~~
Hallo, meine Name ist Script!
Wie heißen Sie? ▮
~~~
{: .output}

Das Argument von `print()` ist ein sogenannter "Prompt", also eine Eingabeaufforderung an den Nutzer. 
Der Prompt wird ausgegeben und es wir solange gewartet, bis der Nutzer eine Eingabe gemacht und diese mit der Eingabetaste <kbd>Return</kbd> abgeschlossen hat.
Die Funktion liefert die Eingabe als Typ String zurück.
In diesem Beispiel wird die Rückgabe in eine Variable geschrieben und wieder ausgegeben.
~~~
Hallo, meine Name ist Script!
Wie heißen Sie? Thomas 
Hallo Thomas!
~~~
{: .output}

> ## Übung
> Schreiben Sie ein Skript das folgendes tut:
> Das Skript hat eine interne „magic number“, die Sie frei wählen können. 
> Fragen Sie den Nutzer, wie die Nummer ist. Geben Sie ihm Feedback, ob die Zahl die er geraten hat größer oder kleiner als die „magic number“ ist.
> Wenn der Nutzer die Zahl erraten hat, gratulieren Sie ihm und beenden das Programm.
>> ## Lösung
>> Mögliche Lösung:
~~~python
magic_number = 355
guessed = None
while guessed != magic_number:
    guessed = input("Bitte Nummer raten: ")
    guessed = int(guessed)
    if guessed < magic_number:
        print("Zu klein!")
    elif guessed > magic_number:
        print("Zu groß!")
print("Herzlichen Glückwunsch, Sie haben die Nummer erraten!")
~~~
>{: .solution}
{: .challenge}