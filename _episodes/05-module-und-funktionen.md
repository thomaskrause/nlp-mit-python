---
title: "Eigene Funktionen und Module"
teaching: 0
exercises: 0
questions:
- Wie können Funktionen aus externen Bibliotheken eingebunden werden?' 
- Wie kann ich selbst eigene Funktionen definieren?
objectives:
- Funktionalität von Programmen nachnutzen
keypoints:
---

## Eigene Funktionen definieren

Bisher haben wir uns nur mit einfachen Anweisungen
beschäftigt. Typischerweise wollen wir aber nicht immer wieder
neu eingreifen, sondern unser Programm soll eine komplexe
Anweisung auf einmal ausführen. Dafür müssen wir unseren
Code als Funktion definieren:
~~~python
def add_mult(a, b):
    output = a + b
    output = output + (a * b)
    return output
~~~

Eine Funktion besteht aus der Funktionsdefinition, die mit den Schlüssewort `def` eingeleitet und mit dem Doppelpunkt abgeschlossen wird.
Darin steht der Name der Funktion (hier `add_mult`) und die Namen der Argumente, abgetrennt durch Komma.
In dem Beispiel werden zwei Argumente `a` und `b` übergeben.

Der Funktionsdefinition folgt ein Code-Block, der die Funktion implementiert.
Der Block ist hier mit der `return` Anweisung abgeschlossen, die die Funktion beendet und den Rückgabewert definiert.

Nachdem eine Funktion definiert ist, kann sie im Code aufgerufen werden, genauso wie die eingebauten Funktionen auch.

~~~python
v = add_mult(1, 100)
print(v)
~~~

> ## Übung
> Schreiben Sie eine Funktion, die gegeben dreier Werte die Summe aller Zahlen zwischen dem ersten und dem zweiten Wert multipliziert mit dem dritten Wert angibt.
> Rufen Sie diese Funktion für verschiedene Werte auf und geben Sie die Werte aus.
>> ## Lösung
>> ~~~python
>> def complex_math(start, end, multiplier):
>>     sum = 0
>>     for i in range(start, end):
>>         sum = sum + (i*multiplier)
>>     return sum
>> 
>> print(complex_math(1,100, 1))
>> print(complex_math(20,100, 3))
>> print(complex_math(1,10, 3.14))
>> ~~~
>> ~~~
>> 4950
>> 14280
>> 141.3
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

Funktionen können Werte von verschiedenen Typen als Argument bekommen.
Auch kann die gleiche Funktion verschiedene Typen von Werten zurückgeben und je nach Bedingungen verschiedene
`return` Anweisungen ausführen (es wird aber immer nur die erste `return` Anweisung ausgeführt).

~~~python
def fancy_add(val):
    if isinstance(val, str):
        return  val + " + 1"
    elif isinstance(val, int):
        return val + 1
    elif isinstance(val, float):
        return val + 1.0
    else:
        return 42

print(fancy_add(2))
print(fancy_add(2.0))
print(fancy_add("2"))
print(fancy_add(False))
~~~
~~~
3
3.0
2 + 1
1
~~~
{: .output}

Der Code nutzt die eingebaute Funktion `isinstance` um zu überprüfen, ob eine Variable einen gegebenen Typ hat.

Außerdem ist es möglich, dass eine Funktion mehr als einen Wert zurückgibt. 
In diesem Fall muss die `return` Anweisung alle Werte mit Komma getrennt auflisten.

~~~python
def get_str_info(text):
    l = len(text)
    n = len(set(text))
    return l, n

a, b = get_str_info("This is an arbitrary string, I swear")
~~~
~~~
36
16
~~~
{: .output}

> ## Frage
> Was bedeuten die Werte, die die Funktion zurückliefert?
{: .callout}

In Python wird unterschieden zwischen positionalen Argumenten, die übergeben werden müssen und Keyword-Argumenten, die optional sind und für die ein Standard-Wert in der Funktions-Definitions angegeben werden kann, der genutzt wird wenn das Argument nicht übergeben wird. 
Hier ein Beispiel:
~~~python
def print_log(log_text, with_exclamation_marks=False):
    out = log_text if not with_exclamation_marks else ('!!! '+log_text+' !!!')
    print(out)
    
print_log('Nothing happend.')
print_log('Alarm', with_exclamation_marks=True)
print_log('Alarm', True)
~~~
~~~
Nothing happend.
!!! Alarm !!!
!!! Alarm !!!
~~~
{: .output}
Der Standardwert für das Argument `with_exclamation_marks` ist hier `False`.

## Module und der `import` Befehl