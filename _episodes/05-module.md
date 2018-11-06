---
title: "Module"
teaching: 0
exercises: 0
questions:
- Wie können Funktionen aus externen Bibliotheken eingebunden werden?' 
objectives:
- Funktionalität von Programmen nachnutzen
keypoints:
- Eigene Module können in Python-Dateien abgespeichert und mit `import` in anderen Python-Skripten nachgenutzt werden.
- Mit `pip3` können neue Pakete, die Module enthalten, installiert werden.
---

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
elif found_at:
    print('I found it somewhere!')
~~~
~~~
I found it somewhere!
~~~
{: .output}

Auf der [Dokumentation des Moduls `re` ](https://docs.python.org/3.6/library/re.html) gibt es eine Einführung in die Syntax dieser Patterns und wie man nicht nur ja/nein Suchen sondern auch die Position des Treffers bekommen kann. 

## Installation neuer Pakete mit `pip`

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

