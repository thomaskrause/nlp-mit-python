---
title: "Eigene Funktionen und Module"
teaching: 0
exercises: 0
questions:
- Wie kann ich selbst eigene Funktionen definieren?
- Wie können Funktionen aus externen Bibliotheken eingebunden werden?' 
objectives:
- Funktionalität von Programmen nachnutzen
keypoints:
- Mit Funktionen können Teile von Programmen ausgegliedert und nachgenutzt werden.
- Eigene Module können in Python-Dateien abgespeichert und mit `import` in anderen Python-Skripten nachgenutzt werden.
- Mit `pip3` können neue Pakete, die Module enthalten, installiert werden.
---

## Eigene Funktionen definieren

Bisher haben wir uns nur mit einfachen Anweisungen
beschäftigt. Typischerweise wollen wir aber nicht immer wieder
neu eingreifen, sondern unser Programm soll eine komplexe
Anweisung auf einmal ausführen. Dafür müssen wir unseren
Code als Funktion definieren:
~~~python
def add_mult(a, b):
    output = a + b
    output = output + (a * b)
    return output
~~~

Eine Funktion besteht aus der Funktionsdefinition, die mit den Schlüssewort `def` eingeleitet und mit dem Doppelpunkt abgeschlossen wird.
Darin steht der Name der Funktion (hier `add_mult`) und die Namen der Argumente, abgetrennt durch Komma.
In dem Beispiel werden zwei Argumente `a` und `b` übergeben.

Der Funktionsdefinition folgt ein Code-Block, der die Funktion implementiert.
Der Block ist hier mit der `return` Anweisung abgeschlossen, die die Funktion beendet und den Rückgabewert definiert.

Nachdem eine Funktion definiert ist, kann sie im Code aufgerufen werden, genauso wie die eingebauten Funktionen auch.

~~~python
v = add_mult(1, 100)
print(v)
~~~

> ## Übung
> Schreiben Sie eine Funktion, die gegeben dreier Werte die Summe aller Zahlen zwischen dem ersten und dem zweiten Wert multipliziert mit dem dritten Wert angibt.
> Rufen Sie diese Funktion für verschiedene Werte auf und geben Sie die Werte aus.
>> ## Lösung
>> ~~~python
>> def complex_math(start, end, multiplier):
>>     sum = 0
>>     for i in range(start, end):
>>         sum = sum + (i*multiplier)
>>     return sum
>> 
>> print(complex_math(1,100, 1))
>> print(complex_math(20,100, 3))
>> print(complex_math(1,10, 3.14))
>> ~~~
>> ~~~
>> 4950
>> 14280
>> 141.3
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

Funktionen können Werte von verschiedenen Typen als Argument bekommen.
Auch kann die gleiche Funktion verschiedene Typen von Werten zurückgeben und je nach Bedingungen verschiedene
`return` Anweisungen ausführen (es wird aber immer nur die erste `return` Anweisung ausgeführt).

~~~python
def fancy_add(val):
    if isinstance(val, str):
        return  val + " + 1"
    elif isinstance(val, int):
        return val + 1
    elif isinstance(val, float):
        return val + 1.0
    else:
        return 42

print(fancy_add(2))
print(fancy_add(2.0))
print(fancy_add("2"))
print(fancy_add(False))
~~~
~~~
3
3.0
2 + 1
1
~~~
{: .output}

Der Code nutzt die eingebaute Funktion `isinstance` um zu überprüfen, ob eine Variable einen gegebenen Typ hat.

Außerdem ist es möglich, dass eine Funktion mehr als einen Wert zurückgibt. 
In diesem Fall muss die `return` Anweisung alle Werte mit Komma getrennt auflisten.
Die Zuweisung von mehreren Werten beim Aufruf einer Funktion erfolgt ebenfals durch Auflistung mit Komma.

~~~python
def get_str_info(text):
    l = len(text)
    n = len(set(text))
    return l, n

a, b = get_str_info("This is an arbitrary string, I swear")
~~~
~~~
36
16
~~~
{: .output}

> ## Frage
> Was bedeuten die Werte, die die Funktion zurückliefert?
{: .callout}

In Python wird unterschieden zwischen positionalen Argumenten, die übergeben werden müssen und Keyword-Argumenten, die optional sind und für die ein Standard-Wert in der Funktions-Definitions angegeben werden kann, der genutzt wird wenn das Argument nicht übergeben wird. 
Hier ein Beispiel:
~~~python
def print_log(log_text, with_exclamation_marks=False):
    out = log_text if not with_exclamation_marks else ('!!! '+log_text+' !!!')
    print(out)
    
print_log('Nothing happend.')
print_log('Alarm', with_exclamation_marks=True)
print_log('Alarm', True)
~~~
~~~
Nothing happend.
!!! Alarm !!!
!!! Alarm !!!
~~~
{: .output}
Der Standardwert für das Argument `with_exclamation_marks` ist hier `False`.

> ## Übung
> Wir wollen alle Nomen aus einer Geschichte und in eine Datei schreiben finden. 
> Dafür brauchen wir
> - eine Liste von Wörtern, die wir aus einem String (der
Geschichte) generieren
> - eine Definition von Nomen - wir gehen vereinfacht davon aus, dass
alle großgeschriebenen Wörter außer am Satzanfang
Nomen sind
>
> Die Geschichte nehmen wir von hier: [http://de.wikipedia.org/wiki/Der_Hase_und_der_Igel](http://de.wikipedia.org/wiki/Der_Hase_und_der_Igel)
>> ## Lösung
>> ~~~python	
>> # Unsere Funktion nimmt eine Liste als Parameter
>> def find_nouns(list_of_words):
>>     nouns = list()
>>     # Das erste Wort ist wahrscheinlich großgeschrieben, fällt aber aus unserer Definition raus
>>     for i in range(1, len(list_of_words)):
>>     	current_word = list_of_words[i]
>>     	if current_word[0].isupper():
>>             # list_of_words[i-1]: Das vorherige Wort
>>             if not list_of_words[i-1].endswith("."):
>>                 nouns.append(current_word)
>>     return nouns
>> 
>> 
>> with open("hase_igel.txt") as f:
>>     story = f.read()
>>     words = story.split()
>>     nouns = find_nouns(words)
>> 
>> with open("hase_igel_nouns.txt", "w") as result:
>>     for noun in nouns:
>>         result.write(noun + ", ")
>> ~~~
> {: .solution}
{: .challenge}


## Module und der `import` Befehl

### Eigene Module

Jede Python-Datei ist gleichzeitig eine sogenanntes *Modul*.
Man z.B. kann man das folgende Python-Skript mit dem Namen `poornlp.py` abspeichern:

~~~python
def get_str_info(text):
    l = len(text)
    n = len(set(text))
    return l, n

def is_noun(word):
    return word[0].isupper()
~~~

Dieses enthält jetzt die beiden Funktionen `get_str_info` und `is_noun`.
Durch das Speichern in der Datei haben wir ein Modul gleichen Names (`poornlp`) erzeugt.
Nun wollen wir diese Funktionen ja nachnutzen und nicht jedes mal in unsere Skripte kopieren.
Zum Laden der Funktion in ein eigenes Skript oder in die interaktive Konsole kann man den `import` Befehl benutzen.
Angenommen, das Skript mit dem Modul befindet sich im gleichen Ordner, dann kann man 
~~~python
import poornlp
~~~
aufrufen und bekommt Zugriff auf die beiden Funktionen über den Modulnamen, gefolgt von einem `.`:
~~~python
poornlp.get_str_info("Das ist ein Text")
~~~

Möchte man eine bestimmte Funktion aus einem Modul importieren, geht das mit `from ... import`:
~~~python
from poornlp import get_str_info
~~~
Danach ist es nicht mehr notwendig, für die importierte Funktion den Modulenamen anzugeben:
~~~python
get_str_info("Das ist ein Text")
~~~

Wenn das Modul in einem Unterordner liegt, kann man ebenfalls durch `import` darauf zugreifen, muss aber wieder einen Punkt zwischen dem Elternmodul (dem Ordner) und dem Kindermodul angeben.
Z.B. sei eine Ordnerstruktur mit einem Ordner `mathmodules` und zwei Python-Dateien in dem Ordner gegeben
~~~
mathmodules/
├── basic.py
└── fancy.py
~~~
basic.py:
~~~python
def add(a,b):
    return a + b
~~~
fancy.py:
~~~python
def add(val):
    if isinstance(val, str):
        return  val + " + 1"
    elif isinstance(val, int):
        return val + 1
    elif isinstance(val, float):
        return val + 1.0
    else:
        return 42
~~~

Der Import für `basic` sehe dann folgendermaßen aus:
~~~python
import mathmodules.basic
mathmodules.basic.add(5,10)
~~~
Auch Untermodule müssen importiert werden, z.B. würde
~~~python
mathmodules.fancy.add("A")
~~~
fehlschlagenn wenn nur `mathmodules` oder `mathmodules.basic`, aber nicht `mathmodules.fancy` importiert worden ist.
~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mathmodules' has no attribute 'fancy'
~~~
{: .output}

Manchmal sind die Modulnamen  sehr lang, dann kann man über `import ... as ...` abgekürzt werden
~~~python
import mathmodules.basic as mb
mb.add(42,3.13)
~~~

Ähnliches geht auch, wenn man Funktionsnamen mit `from ... import ... as ...` importiert, was sogar eine Umbennung der Funktion erlaubt und hilft Namenskonflikte aufzulösen:
~~~python
from mathmodules.fancy import add as fancy_add
fancy_add(42)
~~~

## Module der Standardbibliothek

Python besitzt neben den eingebauten Funktionen und Typen auch noch eine riesige sogenannte Standardbibliothek.
Dies sind Module, die in allen Python-Installationen (für eine bestimmte Version von Python) immer vorhanden sind.
Sie können also erwarten, dass Sie in jedem Skript diese Module importieren können.

Eine Auflistung und Dokumentation der Module der Standardbibliothek findet sich unter [https://docs.python.org/3.6/library/index.html](https://docs.python.org/3.6/library/index.html).

### Kommandozeilenargumente

Wenn man ein Skript  in der System-Konsole aufruft, kann man dem Aufruf zusätzliche per Leerzeichen getrennt Argumente übergeben.
~~~bash
python3 meinskript.py Argument1 NochEinArgument
~~~
Ähnlich wie bei einer Python-Funktion ist das sehr nützlich, um die gleiche Aufgabe bzw. den gleichen Algorithmus/Code auf unterschiedlichen Eingaben auszuführen. 
Wenn ein Skript eine Datei einliest, wäre das z.B. eine gute Möglichkeit den Dateipfad anzugeben, 
damit man das Skript auf verschieden Dateien ausführen kann ohne das Skript selbst fehleranfällig anpassen zu müssen.

Der Zugriff auf die Argumente erfolgt über die Liste `argv` aus dem Modul `sys`.

> ## Frage
> Wie können Sie auf diese Liste in ihren eigenem Skript zugreifen?
>> ## Lösung
>> ~~~pyhon
>> import sys
>> print(sys.argv)
>> ~~~
> {: .solution}
{: .callout}

Gegeben Sei das folgendes Skript in einer Datei `cat.py`. 
~~~python
import sys

print(sys.argv)
~~~
Wenn man das Skript nun mit verschiedenen Parametern auf dem System-Terminal ausführt ausführt, kann man sehen wie sich die Ausgabe verändert.
~~~bash
python3 cat.py
~~~
~~~output
['cat.py']
~~~
~~~bash
python3 /home/nlp/cat.py
~~~
~~~output
['/home/nlp/cat.py']
~~~
Das erste Element in der Liste `sys.argv` ist immer der Pfad, mit dem das Skript aufgerufen wurde, danach folgenden die anderen Argumente:
~~~bash
python3 cat.py Argument1 NochEinArgument
~~~
~~~output
['cat.py', 'Argument1', 'NochEinArgument']
~~~

Wenn Sie z.B. das Skript `cat.py` abändern, können Sie den Inhalt einer beliebigen Datei, die als Argument übergeben wird, als Text ausgeben:
~~~python
import sys

if len(sys.argv) < 2:
    print("No file given")
else:
    with open(sys.argv[1], 'r') as f:
        print(f.read())
~~~
Die Abfrage, ob die Argumentliste groß genug ist fängt den Fall ab, dass kein Argument angegeben worden ist.
Sie können jetzt das Skript austesten:

~~~bash
python3 cat.py hase_igel.txt
~~~
~~~output
Bei einer zufälligen Begegnung macht sich der Hase über die schiefen Beine des Igels lustig, woraufhin ihn dieser zu einem Wettrennen herausfordert,um den Einsatz eines goldenen „Lujedor“ (Louis d’or) und einer Flasche Branntwein. Bei der späteren Durchführung des Rennens auf einem Acker läuft der Igel nur beim Start ein paar Schritte, hat aber am Ende der Ackerfurche seine ihm zum Verwechseln ähnlich sehende Frau platziert. Als der siegesgewisse Hase heranstürmt, erhebt sich die Frau des Igels und ruft ihm zu: „Ick bün al hier!“ („Ich bin schon hier!“). Dem Hasen ist die Niederlage unbegreiflich, er verlangt Revanche und führt insgesamt 73 Läufe mit stets demselben Ergebnis durch. Beim 74. Rennen bricht er erschöpft zusammen und stirbt.
~~~

~~~bash
python3 cat.py
~~~
~~~
No file given
~~~
{: .output}

~~~bash
python3 cat.py nichtda.txt
~~~
~~~
Traceback (most recent call last):
  File "cat.py", line 6, in <module>
    with open(sys.argv[1], 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'nichtda.txt'
~~~
{: .output}

> ## Übung
> Schreiben Sie das Skript so um, dass es den Fehlerfall von nicht vorhanden Dateien auch abfängt.
>> ## Lösung
>> ~~~python
>> import sys
>> from os.path import exists
>> 
>> if len(sys.argv) < 2:
>>     print("No file given")
>> else:
>>     if exists(sys.argv[1]):
>>         with open(sys.argv[1], 'r') as f:
>>             print(f.read())
>>     else:
>>         print("Datei existiert nicht!")
>> 
>> ~~~
>> ~~~bash
>> python3 cat.py nichtda.txt
>> ~~~
>> ~~~
>> Datei existiert nicht!
>> ~~~
>> {: .output}
>{: .solution}
{: .challenge}

### Reguläre Ausdrücke auf Strings mit Modul `re`

Ein weiteres Beispiel für eine sehr nützliches Module aus der Standardbibliothek ist das Modul für reguläre Ausdrücke (also Mustersuche) mit dem Namen `re`.
Muster oder „Patterns“ müssen erst einmal erstellt („kompilliert“) werden und kann dann auf Strings angewendet werden.
~~~python
import re
pattern = re.compile('Glück.+')
search_in = 'Hallo, was für ein Glück, dass wir uns heute treffen!'
# gibt einen bool zurück, wenn der ganze String dem Pattern matched
is_match = pattern.match(search_in)   
# gibt bool zurück, wenn ein Teilstring dem Pattern matched
found = pattern.search(search_in)

if is_match:
    print('It is a full match!')
elif found_at:
    print('I found it somewhere!')
~~~
~~~
I found it somewhere!
~~~
{: .output}

Auf der [Dokumentation des Moduls `re` ](https://docs.python.org/3.6/library/re.html) gibt es eine Einführung in die Syntax dieser Patterns und wie man nicht nur ja/nein Suchen sondern auch die Position des Treffers bekommen kann. 

### Installation neuer Pakete mit `pip`

Hilfreiche Python-Pakete können z.B. über den „Python Package Index“ unter
[https://pypi.org](https://pypi.org) gefunden werden.
Die Installation auf dem lokalen System erfolgt dann mit dem Kommandozeilentool
`pip3` (um die Pakte für Python 3 zur Verfügung zu stellen).

Z.B. gibt es ein Paket um ASCII Art zu generieren:
[https://pypi.org/project/art/](https://pypi.org/project/art/)

Mit
~~~bash
pip3 install art
~~~
kann das Paket installiert werden.

Danach ist es über `import art` für eigene Python-Skripte oder auf der interaktiven Python-Konsole verfügbar:
~~~python
import art

print(art.text2art("Python"))
~~~
~~~
 ____          _    _                   
|  _ \  _   _ | |_ | |__    ___   _ __  
| |_) || | | || __|| '_ \  / _ \ | '_ \ 
|  __/ | |_| || |_ | | | || (_) || | | |
|_|     \__, | \__||_| |_| \___/ |_| |_|
        |___/                           
~~~
{: .output}

