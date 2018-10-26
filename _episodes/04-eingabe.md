---
title: "Eingabe von Daten"
teaching: 0
exercises: 1
questions:
- Wie können veränderbare Daten durch Python verarbeitet werden?' 
objectives:
- Interaktive Eingabe von Nutzern einholen
- Ein- und Auslesen von Dateien
keypoints:
---

## Interaktive Eingabe

Wir kennen bereits `print(var)` um Informationen auszugeben.
Das Gegenstück dazu die Funktion `input()`. 
Sie erlaubt einem Python-Skript, Texteingaben vom Nutzer entgegenzunehmen.

~~~python
print("Hallo, meine Name ist Script!")
name = input("Wie heißen Sie? ")
print("Hallo " +  name + "!")
~~~

Dieses Script erzeugt erst die Ausgabe
~~~
Hallo, meine Name ist Script!
Wie heißen Sie? ▮
~~~
{: .output}

Das Argument von `print()` ist ein sogenannter "Prompt", also eine Eingabeaufforderung an den Nutzer. 
Der Prompt wird ausgegeben und es wir solange gewartet, bis der Nutzer eine Eingabe gemacht und diese mit der Eingabetaste <kbd>Return</kbd> abgeschlossen hat.
Die Funktion liefert die Eingabe als Typ String zurück.
In diesem Beispiel wird die Rückgabe in eine Variable geschrieben und wieder ausgegeben.
~~~
Hallo, meine Name ist Script!
Wie heißen Sie? Thomas 
Hallo Thomas!
~~~
{: .output}

> ## Übung
> Schreiben Sie ein Skript das folgendes tut:
> Das Skript hat eine interne „magic number“, die Sie frei wählen können. 
> Fragen Sie den Nutzer, wie die Nummer ist. Geben Sie ihm Feedback, ob die Zahl die er geraten hat größer oder kleiner als die „magic number“ ist.
> Wenn der Nutzer die Zahl erraten hat, gratulieren Sie ihm und beenden das Programm.
>> ## Lösung
>> Mögliche Lösung:
~~~python
magic_number = 355
guessed = None
while guessed != magic_number:
    guessed = input("Bitte Nummer raten: ")
    guessed = int(guessed)
    if guessed < magic_number:
        print("Zu klein!")
    elif guessed > magic_number:
        print("Zu groß!")
print("Herzlichen Glückwunsch, Sie haben die Nummer erraten!")
~~~
>{: .solution}
{: .challenge}