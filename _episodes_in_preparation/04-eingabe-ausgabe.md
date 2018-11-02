---
title: "Eingabe und Ausgabe von Daten"
teaching: 0
exercises: 1
questions:
- Wie können veränderbare Daten durch Python verarbeitet werden?' 
objectives:
- Interaktive Eingabe von Nutzern einholen
- Ein- und Auslesen von Dateien
keypoints:
- Die eingebaute Funktion `input` erlaubt eine interaktive Eingabe vom Nutzer anzufordern.
- Mit den eingebauten Funktionen `open` können Dateien zum Lesen und Schreiben geöffnet werden, diese müssen immer wieder geschlossen werden.
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
Dafür müssen wir diese Funktion allerdings *importieren*, auch das werden wir noch genauer kennen lernen.
