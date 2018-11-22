---
title: "POS-Tagger trainieren"
teaching: 0
exercises: 0
questions:
- Wie kann ein POS-Tagger in NLTK trainiert werden?
objectives:
- Schritte des Lernverfahrens verstehen
keypoints:
---

## RIDGES Korpus

Bitte laden Sie die Datei `ridges8_gold.txt` aus dem Moodle-Kurs herunter.
Dieses ist ein Subset aus dem RIDGES Korpus mit manuell korrigierten POS-Tags im (STTS Tagset)[http://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/TagSets/stts-table.html].

Die Datei besteht aus Sätzen, wobei jeder Satz in einer Zeile geschrieben ist.
Tokens sind durch Leerzeichen abgetrennt und das POS-Tag ist mit `/` an jedes Token angeängt:
~~~
Die/ART Römer/NN nennen/VVFIN es/PPER Persa/FM ./$.
~~~
Dieses Dateiformat kann direkt von NLTK durch den [TaggedCorpusReader](https://www.nltk.org/api/nltk.corpus.reader.html?highlight=tagged#nltk.corpus.reader.tagged.TaggedCorpusReader) eingelesen werden.

[RIDGES](https://www.linguistik.hu-berlin.de/de/institut/professuren/korpuslinguistik/forschung/ridges-projekt/ridges-projekt) ist ein frei verfügbares Korpus bestehend aus deutsprachige Kräuterkundetexte aus historischen Sprachstufen.
Wir wollen auf diesem Goldstandard einen Hidden-Markov-basierten POS-Tagger trainieren.

Dazu müssen wir erst einmal ein paar Module aus NLTK importieren.
~~~python
import nltk
import nltk.corpus.reader.tagged as tagged
import nltk.tag.hmm as hmm
~~~

Dann laden wir die Datei mit dem `TaggedCorpusReader`. Es gibt noch weitere Korpusreader, die andere Formate verstehen.
Das erste Argument ist das Arbeitsverzeichnis, das zweite eine Liste von Dateien.
~~~python
gold_corpus = tagged.TaggedCorpusReader(".", ["ridges8_gold.txt"])
~~~

Mit der Methode `tagged_words()` kann man sich eine Liste aller Token und deren Tags ausgeben (als Tupel) lassen.
~~~python
for w in gold_corpus.tagged_words():
    print(w)
~~~

Die Methode `tagged_sents()` liefert eine Liste von Sätzen zurück.
Dabei ist jeder Satz wieder selbst eine Liste von Wörtern.
~~~python
print(gold_corpus.tagged_sents()[5])
~~~

Nun legen wir ein neues HMM Trainings-Objekt mit Standard-Parametern an und trainieren es auf den getagged Sätzen.
~~~python
trainer = hmm.HiddenMarkovModelTrainer()
model = trainer.train(gold_corpus.tagged_sents())
~~~
Die [`train()`]((https://www.nltk.org/api/nltk.tag.html?highlight=hiddenmarkovmodeltrainer#nltk.tag.hmm.HiddenMarkovModelTrainer.train)) Funktion liefert ein Modell aus Objekt zurück. Dieses können wir jetzt nutzen, um eigene Sätze zu taggen.

~~~python
print(model.tag(nltk.word_tokenize("Majoran ist frisch")))
print(model.tag(nltk.word_tokenize("Majoran ist cool")))
~~~
~~~
[('Majoran', 'NN'), ('ist', 'VAFIN'), ('frisch', 'ADJD')]
[('Majoran', 'NN'), ('ist', 'VAFIN'), ('cool', 'NN')]
~~~
{: .output}

Modelle können mit der [Dill-Bibliothek](https://pypi.org/project/dill/) in Dateien gespeichert und wieder geladen werden.
Diese muss erst mit `pip3` installiert werden.
~~~bash
pip3 install dill
~~~
Dann kann man ein Modell folgendermaßen speichern:
~~~python
import dill
dill.dump( model, open( "ridges.model", "wb" ) )
new_model = dill.load( open( "ridges.model", "rb" ))
new_model.tag(nltk.word_tokenize("Die Römer nennen es Majoran"))
~~~
~~~
[('Die', 'ART'), ('Römer', 'NN'), ('nennen', 'VVFIN'), ('es', 'PPER'), ('Majoran', 'NN')]
~~~
{: .output}