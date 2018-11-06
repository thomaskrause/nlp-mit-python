---
title: "Levenshtein-Distanz"
teaching: 0
exercises: 0
questions:
objectives:
keypoints:
---

## Nutzung von NLTK zur Berechnung der Levenshtein-Distanz

NLTK ist eine Python-Bibliothek zur Umsetzung vieler NLP-Standard-Aufgaben.
NLTK ist in Untermodulen organisiert.
Für Metriken wie die Levenshtein-Distanz, gibt es das Untermodul `nltk.distance` 
([Dokumentation](http://www.nltk.org/api/nltk.metrics.html#module-nltk.metrics.distance))

NLTK kann mit
~~~python3
import nltk
~~~
importiert werden.

> ## Paketnamen und NLTK
> Paketnamen in NLTK sind nicht unbedingt Modulnamen. So gibt es zwar das Paket `nltk.metrics`, aber nach dem
> Importieren ist der Name des Moduls `nltk.distance`. Das liegt an der etwas verwirrenden internen Modulstruktur von
> NLTK. Zudem gibt es ein anderes Modul mit dem Namen `metrics`, aber aus dem `nltk.translate` Paket und für Konflikte in den Modulnamen sorgt.
> Nutzen Sie einfach `nltk.distance` als Modulenamen, auch wenn die Dokumentation von `nltk.metrics.distance` spricht.
{: .callout}

Die Levenshtein-Distanz ist als Funktion mit der Signatur `edit_distance(s1, s2)` implementiert.
~~~python3
nltk.distance.edit_distance("Geisterbahn", "Achterbahn")
~~~
~~~
4
~~~
{: .output}
