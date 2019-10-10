---
title: "Eigene Funktionen und Module"
teaching: 60
exercises: 0
questions:
- Wie kann ich selbst eigene Funktionen definieren?
- Wie können Funktionen aus externen Bibliotheken eingebunden werden?' 
objectives:
- Funktionalität von Programmen nachnutzen
keypoints:
- Mit Funktionen können Teile von Programmen ausgegliedert und nachgenutzt werden.
- Eigene Module können in Python-Dateien abgespeichert und mit `import` in anderen Python-Skripten nachgenutzt werden.
- Mit `pip` können neue Pakete, die Module enthalten, installiert werden.
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
>>     summe = 0
>>     for i in range(start, end):
>>         summe = summe + (i*multiplier)
>>     return summe
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
    c = text[0]
    return l, n

a, b = get_str_info("This is an arbitrary string, I swear")
~~~
~~~
36
T
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


## Module und der `import` Befehl

### Eigene Module

Jede Python-Datei ist gleichzeitig eine sogenanntes *Modul*.
Man z.B. kann man das folgende Python-Skript mit dem Namen `poornlp.py` abspeichern:

~~~python
def get_str_info(text):
    l = len(text)
    c = text[0]
    return l, c

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


### Reguläre Ausdrücke auf Strings mit Modul `re`

Ein Beispiel für eine sehr nützliches Module aus der Standardbibliothek ist das Modul für reguläre Ausdrücke (also Mustersuche) mit dem Namen `re`.
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
elif found:
    print('I found it somewhere!')
~~~
~~~
I found it somewhere!
~~~
{: .output}

Auf der [Dokumentation des Moduls `re` ](https://docs.python.org/3.6/library/re.html) gibt es eine Einführung in die Syntax dieser Patterns und wie man nicht nur ja/nein Suchen sondern auch die Position des Treffers bekommen kann. 

## Module aus Anaconda

Anaconda ist eine Python-Distribution, in der bereits viele Pakete für NLP, Machine Learning und Data Science vorinstalliert sind.
Im Anaconda Navigator kann man über „Environments“ 
- überprüfen welche Pakete bereits vorhanden sind
- die installierten Pakete aktualisieren
- neue Pakete aus Anaconda installieren

![Anaconda Paketmanager](../fig/anaconda-install.png)

### Installation neuer Pakete mit `pip`

Hilfreiche allgemeine Python-Pakete können z.B. über den „Python Package Index“ unter
[https://pypi.org](https://pypi.org) gefunden werden.
Die Installation auf dem lokalen System erfolgt dann mit dem Kommandozeilentool
`pip`.

Z.B. gibt es ein Paket um ASCII Art zu generieren:
[https://pypi.org/project/art/](https://pypi.org/project/art/)

Mit
~~~bash
pip install art
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


{% include links.md %}