---
title: "NLTK und eigene Texte"
teaching: 50
exercises: 10
questions:
- Wie kann ich meine eigenen Texte in NLTK einbinden?
objectives:
- Tokensieren von Texten
- Auf Argumente der Kommandozeile zugreifen
keypoints:
- Listen von Strings können mit `nltk.Text()` zu einem NLTK-Text umgewandelt werden.
- Kommandozeilenargumente können über die Liste `sys.argv` abgerufen werden. Das erste Element ist immer der Aufrufpfad des Skripts.
---


## Einlesen eines eigenen Texts in NLTK

Wir wollen einen Beispieltext als Text in NLTK laden.
Dafür müssten wir als erstes eine Liste von allen Wörtern des Textes in der richtigen Reihenfolge erstellen.
Das heißt, dass wenn wir den Text zeilenweise einlesen, die Zeichenketten auftrennen müssen.
Eine einfache Methode dazu bietet die eingebaute `split()` Methode von Python.
Diese Methode kann aber z.B. nicht mit Punktuation umgehen.

~~~python
feedback = "Die positivste Reaktion, die man in Berlin bekommen kann, ist eine fehlende Beschwerde."
feedback.split()
~~~
~~~
['Die', 'positivste', 'Reaktion,', 'die', 'man', 'in', 'Berlin', 'bekommen', 'kann,', 'ist', 'eine', 'fehlende', 'Beschwerde.']
~~~
{: .output}

NLTK bietet eine Funktion `word_tokenize(text)`, die diese Aufgabe besser löst.
~~~python
from nltk import word_tokenize
word_tokenize(feedback)
~~~
~~~
['Die', 'positivste', 'Reaktion', ',', 'die', 'man', 'in', 'Berlin', 'bekommen', 'kann', ',', 'ist', 'eine', 'fehlende', 'Beschwerde', '.']
~~~
{: .output}

Die Funktion `nltk.Text` erstellt aus so einer Liste von Wörtern dann einen neuen Text,
der genau so wie alle anderen Texte genutzt werden kann.
~~~python
txt_de = nltk.Text(word_tokenize(feedback))
txt_de.concordance("Reaktion")
nltk.FreqDist(txt_de).plot()
~~~
~~~
Displaying 1 of 1 matches:
Die positivste Reaktion , die man in Berlin bekommen kann ,
~~~
{: .output}

Eine Möglichkeit, Text weiter zu verarbeiten ist das Tagging jedes Tokens nach Wortarten.
Dazu erstellen wir erst einen Text aus einen einfachen englischen Beispielsatz.
~~~python
txt_en = nltk.Text(word_tokenize("The most positive reaction you can get in Berlin is a missing complaint."))
txt_en.tokens
~~~
~~~
['The', 'most', 'positive', 'reaction', 'you', 'can', 'get', 'in', 'Berlin', 'is', 'a', 'missing', 'complaint', '.']
~~~
{: .output}

Die Funktion `nltk.pos_tag(text)`  erlaubt jetzt das taggen eines englischen Texts:
~~~python
nltk.pos_tag(txt_en)
~~~
~~~
[('The', 'DT'), ('most', 'RBS'), ('positive', 'JJ'), ('reaction', 'NN'), ('you', 'PRP'), ('can', 'MD'), ('get', 'VB'), ('in', 'IN'), ('Berlin', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('missing', 'JJ'), ('complaint', 'NN'), ('.', '.')]
~~~
{: .output}
Das Ergebnis ist eine Liste von Tupeln, wobei das erste Element das Token ist und das zweite der Tag für die Wortklasse. 
Das hier verwendete Tagset ist as [UPenn Tagset](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
Mit `nltk.help.upenn_tagset(tag)` kann man für eine einzelnes Tag die Beschreibung bekommen.
~~~python
nltk.help.upenn_tagset('NN')
~~~
~~~
NN: noun, common, singular or mass
    common-carrier cabbage knuckle-duster Casino afghan shed thermostat
    investment slide humour falloff slick wind hyena override subhumanity
    machinist ...
~~~
{: .output}

Wir werden uns später damit beschäftigen, wie diese Tagger funktionieren.
Tagsets können über den optionalen Parameter `tagset` ausgewählt werden, z.B. gibt es auch das „[Universal POS Tagset](http://universaldependencies.org/u/pos/)“

~~~python
nltk.pos_tag(txt_en, tagset="universal")
~~~
~~~
[('The', 'DET'), ('most', 'ADV'), ('positive', 'ADJ'), ('reaction', 'NOUN'), ('you', 'PRON'), ('can', 'VERB'), ('get', 'VERB'), ('in', 'ADP'), ('Berlin', 'NOUN'), ('is', 'VERB'), ('a', 'DET'), ('missing', 'ADJ'), ('complaint', 'NOUN'), ('.', '.')]
~~~
{: .output}

Um den Tagger für eine andere Sprache zu nutzen, muss das Argument `lang` mit angeben werden.
Als Argument muss der aus drei Buchstaben bestehende [ISO 639 Code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) genutz werden, z.B. für Deutsch:
~~~python
nltk.pos_tag(txt_de, tagset="universal", lang="deu")
~~~
~~~
NotImplementedError: Currently, NLTK pos_tag only supports English and Russian (i.e. lang='eng' or lang='rus')
~~~
{: .output}
In älteren Versionen von NLTK war ein sehr rudimentäre Tagger für Deutsch enthalten.
Dieser wurde allerdings entfernt.
Für das Beispiel hätte der alte POS-Tagger 
~~~
[('Die', 'NOUN'), ('positivste', 'NOUN'), ('Reaktion', 'NOUN'), (',', '.'), ('die', 'NOUN'), ('man', 'NOUN'), ('in', 'ADP'), ('Berlin', 'NOUN'), ('bekommen', 'NOUN'), ('kann', 'VERB'), (',', '.'), ('ist', 'ADJ'), ('eine', 'NOUN'), ('fehlende', 'NOUN'), ('Beschwerde', 'NOUN'), ('.', '.')]
~~~
{: .output}
ausgegeben.
Wir Sie sehen, war der Tagger für Deutsch ausbaufähig und seine Entfernung kein großer Verlust.

## Kommandozeilenargumente


Wenn man ein Skript  in der System-Konsole aufruft, kann man dem Aufruf zusätzliche per Leerzeichen getrennt Argumente übergeben.
~~~bash
python3 meinskript.py Argument1 NochEinArgument
~~~

Ähnlich wie bei einer Python-Funktion ist das sehr nützlich, um die gleiche Aufgabe bzw. den gleichen Algorithmus/Code auf unterschiedlichen Eingaben auszuführen. 
Wenn ein Skript eine Datei einliest, wäre das z.B. eine gute Möglichkeit den Dateipfad anzugeben, 
damit man das Skript auf verschieden Dateien ausführen kann ohne das Skript selbst fehleranfällig anpassen zu müssen.

Der Zugriff auf die Argumente erfolgt über die Liste `argv` aus dem Modul `sys`.
Dazu müssen Sie das Modul erst importieren, und können dann auf die Listen-Variable zugreifen.
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
~~~
Bei einer zufälligen Begegnung macht sich der Hase über die schiefen Beine des Igels lustig, woraufhin ihn dieser zu einem Wettrennen herausfordert,um den Einsatz eines goldenen „Lujedor“ (Louis d’or) und einer Flasche Branntwein. Bei der späteren Durchführung des Rennens auf einem Acker läuft der Igel nur beim Start ein paar Schritte, hat aber am Ende der Ackerfurche seine ihm zum Verwechseln ähnlich sehende Frau platziert. Als der siegesgewisse Hase heranstürmt, erhebt sich die Frau des Igels und ruft ihm zu: „Ick bün al hier!“ („Ich bin schon hier!“). Dem Hasen ist die Niederlage unbegreiflich, er verlangt Revanche und führt insgesamt 73 Läufe mit stets demselben Ergebnis durch. Beim 74. Rennen bricht er erschöpft zusammen und stirbt.
~~~
{: .output}

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

{% include links.md %}