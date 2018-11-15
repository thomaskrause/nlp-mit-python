---
title: "NLTK und eigene Texte"
teaching: 0
exercises: 0
questions:
- Wie können Dateien durch Python verarbeitet werden?
- Wie kann ich meine eigenen Texte in NLTK einbinden?
objectives:
- Ein- und Auslesen von Dateien
- Auf Argumente der Kommandozeile zugreifen
- Tokensieren von Texten
keypoints:
- Mit den eingebauten Funktionen `open` können Dateien zum Lesen und Schreiben geöffnet werden, diese müssen immer wieder geschlossen werden.
- Listen von Strings können mit `nltk.Text()` zu einem NLTK-Text umgewandelt werden.
- Kommandozeilenargumente können über die Liste `sys.argv` abgerufen werden. Das erste Element ist immer der Aufrufpfad des Skripts.
---

## Daten von der Festplatte laden und wieder speichern

Wenn wir unsere linguistische Forschung mit technischen Mitteln unterstützen wollen, kommen wir nicht umhin gespeicherte Sprachdaten zu laden und berechnete Auswertungen und/oder Aufbereitungen zu speichern. Unsere Berechnungen und Variablenbelegungen zur Laufzeit des Programmes sind im Hauptspeicher des Computers gespeichert. Dieser ist flüchtig. Persitenz bietet nur die Festplatte.

### Lesen

Also, beginnen wir mit dem einfachen Laden. Hierfür benötigen wir `open`:

~~~python
f1 = open('demofile.txt', 'r')
content1 = f1.read()
# ...

f2 = open('demofile.txt', 'r')
content2 = f2.readlines()
# ...
~~~

> ## Frage(n)
> - Was passiert in jeder Zeile des Programmes?
> - Welchen Typ hat `f` und welchen Typ hat `content1` bzw. `content2`?
> - Was fehlt noch? Warum ist das wichtig?
> - Was ist der Unterschied zwischen `read` und `readlines`?
{: .discussion}

### Schreiben

Wenn wir schreiben wollen, dann geht das so:

~~~python
f = open('outfile.txt', 'w')
content = 'blablabla'
f.write(content)
f.close()
~~~

> ## Frage(n)
> Existiert `outfile.txt` bereits?
> Was kann passieren, wenn wir `f` nicht schließen?
{: .discussion}

Einen Datei manuell in allen möglichen Code-Pfaden zu schließen kann man oft vergessen, in Python gibt es daher einen speziellen `with` Block, der uns das vereinfacht:
~~~python
with open("outfile.txt","a") as f
  f.write("hello world!\n")
  # wird nach diesem Block automatisch geschlossen
~~~

### Tipps und Tricks

Wenn ihr vermeiden wollt, dass ihr eine Datei überschreibt, die es schon gibt, gibt es mehrere Mittel. Zum einen könnt ihr einen anderen Schreibmodus verwenden:

~~~python
f = open('demofile.txt', 'x')
# ...
f.close()
~~~



Der Modus x schreibt in eine neue Datei. Existiert die Datei jedoch schon, wird ein sogenannter `FileExistsError` ausgegeben und das Programm beendet.

Das ist jedoch nicht die eleganteste Lösung. Solche *Exceptions* und *Errors* (mehr dazu in einer späteren Sitzung) sollten vermieden werden, wo es möglich ist.

Alternativ gibt es im Modul os (Submodul path) eine Funktion `exists`:
~~~python
from os.path import exists
print(exists('demofile.txt'))
~~~


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


## Einlesen einer Textdatei in NLTK

Wir wollen nun unseren Beispieltext mit der Geschichte von Hase und Igel als Text in NLTK laden.
Dafür müssten wir als erstes eine Liste von allen Wörtern des Textes in der richtigen Reihenfolge erstellen.
Das heißt, dass wenn wir den Text zeilenweise einlesen, die Zeichenketten auftrennen müssen.
Eine einfache Methode dazu haben wir mit der `split()` Funktion bereits kennen gelernt.
Diese Funktion kann aber z.B. nicht mit Punktuation umgehen.

~~~python
txt = "Ich, der große Zappano, werde ein Kaninchen aus dem Hut zaubern!"
txt.split()
~~~
~~~
['Ich,', 'der', 'große', 'Zappano,', 'werde', 'ein', 'Kaninchen', 'aus', 'dem', 'Hut', 'zaubern!']
~~~
{: .output}

NLTK bietet eine Funktion `word_tokenize(text)`, die diese Aufgabe besser löst.
~~~python
from nltk import word_tokenize
word_tokenize(txt)
~~~
~~~
['Ich', ',', 'der', 'große', 'Zappano', ',', 'werde', 'ein', 'Kaninchen', 'aus', 'dem', 'Hut', 'zaubern', '!']
~~~
{: .output}

Die Funktion `nltk.Text` erstellt aus so einer Liste von Wörtern dann einen neuen Text,
der genau so wie alle anderen Texte genutzt werden kann.
~~~python
ntxt = nltk.Text(word_tokenize(txt))
ntxt.concordance("werde")
FreqDist(ntxt).plot()
~~~
~~~
Displaying 1 of 1 matches:
Ich , der große Zappano , werde ein Kaninchen aus dem Hut zaubern !
~~~
{: .output}

## Kommandozeilenargumente

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
