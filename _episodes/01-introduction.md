---
title: "Einfache Anweisungen und Datentypen"
teaching: 0
exercises: 0
questions:
- "Wie kann man einfache Anweisungen in Python ausführen?"
- "Was sind Datentypen?"
objectives:
- "Umgang mit der Python-Konsole"
- "Datentypen verstehen"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

# Python starten

Zum Kennenlernen arbeiten wir zunächst nur auf der interaktiven Kommandozeile (Konsole) des Python-Interpreters. Diese wird gestartet, indem wir ein Terminal (kann unter Ubuntu z.B. mit dem Shortcut  <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> gestartet werden) öffnen und folgendes eintippen:

~~~bash
python3
~~~


Das Ergebnis sollte ungefähr so aussehen:
~~~
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~
{: .output}

Die Versionen von Python und GCC werden wahrscheinlich nicht überall identisch sein. Wichtig: Python muss in Version 3.6.x vorliegen.


# Kommentare und Dokumentation

Kommentieren Sie ihren eigenen Code und dokumentieren Sie somit dessen Funktionsweise. Das erleichtert anderen und auch Ihnen, den Code später noch zu verstehen. Außerdem können auf diese Weise Voraussetzungen Ihres Programms an die Eingabe und eine Darlegung der Form des Outputs dargelegt werden. Kommentare im Code beginnen Sie mit einer `#`.

Ein Beispiel:

~~~python
# Das ist ein Kommentar
# This is a comment
~~~

> ## Sprache in Python-Skripten
>
> Es ist üblich Kommentare und andere Element des Programmskripts
> in Englisch zu halten, da sie so für ein
> breiteres Publikum verständlich sind. Im Rahmen dieses Kurses können
> Sie das aber ignorieren. Sie sollten lediglich sicherstellen, dass 
> Ihre Kommilitonen, Ihre Dozentin und Ihr Tutor Sie/sie verstehen :)
{: .callout}

# Ganze Zahlen und Kommazahlen

Zunächst wollen wir testen, wie die Python-Konsole auf Dateneingaben reagiert. Dafür tippen wir eine x-beliebige Zahl ein und drücken die Eingabetaste <kbd>Return</kbd>:

~~~python
12
~~~
Der Python-Interpreter gibt nun folgende Ausgabe als Antwort:
~~~
12
~~~
{: .output}

Die Python-Konsole berechnet für uns 12. Das klingt nur so merkwürdig, weil es an 12 nichts mehr zu berechnen gibt, weshalb Ein- und Ausgabe identisch sind. 

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

{% include links.md %}

