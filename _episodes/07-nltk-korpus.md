---
title: "Texte in NLTK"
teaching: 130
exercises: 0
questions:
- Wie werden Text in NLTK dargestellt?
- Wie kann man auf diese Texte zugreifen?
- Was kann man mit den Texten an einfachen statistischen Auswertungen durchführen?
objectives:
- Laden der vorgefertigten NLTK Buch Beispieltexte
- Einfache Auswertungen auf diesen Texten
keypoints:
- Texte sind Sequenzen von Token  und können wir Listen von Strings behandelt werden
- Es ist in NLTK direkt möglich, Frequenzanalysen, Kollokationen und andere einfache statistische Auswertungen auf Texten durchzuführen.
---

Das NLTK besteht aus verschiedenen Modulen für
verschiedene Aufgaben, z.B. `nltk.corpora`, `nltk.parse` oder `nltk.stem`. 
Eine Übersicht der Module finden Sie z.B. im [Vorwort](http://www.nltk.org/book/ch00.html) des [NLTK-Buchs](http://www.nltk.org/book/).
Viele Beispiele sind auch aus dem [NLTK-Buch](http://www.nltk.org/book/) übernommen, und es lohnt sich, als Nachbereitung die Kapitel 1 bis 3 durchzulesen. 

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
>
>> ## Lösung
>> Wir können den Typ einfach mit `type(text1)` überprüfen.
>> Die Variablen mit den Texten haben *nicht* den Typ String, sondern den NLTK-eigenen Typ `nltk.text.Text`.
>> Welche Methoden wir auf diesen Typ nutzen können, schauen wir uns im Rest des Tutorials an.
> {: .solution}
{: .discussion}

## Texte als Sequenzen von Wörtern

Wir haben bereits Zeichenketten als Sequenzen von Zeichen betrachtet.
In Korpora wird typischerweise bereits ein weiterer Vorverarbeitungsschritt vorausgesetzt, nämlich
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
[word for word in text4 if word.startswith("fr")]
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
Das Ergebnis ist eine Liste aller Werte, die durch den Ausdruck generiert werden.
~~~python
fr_woerter = [word for word in text4 if word.startswith("fr")]
print(fr_woerter)
print(type(fr_woerter))
~~~
~~~
[...]
'from', 'freedom', 'free', 'freedom', 'freedom', 'freedom', 'free', 'freedom', 'friendship', 'free', 'freedom', 'free', 'freedom', 'freedom', 'free', 'fragile', 'freedom', 'freedom', 'free', 'freedom', 'from', 'freedom', 'freedom', 'from', 'freedom', 'freedom', 'freedom', 'freedom', 'free', 'freedom', 'freedom', 'freedom', 'from', 'free', 'freedom', 'free', 'freedom', 'from', 'friend', 'from', 'friends', 'from', 'from', 'friend', 'freedom', 'freedom', 'from', 'free', 'free', 'from', 'freedoms', 'from', 'free', 'freedom', 'free', 'friendsâ', 'from', 'from', 'freedom', 'freedom', 'freedom', 'from', 'from', 'from', 'from', 'from', 'freedom', 'from', 'from', 'from', 'from', 'from', 'friendship', 'from', 'free', 'from', 'freedoms', 'from', 'from']
<class 'list'>
~~~
{: .output}

Ein Aufruf von `print` innerhalb der „list comprehension“ funktioniert daher in der interaktiven Konsole, 
die immer den Rückgabewert ausgibt, nur bedingt.
~~~python
[print(word) for word in text4 if word.startswith("friends")]
~~~
~~~
friends
friendship
friendship
friendship
friendship
friends
friendship
friendship
friendship
friends
friendship
friendship
friendship
friends
friends
friendship
friendship
friendship
friends
friends
friends
friendship
friends
friends
friendship
friendship
friends
friends
friends
friends
friends
friends
friends
friendship
friendship
friends
friends
friendships
friends
friendship
friends
friends
friends
friends
friends
friends
friendship
friends
friends
friends
friends
friends
friendships
friends
friends
friendship
friends
friendsâ
friendship
Out[6]: 
[None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None]
~~~
{: .output}
„List comprehension“ Ausdrücke sind also am besten dazu geeignet, Listen zu generieren.

Man kann für die Bedingung auch reguläre Ausdrücke verwenden, wenn man das `re` Modul importiert und 
die `re.search(pattern, word)` Funktion verwendet.

Z.B. kann man nach allen Wörtern suchen, die mit „fruit“ anfangen, aber noch mehre Zeichen enthalten können:
~~~python
import re
[w for w in text4 if re.search("fruit.*", w)]
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
[w   for w in text4 if re.search(".+(end|begin)$", w)]
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

## Konkordanz auf NLTK-Texten

Das NLTK hat eine eigene Konkordanzfunktion:
~~~python
text4.concordance("fruit")
~~~
~~~
Displaying 2 of 2 matches:
as we do all the raw materials , the fruit of our own soil and industry , we ou
ce will grow greater and bear richer fruit with the coming years . No doubt thi
~~~
{: .output}

Damit können die gefunden Stellen gemeinsam mit ihren Kontext angezeigt werden. 
In diesem Fall ist der Kontext durch die Wörter/Zeichen links und rechts vom Treffer gegeben.

Die Konkordanzfunktion arbeitet auf tokenisiertem Text - sie
kann deshalb nicht über mehrere Wörter suchen:
~~~python
text4.concordance("fruit of")
~~~
~~~
no matches
~~~
{: .output}
liefert keine Matches, weil es das Token „fruit of“ nicht gibt!

Die Konkordanzfunktion funktioniert nur auf der Datenstruktur
Text, die vom NLTK vorgegeben wird.

> ## Übung
> Wie können wir uns den Kontext für das Ergebnis einer Mustersuche ausgeben lassen?
>> ## Lösung
>> ~~~python
>> words = set([w for w in text4 if re.search(".+(end|begin)$", w)])
>> for w in words:
>>     text4.concordance(w)
>> ~~~
> {: .solution}
{: .challenge}

## Vorkommen eines Worts im Text

Wenn man eine Übersicht haben möchte, an welchen Stellen ein Wort im Text vorkommt, kann man einen sogenannten „dispersion plot“ nutzen:

~~~python
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
~~~

## Einfache statistische Auswertungen


### Wortfrequenzen

Um die Frequenz der Wörter für ein Korpus berechnen, kann man mit der Funktion `Freqdist(text)` ein neues Objekt anlegen, dass die Vorkommen zählt und die Möglichkeit gibt, auf verschiedene Aspekte der Frequenzanalyse zuzugreifen.

~~~python
fdist1 = FreqDist(text1)
print(fdist1)
~~~
~~~
<FreqDist with 19317 samples and 260819 outcomes>
~~~
{: .output}

Mit der Methode `.most_common(n)` kann man sich jetzt die `n` häufigsten Wörter ausgeben lassen.
~~~python
fdist1.most_common(50)
~~~
~~~
[(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024), ('a', 4569), ('to', 4542), (';', 4072), ('in', 3916), ('that', 2982), ("'", 2684), ('-', 2552), ('his',2459), ('it', 2209), ('I', 2124), ('s', 1739), ('is', 1695), ('he', 1661), ('with', 1659), ('was', 1632), ('as', 1620), ('"', 1478), ('all', 1462), ('for', 1414), ('this', 1280), ('!', 1269), ('at', 1231), ('by', 1137), ('but', 1113), ('not', 1103), ('--', 1070), ('him', 1058), ('from', 1052), ('be', 1030), ('on', 1005), ('so', 918), ('whale', 906), ('one', 889), ('you', 841), ('had', 767), ('have', 760), ('there', 715), ('But', 705), ('or', 697), ('were', 680), ('now', 646), ('which', 640), ('?', 637), ('me', 627), ('like',624)]
~~~
{: .output}

Über einen Indexzugriff kann man auch die Häufigkeit eines gegebenen Wortes ausgeben:
~~~python
fdist1['whale']
~~~
~~~
906
~~~
{: .output}

Man kann die Frequenzen auch wieder plotten lassen:
~~~python
print(len(text1))
fdist1.plot(50)
~~~
~~~
260819
~~~
{: .output}

Wenn man die Häufigkeiten der häufigsten 50 Wörter aufaddiert kann man sehen, dass diese
fast die Hälfte des Gesamttextes umfassen.
~~~python
print(len(text1))
fdist1.plot(50, cumulative=True)
~~~
~~~
260819
~~~
{: .output}


### Durchschnittliche Wortlänge

Man kann mit `FreqDist()` auch andere Dinge berechnen, wie z.B. die Verteilung der Wortlänge eines Textes.
Dazu erstellen wir zuerst ein neue List, in der für jedes Wort des Textes die Länge eingetragen ist.

> ## Übung
> Erstellen Sie eine Liste mit den Wortlängen des Textes `text1`!
>> ## Lösung
>> ~~~python
>> l = [len(w) for w in text1]
>> print(l)
>> ~~~
>> ~~~
>> [1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, ...]
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

Jetzt können wir die Frequenz der verschiedenen Wortlängen direkt berechnen:
~~~python
ldist = FreqDist(l)
print(ldist.most_common(10))
ldist.plot()
~~~
~~~
[(3, 50223), (1, 47933), (4, 42345), (2, 38513), (5, 26597), (6, 17111), (7, 14399), (8, 9966), (9, 6428), (10, 3528)]
~~~
{: .output}

Wir können auch direkt die häufigste Wortlänge mit der Methode `.max()` berechnen lassen:
~~~python
ldist.max()
~~~
~~~
3
~~~
{: .output}

### Kollokation

Kollokationen sind Sequenzen von ungewöhnlich häufig zusammen auftretenden Wörtern.
Sequenzen von Wörtern, bei denen jedes einzelne Wort bereits häufig auftritt sind keine auffälligen Kollokationen, z.B. sind „the“ und „wine“ in einem Text vielleicht einzeln schon sehr häufig, deswegen ist klar, dass „the wine“ ebenfalls häufig auftritt und keine Kollokation.
Dagegen ist „red wine“ eine, da die Sequenz der beiden Wörter häufiger auftritt als die einzelne Frequenz der beiden Wörter dies erwarten lassen würde. 

Ein Beispiel für die Frequenz von „the“, „wine“ und „red“ in einem der Texte:
~~~python
print(fdist1["the"])
print(fdist1["wine"])
print(fdist1["red"])
~~~
~~~
13721
12
36
~~~
{: .output}

Nun ist die Frage, wie man die Häufigkeit von „red wine“ finden kann.
Als erstes muss man eine Liste von sogenannten Bigrammen erstellen, also alle
Paare von Wörtern die jeweils als Sequenz im Text vorkommen. 
Bigramme können mit Methode `bigrams(text)` erstellt werden.
~~~python
for b in bigrams(text1):
  print(b)
~~~
~~~
('Nantucket', 'commanders')
('commanders', ';')
(';', 'that')
('that', 'from')
('from', 'the')
('the', 'simple')
('simple', 'observation')
('observation', 'of')
('of', 'a')
[...]
~~~
{: .output}

Die einzelnen Bigramme sind vom Typ Tupel, den wir bisher noch nicht kennengelernt haben.
Tupel sind ähnlich wie Listen, allerdings ist die Anzahl der Element fest und es können nicht
neue Element angehängt oder bestehende gelöscht werden.
Ein Tupel-Wert kann in Python mit Hilfe von Klammern angelegt werden.
~~~python
t = ("red", "wine")
type(t)
print(t)
print(t[0])
print(t[1])
~~~
~~~
<class 'tuple'>
('red', 'wine')
'red'
'wine'
~~~
{: .output}

Listen von Bigrammen können nun ähnlich wie Listen von Wörtern behandelt werden, indem z.B.
Frequenzlisten davon erstellt und ausgewertet werden.

~~~python
bf = FreqDist(bigrams(text1))
print(bf.most_common(10))
print(bf[("red", "wine")])
print(bf[("the", "wine")])
~~~
~~~
[((',', 'and'), 2607), (('of', 'the'), 1847), (("'", 's'), 1737), (('in', 'the'), 1120), ((',', 'the'), 908), ((';', 'and'), 853), (('to', 'the'), 712), (('.', 'But'), 596), ((',', 'that'), 584), (('.', '"'), 557)]
1
0
~~~
{: .output}

Während „the“ häufiger vorkommt als „red“, gibt es kein einziges Bigramm „the wine“ in diesem Text, während „red wine“ einmal vorkommt.
Damit ist „red wine“ eine Kollokation.

Nun kann man für einen Text direct mit der Methode `.collocation_list()` häufige Bigramme finden.
~~~python
text4.collocation_list()
~~~
~~~
United States; fellow citizens; four years; years ago; Federal
Government; General Government; American people; Vice President; Old
World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
God bless; every citizen; Indian tribes; public debt; one another;
foreign nations; political parties
~~~
{: .output}

~~~python
text8.collocation_list()
~~~
~~~
would like; medium build; social drinker; quiet nights; non smoker;
long term; age open; Would like; easy going; financially secure; fun
times; similar interests; Age open; weekends away; poss rship; well
presented; never married; single mum; permanent relationship; slim
build
~~~
{: .output}

{% include links.md %}