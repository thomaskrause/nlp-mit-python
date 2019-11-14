---
title: "NLTK und eigene Texte"
teaching: 60
exercises: 30
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
FreqDist(txt_de).plot()
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
[('Die', 'NOUN'), ('positivste', 'NOUN'), ('Reaktion', 'NOUN'), (',', '.'), ('die', 'NOUN'), ('man', 'NOUN'), ('in', 'ADP'), ('Berlin', 'NOUN'), ('bekommen', 'NOUN'), ('kann', 'VERB'), (',', '.'), ('ist', 'ADJ'), ('eine', 'NOUN'), ('fehlende', 'NOUN'), ('Beschwerde', 'NOUN'), ('.', '.')]
~~~
{: .output}
Wir Sie sehen, ist der Tagger für Deutsch ausbaufähig.

## Kommandozeilenargumente

> ## System-Konsole aufrufen
> Um die System-Kommandozeile auzurufen, muss man unter **Windows** im Startmenü „Anaconda Prompt“ suchen und auswählen.
> Unter **Mac OS** können Sie eine System-Kommandozeile starten, in dem Sie mit [Spotlight](https://support.apple.com/de-de/HT204014) nach Terminal suchen
> und dieses starten.
> Danach müssen Sie unter Mac OS (aber nicht unter Windows) die Anaconda-Umgebung aktivieren, in dem Sie einmal
> ```bash
> conda activate
> ```
> im Terminal eingeben (der letzte Schritt ist unter Umständen auch unter Linux notwendig).
> Wenn Sie das System-Terminal ausführen, müssen Sie meistens erst 
> Danach müssen Sie unter Mac OS (aber nicht unter Windows) die Anaconda-Umgebung aktivieren, in dem Sie einmal
> ```bash
> conda activate
> ```
> im Terminal eingeben (der letzte Schritt ist unter Umständen auch unter Linux notwendig).
> Falls Sie mehr über die Bedienung von System-Kommandozeilen erfahren wollen, können Sie sich z.B. das Tutorial unter 
> <https://tutorial.djangogirls.org/deintro_to_command_line/> anschauen.
{: .callout}


Wenn man ein Skript  in der System-Konsole aufruft, kann man dem Aufruf zusätzliche per Leerzeichen getrennt Argumente übergeben.
~~~bash
python3 meinskript.py Argument1 NochEinArgument
~~~

Ähnlich wie bei einer Python-Funktion ist das sehr nützlich, um die gleiche Aufgabe bzw. den gleichen Algorithmus/Code auf unterschiedlichen Eingaben auszuführen. 
Wenn ein Skript eine Datei einliest, wäre das z.B. eine gute Möglichkeit den Dateipfad anzugeben, 
damit man das Skript auf verschieden Dateien ausführen kann ohne das Skript selbst fehleranfällig anpassen zu müssen.

Man kann die Argumente, die an ein Skript übergeben werden, alternativ auch in Spyder angeben.
Dazu muss im Menü "Run -> Configuration per File" oder der Shortcut <kbd>Strg</kbd>+<kbd>F6</kbd> ausgeführt werden.
Dann kann man das Häkchen bei "Command line options" auswählen und die Argumente eingeben.
![Einstellung Argumente für Skript in Spyder](../fig/spyder-script-args.png).

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



> ## Übung
> Stellen Sie ihren angefangenen Chatbot fertig, dass er die Mindestanforderung erfüllt.
> Dann bauen Sie ihn folgendermaßen aus (Schritt für Schritt)
> - Tokenisieren Sie die Eingabe um die Stichwörter besser erkennen zu können
> - Finden Sie mit Hilfe des POS-Taggers ein Nomen und referenzieren Sie das Nomen in der Nachfrage (ein englischer Dialog wäre jetzt besser)
> - Fragen Sie am Anfang nach dem Namen des Gegenübers, schreiben Sie diesen in eine Datei und begrüßen Sie den Nutzer mit den richtigen Namen sobald er das Programm noch einmal ausführt.
{: .challenge}

{% include links.md %}