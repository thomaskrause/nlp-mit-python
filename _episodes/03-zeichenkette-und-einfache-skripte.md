---
title: "Zeichenketten und einfache Skripte"
teaching: 110
exercises: 0
questions:
- Wie kann ich Zeichenketten in Python eingeben und darstellen?
- Wie kann ich auf diese oder Teile davon zugreifen?
- Was muss ich beim Ausführen von Python-Skripten beachten?
objectives:
- Verstehen des Datentyps `str` Typs von Python
keypoints:
- Strings sind Sequenzen von Zeichen auf die über einen Index zugegriffen werden kann.
- Es gibt Methoden, die Operationen auf diesen Zeichenketten ausführen, wie z.B. finden und ersetzen.
- Variablen werden nur innerhalb eines Aufrufs des Python-Interpreters gespeichert.
---

## Zeichenketten als Wert definieren

Zeichenketten oder *Strings* sind Sequenzen von Zeichen die zur Repräsentation von Text verwendet werden. 
Sie werden in Python gekennzeichnet mit umschließenden `'` oder `"`. Folgende Befehle sind also äquivalent:

~~~python
text = 'Ein Brötchen kostet 25 Cent'
text = "Ein Brötchen kostet 25 Cent"
~~~

Variablen mit einem Textwert haben den Typ `str`:
~~~python
type(text)
~~~
~~~
<class 'str'>
~~~
{: .output}

Man kann allerdings nicht einen String mit `'` beginnen und dann mit `"` schließen, oder umgekehrt
~~~
text = 'Ein Brötchen kostet 25 Cent"
  File "<stdin>", line 1
    text = 'Ein Brötchen kostet 25 Cent"
                                        ^
SyntaxError: EOL while scanning string literal
~~~
{: .error}

## Zugriff auf Teile von Strings

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

> ## Frage(n)
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
{: .discussion}

> ## Frage(n)
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
{: .discussion}

Einen Abschnitt eines Strings (*Substring*) erhalten wir über einen Index `[a:b]` wobei `a` der Index des ersten Zeichens ist und `b` das Ende des Abschnitts beschreibt. `a` ist inklusiv, der `a`-te Buchstabe ist also selbst im Substring enthalten, `b` ist dagegen exklusiv, der `b`-te Buchstabe ist also nicht enthalten, nur der Buchstabe (mit Index `b-1`) davor.
~~~python
text[0:3]
~~~
~~~
'Ein'
~~~
{: .output}

> ## Frage(n)
> Probieren Sie anhand eines Beispielstrings mit der Länge L folgende Dinge aus:
> - Was passiert, wenn Sie a, b oder beide Grenzen weglassen?
> - Was passiert, wenn b > Länge des Strings
> - Was passiert, wenn a > Länge des Strings
> - Was passiert, wenn a > b? Was wenn a == b?
> - Was passiert, wenn a > 0 und b < 0?
> - Was passiert, wenn a < 0 und b > 0?
>
>> ## Lösung
>> Wenn die erste Grenze a weggelassen wird, wird implizit das erste Zeichen (0) als Start angenommen.
>> ~~~python
>> text[:3]
>> ~~~
>> ~~~
>> 'Ein'
>> ~~~
>> {: .output}
>>
>> Wenn dagegen die zweite Grenze b weggelassen wird, wird implizit das letzte Zeichen als Ende angenommen.
>> ~~~python
>> text[23:]
>> ~~~
>> ~~~
>> 'Cent'
>> ~~~
>> {: .output}
>>
>> Das Weglassen beider Grenzen entspricht dem ganzen String, ohne Einschränkung für Beginn und Ende.
>> ~~~python
>> text[:]
>> ~~~
>> ~~~
>> 'Ein Brötchen kostet 25 Cent'
>> ~~~
>> {: .output}
>>
>> Der End-Index wird immer implizit auf die Länge des Strings begrenzt.
>> Ist der Größer, wird der String nur bis zum Ende des Strings zurück gegeben. 
>> Ist hingegen der Start-Index größer als die Länge des Texts, wird nur der leere String zurück gegeben.
>> ~~~python
>> text[4:123]
>> ~~~
>> ~~~
>> 'Brötchen kostet 25 Cent'
>> ~~~
>> {: .output}
>> ~~~python
>> text[123:]
>> ~~~
>> ~~~
>> ''
>> ~~~
>> {: .output}
>>
>> Analog dazu, wird auch der leere String ausgegeben, wenn der Start-Index größer oder gleich dem End-Index ist.
>> ~~~python
>> text[123:4]
>> ~~~
>> ~~~
>> ''
>> ~~~
>> {: .output}
>> ~~~python
>> text[4:4]
>> ~~~
>> ~~~
>> ''
>> ~~~
>> {: .output}
>>
>> Wenn der Start-Index a größer gleich 0 ist und der End-Index b negativ, wird der Teilstring vom Zeichen mit dem Index a bis zum b. Zeichen zählend vom Ende des Texts zurückgegeben.
>> ~~~python
>> text[4:-8]
>> ~~~
>> ~~~
>> 'Brötchen kostet'
>> ~~~
>> {: .output}
>> Das geht aber nur, solange der negative Wert nicht über den Anfang des mit a beginnenden Teilstrings "hinausragt".
>> 
>> Wenn a < 0 und b > 0 ist, wird normalerweise eine leerer String zurückgegeben. Wenn das Ende b aber größer ist als die Länge des Strings, ist der Ausdruck äquivalent zu `text[-a:]` und es werden die letzten a Zeichen des Teilstrings ausgeben.
>> ~~~python
>> text[-4:10]
>> ~~~
>> ~~~
>> ''
>> ~~~
>> {: .output}
>> ~~~python
>> text[-4:100]
>> ~~~
>> ~~~
>> 'Cent'
>> ~~~
>> {: .output}
>>
>> Wie Sie sehen, können negative Index sehr schnell sehr kompliziert und unerwartete Semantik mit sich bringen.
>> Die Python-Dokumentation zu "Sequences" hat weitere Beispiele für komplexe Zugriffe über Indexes: <https://docs.python.org/3.7/library/stdtypes.html?highlight=sequence#sequence-types-list-tuple-range>.
>> Solche komplexen Konstrukte werden ohne genaue Kenntnis der Python-Dokument sehr schnell sehr schwer verständlich und sollten vermieden werden.
> {: .solution}
{: .discussion}

> ## Übung
> Beschäftigen wir uns weiter mit dem oben erwähnten String, den wir in text gespeichert haben. Nehmen Sie an, 
> Sie wollen die für Sie wesentliche
> Information aus Werbetexten wie „Ein Brötchen kostet 25 Cent“ extrahieren. 
> Sie interessieren sich nur für das Produkt („Brötchen“) und den Preis („25 Cent“). 
>
> Vervollständigen Sie das folgende Codefragment so, dass diese Daten in den beiden Variablen `what` und `howmuch` gespeichert werden.
> ~~~python
> what = text
> howmuch = text
> ~~~
>> ## Lösung
>> ~~~python
>> what = text[4:12]
>> howmuch = text[20:len(text)]
>>~~~
>{: .solution}
{: .challenge}

## `print`-Funktion

In der interaktiven Konsole kann man den Namen einer Variable als Befehl eingeben und bekommt deren Wert angezeigt.
Sobald wir nicht mehr interaktiv in der Konsole, sondern mit Python-Skripte arbeiten, wird uns das nicht mehr weiterhelfen. 
Wir benötigen eine Funktion, mit der wir Variablen explizit ausgeben können.

Die Funktion `print` nimmt als Eingabe Daten vom Typ String und gibt diese auf der Konsole aus. Das einzige Argument der Funktion wird dabei in Klammern angegeben. Versuchen Sie es selbst:
~~~python
print(what)
~~~

Sie können `print` auch mehrere Strings übergeben. 
Diese werden durch ein Zeichen (Standard: Leerzeichen) getrennt ausgegeben. Das Trennzeichen kann über den Parameter `sep` manipuliert werden.
`sep` ist ein benannter Parameter, das heißt man gibt in den Klammern nicht nur den Wert an, sondern schreibt `sep=` davor.
~~~python
print(what,howmuch)
~~~
~~~
Brötchen 25 Cent
~~~
~~~python
print(what,howmuch,sep=";")
~~~
~~~
Brötchen;25 Cent
~~~
{: .output}

## Ausführen mehrerer Anweisungen in einem Skript

Wie wir bereits im [1. Kapitel](../01-python-starten/index.html) gesehen haben, können wir anstatt Anweisungen für ein Programm interaktiv in der Konsole auszuführen sie auch in eine Textdatei mit der Endung `.py` schreiben.
Der Befehl `python3 dateiname.py` auf der Konsole führt diese Anweisungen dann hintereinander aus.
Wird das Programm beendet, werden auch alle Variablen vergessen.
Jeder Aufruf vom Python-Interpreter startet also immer ohne definierte Variablen, erst durch die einzelnen Ausführungsschritte im Skripts werden die Variablen definiert und mit Werten belegt.
Bei der Entwicklung testet man oft kurze Code-Stücke in der interaktiven Konsole, die man dann in ein Skript überträgt.

> ## Windows
> Windows enthält standardmäßig kein Python und die Unterscheidung in Version 2 und 3 ist daher nicht so relevant. 
> Nach einer systemweiten Installation und der Eintragung von der Python-Installation in die Systemvariable `PATH` oder mit `conda activate` kann man daher unter Windows mit dem Befehl `python` (also ohne die Versionsnummer „3“) auf der Kommandozeile starten.
{: .callout}


> ## Übung
> Nutzen Sie einen Texteditor um ein Programm zu schreiben, dass folgende Anweisungen hintereinander ausführt und führen sie dies aus.
> - Berechne die Summe von 100 und 123
> - Gebe die Zeichenkette "100+123=???" wobei „???“ für das Ergebnis steht.
> 
>> ## Lösung
>> ~~~python
>> # Dieser Text steht in der Datei summe.py
>> summe = 100+123
>> print("100+123",summe,sep="=")
>> ~~~
>> ~~~bash
>> python3 summe.py
>> ~~~
>> ~~~
>> 100+123=223
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

## Strings verketten

Wenn wir zwei Strings miteinander zu einem neuen String verbinden wollen (*konkatenieren*), 
so nutzen wir den „+“-Operator, den wir schon von den Zahlenoperationen kennen.

~~~python
stem_1 = 'Haus'
stem_2 = 'boot'
comp = stem_1 + stem_2
print(comp)
~~~
~~~
Hausboot
~~~
{: .output}

Wollen wir eine Zeichenkette n mal vervielfachen, so können wir sie einfach mit n multiplizieren:
~~~python
result = 'Nomen'*10
print(result)
~~~
~~~
NomenNomenNomenNomenNomenNomenNomenNomenNomenNomen
~~~
{: .output}


Strings können aus anderen Datentypen über die Konvertierungsfunktion `str(val)` erzeugt werden.
Damit kann man z.B. auch einen String mit einer Zahl verketten

~~~python
zahl = 13+13
result = "Die Zahl ist " + str(zahl)
print(result)
~~~
~~~
Die Zahl ist 26
~~~
{: .output}

## String-Methoden

Wir wollen uns einen Überblick über die wichtigsten Methoden für String-Variablen ansehen. 
Aber was sind denn nun wieder *Methoden*? 
In dieser Episode nur so viel: Methoden sind Funktionen, die wir an einer Variable (genauer: einem Objekt) mit Hilfe eines `.` direkt aufrufen. 
Hier ein Beispiel:

~~~python
var = "Huch"
print(var) # Funktion
var.strip() # Methode
~~~

### `strip()`

Diese Methode ist z. B. wichtig bei der Bereinigung unserer Eingabe. 
Sie entfernt Leerzeichen, Zeilenumbrüche (\n in Linux), Tab-Einrückungszeichen (\t) und andere White-Space-Zeichen am Anfang und Ende des Strings. 
Sie verändert nicht die Variable, an der sie aufgerufen wird, sondern gibt einen neuen String zurück.

~~~python
txt = "\tWas macht strip()? "
txt_no_whitespaces = txt.strip()
print("|" + txt + "|")
~~~
~~~
|       Was macht strip()? |
~~~
{: .output}

~~~python
print("|" + txt_no_whitespaces + "|")
~~~
~~~
|Was macht strip()?|
~~~
{: .output}

### `find(seq)` und `rfind(seq)`

Wenn wir eine Sequenz von 1 und mehr Zeichen in einem String suchen wollen, geben uns diese Methoden die Stelle (als Integer) im String zurück, 
an der die Sequenz beginnt. 
`find(seq)` gibt uns den ersten Treffer von links, `rfind(seq)` entsprechend von rechts.
Ausgegeben wird die Stelle des ersten Zeichens der gesuchten Sequenz.

~~~python
haystack = 'Heu Nadel Heu Heu Nadel Heu'
l = haystack.find('Nadel')
r = haystack.rfind('Nadel')
print(l,r)
~~~
~~~
4 18
~~~
{: .output}

> ## Übung
> Bearbeiten Sie den folgenden Abschnitt so, dass aus `info` nur der Text zwischen „Achtung“ und „egal“ ausgegeben (über die `print` Funktion) wird.
> ~~~python
> info = "bla bla bla Achtung Wichtig egal bla bla bla"
> # Ihr Code:
> ~~~
>> ## Lösung
>> ~~~python
>> wichtig_l = info.find("Achtung") + len("Achtung")
>> wichtig_r = info.rfind("egal")
>> print(info[wichtig_l:wichtig_r].strip())
>> ~~~
>>~~~
>>Wichtig
>>~~~
>>{: .output}
> {: .solution}
{: .challenge}

### `replace(is, willbe)`

Mit dieser Methode wird eine Zeichensequenz in einem String an jeder Stelle ihres Vorkommens durch eine andere ersetzt. 
Das Ergebnis wird als neuer String zurückgegeben.

In folgendem Beispiel sollen aus dem Input-String „ß“ und Umlaute entfernt und durch Alternativen ersetzt werden:
~~~python
messy_input = "Sie wohnen in der Hauptstraße. Das ist ungewöhnlich."
clean_input = messy_input.replace("ß","ss").replace("ö","oe").replace("ä","ae").replace("ü","ue")
print(clean_input)
~~~
~~~
Sie wohnen in der Hauptstrasse. Das ist ungewoehnlich.
~~~
{: .output}

> ## Frage(n)
> - Warum kann `replace` einfach mehrmals hintereinander aufgerufen werden?
> - Was passiert, wenn ein String eine zu ersetzende Zeichensequenz nicht enthält?
>
>> ## Lösung
>> Die Methode `replace` liefert als Rückgabewert wieder einen neuen String zurück und auf Strings kann man die Methode `replace` ausführen. 
>> Man muss nicht zwingend den Rückgabewert in eine Variable zwischenspeichern, um ihn zu nutzen.
>>
>> Wenn die gesuchte Zeichensequenz nicht vorkommt, wird der unveränderte Original-String zurückgegeben.
>> ~~~python
>> messy_input.replace("Berlin", "Brandenburg")
>> ~~~
>> ~~~
>> 'Sie wohnen in der Hauptstraße. Das ist ungewöhnlich.'
>> ~~~
>> {: .output}
> {: .solution}
{: .discussion}

> ## Übung
> Schreiben Sie einen „Übersetzer“, der den String german ins Englische übersetzt.
> ~~~python
> german = "Die Katze ist schwarz"
> # Ihr Code
> engl = 
> ~~~
> Überlegen Sie kurz, ob dieses Vorgehen generell, also für eine beliebige deutsche Eingabe, sinnvoll ist.
>> ## Lösung
>> 
>> Wir können im Moment nur kontextunabhängig einzelne Strings ersetzen.
>> Für das konkrete Beispiel reicht das schon, auch wenn wir natürlich kein Zugriff auf ein Lexikon oder syntaktische und semantische Informationen haben und nicht einmal Wörter erkennen oder sogar die Wortstellung umschreiben können. 
>>
>> ~~~python
>> german = "Die Katze ist schwarz"
>> engl = german.replace("Die", "The").replace("Katze", "cat").replace("ist", "is").replace("schwarz", "black")
>> print(engl)
>> ~~~
>> ~~~
>> The cat is black
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

## `startswith` und `endswith` 

Die beiden Funktionen überprüfen, ob ein String mit einem Prefix beginnt oder einem Suffix endet.

~~~python
satz = "Ein Wort ist kein Satz."

print(satz.startswith("Ein"))
print(satz.endswith("!"))
~~~
~~~
True
False
~~~
{: .output}

> ## Übung
> Wie könnte man die beiden Funktionen auch alternativ ohne String-Methoden aber mit dem Wissen aus der ersten Teil dieser Einführung ausdrücken?
>> ## Lösung
>> ~~~python
>> satz = "Ein Wort ist kein Satz."
>>
>> satz[:len("Ein")] == "Ein"
>> satz[-len("Satz."):] == "Satz."
>> ~~~
>{: .solution}
{: .challenge}

{% include links.md %}

