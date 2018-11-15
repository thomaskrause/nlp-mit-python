---
title: "Texte in NLTK"
teaching: 0
exercises: 0
questions:
objectives:
keypoints:
---

Das NLTK besteht aus verschiedenen Modulen für
verschiedene Aufgaben, z.B. `nltk.corpora`, `nltk.parse` oder `nltk.stem`. 
Eine Übersicht der Module finden Sie z.B. im [Vorwort](http://www.nltk.org/book/ch00.html) des NLTK-Buchs

## Download von NLTK-Ressourcen

Es gibt zusätzlich eine Datenkollektion (Korpora und anderes), die für das NLTK-Buch zusammengestellt wurde.
Um diese herunterzuladen, öffnen Sie eine Python-Konsole und führen Sie folgenden Code aus:

~~~python
import nltk
nltk.download()
~~~

Es erscheint eine graphische Oberfläche, auf der Sie die „Collection“ „book“ auswählen müssen und dann über die Schaltfläche „Download“ herunterladen können.
Danach können Sie die verschiedenen Korpora in Python importieren, in dem Sie
~~~python
from nltk.book import *
~~~
ausführen.
~~~
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
~~~
{: .output}
Nach dem Import sind die verschiedenen Korpora als Variablen mit dem Namen `text1`, `text2` etc. vorhanden.

> ## Frage(n)
> Welchen Typ haben diese Variablen?
{: .discussion}

## Texte als Sequenzen von Wörtern

Wir haben bereits Zeichenketten als Sequenzen von Zeichen betrachtet.
In Korpora wird typischerweise bereits ein weiter Vorverarbeitungsschritt vorausgesetzt, nämlich
dass die Texte in Token unterteilt sind.
Token sind typischerweise Wörter und Punktuationen.
Ein Text ist dann eine Sequenz von Token und kann wie eine Liste interpretiert werden.
Obwohl der Typ von NLTK-Texten `nltk.text.Text` ist, kann man die Variablen wie eine Liste von Zeichenketten nutzen.

Man kann sich zum Beispiel die ersten 10 Wörter eines Textes über die Listen-Indexierung (`[n:m]`) ausgeben lassen.
~~~python
text4[0:10]
~~~
~~~
['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', 'and', 'of', 'the', 'House']
~~~
{: .output}

Die Ausgabe ist wiederum von Typ `list`.
~~~python
type(text4[0:10])
~~~
~~~
<class 'list'>
~~~
{: .output}


## Suche in Texten

Wenn man nun nach „einen Wort in einem Text“ suchen möchte, kann das mehrere Dinge heißen:
- Ist ein Wort überhaupt in einem Text enthalten?
- An welcher Stelle ist ein Wort in einem Text enthalten?
- Wie oft ist ein Wort in einem Text enthalten?

### Prüfen ob Element enthalten ist über den `in` Ausdruck

Mit dem Ausdruck `wert in liste` kann überprüft werden, ob ein Element in einer Liste vorhanden ist.

~~~python
nachspeisen = ["Obst", "Quark", "Eis"]
if "Obst" in nachspeisen:
  print("Heute mal gesund.")
else:
  print("Esst mehr Obst!")
~~~

Da NLTK-Texte Listen von Zeichenketten sind, kann man mit `in` auch überprüfen, ob ein Wort im Text vorhanden ist.

> ## Übung
> Überprüfen Sie, ob irgendeiner Antrittsrede eines US-Präsidenten das Wort „fruit“ vorkommt.
>> ## Lösung
>> Ja, denn
>> ~~~python
>> "fruit" in text4
>> ~~~
>> ergibt `True`.
> {: .solution}
{: .challenge}

### Stelle finden, an dem ein Wort im Text vorkommt

Mit der Funktion `text.index(wert)` kann das erste Vorkommen eines Wortes im Text als Index der Liste gefunden werten
~~~python
i = text4.index("fruit")
print(i)
print(text4[i-1], text4[i], text4[i+1])
~~~
~~~
13694
the fruit of
~~~
{: .output}

### Zählen wie oft ein Wort im Text enthalten ist

Mit der Funktion `text.count(wert)` kann gezählt werden, wie oft ein Wort im Text vorkommt.
~~~python
text4.count("fruit")
~~~
~~~
2
~~~
{: .output}

### Komplexere Bedigungen abfragen

Man kann für jedes Wort des Textes eine Bedingung überprüfen, in dem man mit einer for-Schleife über die Wörter des Textes iteriert
und für jedes Wort eine if-Abfrage ausführt.

~~~python
from nltk.book import text4
for word in text4:
    if word.startswith("fr"):
        print(word)
~~~
~~~
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
from
frequent
from
from
from
free
from
free
from
freemen
from
from
from
frankly
from
from
frontier
from
friends
from
from
fresh
from
from
from
free
[...]
~~~
{: .output}

Eleganter (und schneller) ist aber die Verwendung einer sogenannten „list comprehension“, einer aussagelogischen Abfrage:
~~~python
[word for word in text4 if w.startswith("fr")]
~~~
~~~
['from', 'frequent', 'from', 'from', 'from', 'free', 'from', 'free', 'from', 'freemen', 'from', 'from', 'from', 'frankly', 'from', 'from', 'frontier', 'from', 'friends', 'from', 'from', 'fresh', 'from', 'from', 'from', 'free', 'fraud', 'fruits', 'from', 'free', 'from', 'friendly', 'friendly', 'friendship', 'friendship', 'fruitful', 'from', 'freely', 'from', 'free', 'free', 'from', 'from', 'from', 'from', 'frugal', 'from', 'free', 'from', 'friendship', 'from', 'freedom', 'freedom', 'freedom', 'from', 'from', 'freedom', 'from', 'from', 'friendship', 'from', 'from', 'frontiers', 'from', 'friendly', 'free', 'from', 'from', 'friends', 'from', 'freedom', 'freedom', 'from', 'friend', 'from', 'from', 'from', 'from', 'friendship', 'from', 'from', 'free', 'from', 'fruits', 'from', 'from', 'friendly', 'free', 'from', 'freedom', 'friendly', 'from', 'from', 'from', 'from', 'from', 'from', 'free', 'from', 'from', 'from', 'free', 'from', 'fraught', 'from', 'from', 'from', 'from', 'friendship', 'from', 'from', 'from', 'frontiers', 'from', 'from', 'free', 'from', 'from', 'fruit', 'from', 'friendly', 'free', 'from', 'from', 'from', 'from', 'frontiers', 'frontiers', 'from', 'from', 'front', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'friendship', 'free', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'free', 'from', 'from', 'from',
[...]
~~~
{: .output}

Der grundsätzliche Aufbau des Ausdrucks ist 
~~~python
[ausdruck for element in liste if bedingung]
~~~
Für jedes `item` in der `liste` wird der `ausdruck` ausgeführt, wenn die `bedingung` wahr ist.

Man kann für die Bedingung auch reguläre Ausdrücke verwenden, wenn man das `re` Modul importiert und 
die `re.search(pattern, word)` Funktion verwendet.

Z.B. kann man nach allen Wörtern suchen, die mit „fruit“ anfangen, aber noch mehre Zeichen enthalten können:
~~~python
import re
[print(w) for w in text4 if re.search("fruit.*", w)]
~~~
~~~
fruits
fruitful
fruits
fruit
fruits
fruitful
fruitful
fruits
[...]
~~~
{: .output}

Oder z.B. die Suche nach allen Wörtern, die mit „end“ oder „begin“ enden:
~~~python
[print(w) for w in text4 if re.search(".+(end|begin)$", w)]
~~~
~~~
recommend
depend
depend
comprehend
extend
extend
contend
tend
friend
contend
depend
depend
depend
extend
depend
[...]
~~~
{: .output}

## Mengen

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

Wenn man Texte mit einer komplexen Bedingung durchsucht, kann man die daraus entstandene Liste zu einer Menge machen, um jeder Variante nur noch einmal vorkommen zu lassen:

~~~python
import re
from nltk.book import text4

words = [w for w in text4 if re.search(".+(end|begin)$", w)]
words = set(words)
print(words)
~~~
~~~
{'comprehend', 'lend', 'recommend', 'tend', 'dividend', 'Godsend', 'attend', 'send', 'spend', 'rend', 'trend', 'friend', 'Reverend', 'apprehend', 'extend', 'contend', 'reverend', 'legend', 'intend', 'transcend', 'blend', 'depend', 'defend', 'superintend', 'pretend', 'bend'}
~~~
{: .output}