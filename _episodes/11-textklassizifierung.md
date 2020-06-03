---
title: "Textklassifzierung mit Tensorflow"
teaching: 0
exercises: 0
questions:
- Wie kann man mit Hilfe von neuronalen Netzen Texte klassifizieren?
objectives:
- Tensorflow-API mit Python ansprechen
- Daten für Tensorflow aus CSV Dateien einlesen und aufbereiten
keypoints:
---

## Einführung

Textklassifizierung kann für verschiedene Bereiche eingesetzt werden, um Texte Kategorien zuzuweisen.
Beispiele dafür sind
- die Kategorisierung von E-Mails in Spam oder Nicht-Spam,
- eine Zuordnung eines Textes zu einem Autor oder Eigenschaften des Autors,
- Positives oder negatives Sentiment bestimmen (zum Beispiel bei einer Produkt-Bewertung),
- die Sprache eines Textes zu identifizieren.

## Bag of words

Textklassifikation hat den gesamten Text als Eingabe und die Klasse als Ausgabe.
Neuronale Netzwerke haben aber Vektoren von Zahlen als Ein- und Ausgabe.
Um die Ausgabe zu kodieren, kann man Vektoren nutzen, die die gleiche Länge wie die Anzahl der Klassen haben.
Jeder Klasse wird dann ein Index des Ausgabe-Vektors zugeordnet.
Nach Berechnung der Ausgabe des neuronalen Netzwerk ist dann die Klasse, die dem Index mit dem höchsten Wert im Vektor zugeordnet ist die erkannte Klasse.
Wenn man zum Beispiel zwischen den Sprachen „Englisch“, „Deutsch“, „Französisch“ unterscheiden möchte, hat man 3 Klassen und damit Vektor der Länge drei.
Wenn wir also zum Beispiel die Ausgabe `(0.13, 0.99, 0.4)` haben und Englisch dem ersten Index, Deutsch dem zweiten und Französisch dem dritten Index zugeordnet ist, dann wurde vom neuronalen Netz die Klasse „Deutsch“ vorhergesagt.


Für die Eingabe, also den eigentlichen Text, müssen wir aber auch eine geeignete Vektordarstellung finden.
Dazu nutzen wir in diesem Tutorial sogenannte *Bag of words*.

{% include links.md %}