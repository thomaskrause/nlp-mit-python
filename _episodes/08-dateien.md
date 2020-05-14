---
title: "Dateien lesen und schreiben"
teaching: 10
exercises: 30
questions:
- Wie können Dateien durch Python verarbeitet werden?
objectives:
- Ein- und Auslesen von Dateien
keypoints:
- Mit den eingebauten Funktionen `open` können Dateien zum Lesen und Schreiben geöffnet werden, diese müssen immer wieder geschlossen werden.
---

## Daten von der Festplatte laden und wieder speichern

Wenn wir unsere linguistische Forschung mit technischen Mitteln unterstützen wollen, kommen wir nicht umhin gespeicherte Sprachdaten zu laden und berechnete Auswertungen und/oder Aufbereitungen zu speichern. Unsere Berechnungen und Variablenbelegungen zur Laufzeit des Programmes sind im Hauptspeicher des Computers gespeichert. Dieser ist flüchtig. Persitenz bietet nur die Festplatte.

### Lesen

Also, beginnen wir mit dem einfachen Laden. Hierfür benötigen wir `open` (schauen Sie für die Beschreibung der verwendeten Funktionen auch in die Python-Hilfe):

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
>
>> ## Lösung
>>
>> Die Funktion `open` öffnet die Datei im Lesemodus (`"r"` als Wert für den Modus-Parameter) und liest dann den Inhalt mit den Methoden `read()` bzw. `readlines()` in Variablen.
> `read()` liest die gesamte Datei als einen String und liefert einen Wert vom Typ `str` zurück.
> `readlines()` liest die Datei zeilenweise und liefert eine Liste mit Strings zurück.
> Es fehlt noch das Schließen der Dateien mit der Methode `close()`.
> ~~~python
> f1.close()
> ~~~
> Das Schließen von Datein ist notwendig, wenn die gleiche Datei von mehreren Programmen oder Programmteilen genutzt werden soll.
> Insbesondere beim mischen von Lesen und Schreiben in Dateien kann es zu Problemen kommen, wenn gleichzeitig zwei Dateivariablen offen sind.
> {: .solution}
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
>> ## Lösung
>>
>> Die Datei muss nicht bereits existieren, das Programm wird die Datei neu anlegen und überschreiben.
>> Wenn `f` nicht geschlossen wird, wird zwar auch die Datei angelegt, aber es kann passieren, dass der Inhalt nicht oder nicht vollständig geschrieben wird.
> {: .solution}
{: .discussion}

Einen Datei manuell in allen möglichen Code-Pfaden zu schließen kann man oft vergessen, in Python gibt es daher einen speziellen `with` Block, der uns das vereinfacht:
~~~python
with open("outfile.txt","a") as f
  f.write("hello world!\n")
  # wird nach diesem Block automatisch geschlossen
~~~

### Tipps und Tricks

Wenn Sie vermeiden wollen, dass Sie eine Datei überschreiben, die es schon gibt, gibt es mehrere Mittel. Zum einen können Sie einen anderen Schreibmodus verwenden:

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
> Als Geschichte nehmen wir die Zusammenfassung des Inhalts von hier: [http://de.wikipedia.org/wiki/Der_Hase_und_der_Igel](http://de.wikipedia.org/wiki/Der_Hase_und_der_Igel)
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


{% include links.md %}