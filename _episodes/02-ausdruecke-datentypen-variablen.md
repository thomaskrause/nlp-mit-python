---
title: "Zeichenketten"
teaching: 0
exercises: 0
questions:
- Wie kann ich Zeichenketten in Python eingeben und darstellen?
- Wie kann ich auf diese oder Teile davon zugreifen?
objectives:
- Verstehen des Datentyps `str` Typs von Python
keypoints:
---

Zeichenketten oder *Strings* sind Sequenzen von Zeichen. 
Sie werden in Python gekennzeichnet mit umschließenden `'` oder `"`. Folgende Befehle sind also äquivalent:

~~~python
text = 'Ein Brötchen kostet 25 Cent'
text = "Ein Brötchen kostet 25 Cent"
~~~

Man kann allerdings nicht einen String mit `'` beginnen und dann mit `"` schließen, oder umgekehrt
~~~
text = 'Ein Brötchen kostet 25 Cent"
  File "<stdin>", line 1
    text = 'Ein Brötchen kostet 25 Cent"
                                        ^
SyntaxError: EOL while scanning string literal
~~~
{: .error}

Jedem Zeichen in einem String ist ein Index zugewiesen, der seiner Position in der Zeichenkette entspricht. Gezählt wird ab 0 und Leerzeichen werden nicht übersprungen:

|  E  |  i  |  n  |     |  B  |  r  |  ö  |  t  |  c  |  h  |  e  |  n  |     |  k  |  o  |  s  |  t  |  e  |  t  |     |  2  |  5  |     |  C  |  e  |  n  |  t  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  |
{: .table-bordered}

Der in `text` gespeicherte String hat eine Länge von 27 Zeichen. Diese berechnen wir in Python mit der `len` Funktion:
~~~python
len(text)
~~~

Es ist möglich auf Abschnitte bzw. einzelne Zeichen des Strings über den Index und eckige Klammern zuzugreifen. Probieren Sie es selbst:
~~~python
text[6]
~~~


> ## Zeichenkodierung in Python
>Wir erkennen, dass Python keine Probleme mit Umlauten hat. Das liegt daran, dass in Python 3 (im Gegensatz zu Python 2) Strings standardmäßig in Unicode kodiert sind.
{: .callout}

> ## Negativer Index
> Indexierung funktioniert auch mit negativen Zahlen:
> ~~~python
> text[-3]
>~~~
>
> Was erhalten Sie für den negativen index `[-3]`, wie geht Python in solchen Fällen vor?
>> ## Lösung
>> ~~~
>> 'e'
>> ~~~
>>{: .output}
>> Python gibt nicht das 3. Zeichen von vorne, sondern das 3. Zeichen vom Ende des Textes aus.
> {: .solution}
{: .challenge}

> ## Index größer als Text
> Was passiert in folgendem Fall? Bevor sie es ausführen, was erwarten Sie?
> ~~~python
> text[30]
> ~~~
>> ## Lösung
>> Sie erhalten eine Fehlermeldung, dass der Index außerhalb des korrekten Bereichs für diesen Textwert war.
>> ~~~
>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>> ~~~
>> {: .error}
> {: .solution}
{: .challenge}

{% include links.md %}

