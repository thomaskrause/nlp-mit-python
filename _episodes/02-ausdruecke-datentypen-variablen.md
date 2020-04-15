---
title: "Einfache Ausdrücke, Datentypen und Variablen"
teaching: 50
exercises: 0
questions:
- "Wie kann man einfache Ausdrücke in Python ausführen?"
- "Was sind Datentypen und Variablen?"
objectives:
- "Umgang mit der Python-Konsole"
- "Datentypen, Werte und Variablen verstehen"
keypoints:
- "Einfache Ausdrücke können durch die interaktive Eingabe in der Python-Konsole ausgeführt werden."
- "Datentypen sind Kategorien von Werten"
- "Unterschiedliche Ausdrücke können Werte mit unterschiedliche Datentypen erzeugen"
- "Variablen speichern Werte"
- "Variablen muss ein Wert zugewiesen werden bevor sie genutzt werden können"
- "Variablen können in Ausdrücken benutzt werden."
- "Variablen haben Namen und diese Namen unterscheiden Groß- und Kleinschreibung" 
---


## Kommentare und Dokumentation

Kommentieren Sie ihren eigenen Code und dokumentieren Sie somit dessen Funktionsweise. Das erleichtert anderen und auch Ihnen, den Code später noch zu verstehen. Außerdem können auf diese Weise Voraussetzungen Ihres Programms an die Eingabe und eine Darlegung der Form des Outputs dargelegt werden. Kommentare im Code beginnen Sie mit einer `#`.

Ein Beispiel:

~~~python
# Das ist ein Kommentar
# This is a comment
~~~

> ## Sprache in Python-Skripten
>
> Es ist üblich Kommentare und andere Element des Quelltexts
> in Englisch zu halten, da sie so für ein
> breiteres Publikum verständlich sind. Im Rahmen dieses Kurses können
> Sie das aber ignorieren. Sie sollten lediglich sicherstellen, dass 
> Ihre Mit-Studierenden und Ihr Dozent Sie verstehen.
{: .callout}

## Ganze Zahlen und Kommazahlen

In Programmen muss man immer wieder Dinge berechnen, zum Beispiel Häufigkeiten 
von Vorkommen von Wörtern.
Python kann mit zwei Arten von Zahlen umgehen: ganzen Zahlen (*Integer*) und 
Kommazahlen (*Float* von „Gleitkommazahl“).

Zunächst wollen wir testen, wie die Python-Konsole auf Dateneingaben reagiert. Dafür tippen wir eine x-beliebige Zahl ein und drücken die Eingabetaste <kbd>Return</kbd>:

~~~python
12
~~~
Der Python-Interpreter gibt nun folgende Ausgabe als Antwort:
~~~
12
~~~
{: .output}

Die Python-Konsole berechnet für uns den Wert 12. Das klingt nur so merkwürdig, weil es an ursprünglichen Wert 12 nichts mehr zu berechnen gibt, weshalb Ein- und Ausgabe identisch sind. 

Trotzdem haben wir einen vollständigen *Ausdruck* (in Englisch „Expression“) an Python übergeben, den wir mit der Eingabetaste abgeschlossen haben.

12 lässt sich aber noch anders ausdrücken bzw. berechnen, z. B. durch
~~~python
6+6
~~~

Die Python-Konsole gibt uns das Ergebnis der Operation „+“ zurück, angewendet auf 6 und 6.
~~~
12
~~~
{: .output}

Zum Verständnis: Wir haben der Python-Konsole das Input `6+6` gegeben und als Output `12` erhalten. Gleichzeitig haben wir der Operation `+` das Input `(6,6)` gegeben und als Output `12` erhalten.

## Rechenoperationen

Es gibt folgende relevante Rechenoperationen in Python, die Operatoren sind in Klammern mit angebeben.

1. Addition (`+`) und Subtraktion (`-`)
2. Multiplikation (`*`), Division (`/`)
3. ganzzahlige Division (`//`), Modulo (`%`)

`+` und `-` werden zusätzlich als Vorzeichenoperatoren verwendet, wobei wir `+` in diesem Sinne nicht benutzen werden.

~~~python
-12
~~~

Wie in der Mathematik, haben auch in Python `*` und `/` Vorrang vor `+` und `-`. 

> ## Übung
> Was ist die Ausgabe vom Ausdruck und warum?
> ~~~python
> -4*2+10
>~~~
>> ## Lösung
>>~~~
>> 2
>>~~~
>> {: .output}
>> Zuerst wird `-4*2` ausgewertet, was `-8` ergibt. 
>> Danach wird mit `+10` addiert und das Ergebnis `2` angezeigt.
>{: .solution}
{: .challenge}

Klammern können genutzt werden, um die Reihenfolge der Operatoren explizit anzugeben.
~~~python
-4*(2+10)
~~~
~~~
-48
~~~
{: .output}

Wenn wir dividieren, erhalten wir als Rückgabewert keinen Integer, sondern einen Float:
~~~python
3/4
~~~
~~~
0.75
~~~
{: .output}

Das gilt auch, wenn der Dividend durch den Divisor teilbar ist 
und eigentlich eine ganze Zahl anstatt einer Kommazahl zurückgegeben werden
könnte. 
~~~python
-10/5
~~~
~~~
-2.0
~~~
{: .output}
Der Operator erzeugt also immer einen Float als Rückggabewert.


> ## Übung
> Was berechnen die Operatoren `//` und `%` ?
> Finden Sie es für die folgenden Ausdrücke heraus!
> ~~~python
> 5//2
> 6//4
> 9//3
> ~~~
> ~~~python
> 7%4
> 15%13
> 4%2
> ~~~
>> ## Lösung
>> - `5//2` = `2` 
>> - `6//4` = `1`
>> - `9//3` = `3`
>> - `7%4` = `3`
>> - `15%13` = `2`
>> - `4%2` = `0`
>>
>> Ganzzahlige Division (`//`) gibt uns das Ergebnis der Division ohne Nachkommastellen als Integer (nicht: Float) zurück.
>> Modulo-Rechnung (`%`) hingegen gibt uns den Rest der ganzzahligen Division zurück. 
>> Das heißt immer dann, wenn `a` durch `b` teilbar ist, ist `a%b` gleich 0.
>> Diese zwei Operationen können in verschiedenen Anwendungsfällen sehr nützlich sein.
>{: .solution}
{: .challenge}



## Variablen

Wir programmieren (u. a.), um Probleme zu lösen und uns eigene Rechenarbeit zu ersparen. Für komplexe Berechnungen nützt uns die simple Berechnung allein wenig, wir müssen ihr Ergebnis auch zwischenspeichern, um es weiter verwenden zu können. Hierfür gibt es Variablen.

- Variablen sind Namen für Werte.
- In Python wird das `=` Symbol benutzt um eine Wert auf der rechten Seite einer
  Variable auf der linken Seite zuzuweisen.
- Variablen werden erstellt, wenn ihnen ein Wert zugewiesen wird.
- Variablennamen können aus den Buchstaben a-z, A-Z (Groß- und Kleinschreibung wird unterschieden), Unterstrichen und Ziffern bestehen. Ziffern sind nicht als erstes Zeichen erlaubt. Variablen sollten mit Kleinbuchstaben anfangen.

~~~python
zahl1 = 5
zahl2 = 7
~~~

Wir haben 5 in der Variable mit dem Namen zahl1 gespeichert, 7 in zahl2. Die Zuweisung eines Wertes zu einer Variable wird auch *assignment* genannt.

Was passiert, wenn wir anschließend folgenden Befehl ausführen?
~~~python
zahl1+zahl2
~~~
Python evaluiert die Werte von zahl1 und zahl2 und addiert diese. 
~~~
12
~~~
{: .output}
Und auch dieses Ergebnis können wir wieder in einer Variable speichern:
~~~python
ergebnis = zahl1+zahl2
~~~

Variablen können einen leeren Wert annehmen, in denen ihnen der spezielle Wert
`None` zugewiesen wird. 

~~~python
ergebnis = None
ergebnis
~~~
Variablen vom Wert `None` erzeugen keine Ausgabe.


> ## Übung
> Wie können wir nun das Ergebnis der Addition ansehen? 
> Versuchen Sie es auf der Python-Konsole.
>> ## Lösung
>> Sie müssen den Variablennamen als Ausdruck in die Konsole eingeben:
>> ~~~python
>> ergebnis
>> ~~~
> {: .solution}
{: .challenge}

> ## Frage(n)
> Was passiert, wenn wir die folgende Zeilen nacheinander ausführen?
> ~~~python
> zahl1
> Zahl2
> ~~~
>> ## Lösung
>> ~~~
>> >>> zahl1
>> 5
>> >>> Zahl2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Zahl2' is not defined
>> ~~~
>> {: .error}
> {: .solution}
> Was hat das zu bedeuten? 
> Wie können wir das „reparieren“? 
> Was erfahren wir über Variablennamen?
{: .discussion}

## Einfache eingebaute Funktionen

Sogenannte *Funktionen* haben einen Namen, es können ein odere mehrere Argumente in Klammern angegeben werden und sie liefern einen Wert zurück (mehrere Argumente werden durch Komma getrennt).

Zum Beispiel liefert die eingebaute Funktion mit dem Namen `type` eine Information über den Typ eines Werts oder Variable.

~~~python
type(zahl1)
~~~
~~~
<class 'int'>
~~~
{: .output}
Der Rückgabewert zeigt an, dass es sich um eine Ganze Zahl (Integer) handelt.

Im Gegensatz dazu, liefert
~~~python
type(3.141)
~~~
~~~
<class 'float'>
~~~
{: .output}
einen Rückgabe wert für eine Kommazahl (Float) zurück.

Mit der eingebauten Funktion `isinstance(wert, klasse)` kann man überprüfen, ob ein Wert bzw. eine Variable einen bestimmten Typ hat.
Der Rückgabewert ist dabei vom Typ `bool`, also ein Wahrheitswert, und kann `True` oder `False` sein.
~~~python
isinstance(3, int)
~~~
~~~
True
~~~
{: .output}
~~~python
isinstance(3.0, int)
~~~
~~~
False
~~~
{: .output}

Python ist eine dynamisch typisierte Programmiersprache.
Das heißt, die gleiche Variable kann unterschiedliche Typen wie Float oder Integer zugewiesen bekommen.
Mit `type` kann man den Typ herausfinden, aber es gibt auch Funktionen um explizit eine Variable zu einem anderen Typ zu überführen
(„casten“).
- `int(val)` überführt eine Variable in eine Ganzzahl
- `float(val)` überführt eine Variable in eine Gleitkommazahl

~~~python
pi = int(3.141)
type(pi)
~~~
~~~
<class 'int'>
~~~
{: .output}

~~~python
pi
~~~

~~~
3
~~~
{: .output}

~~~python
float(pi)
~~~
~~~
3.0
~~~
{: .output}

Es noch gibt eine Vielzahl weiterer, bereits eingebauter Funktionen in Python.
Eine Listen davon finden Sie unter [https://docs.python.org/3.7/library/functions.html](https://docs.python.org/3.7/library/functions.html)
Einige davon benötigen keine Eingabeargumente, trotzdem müssen in diesem Fall die Klammern mit angegeben werden.


{% include links.md %}

