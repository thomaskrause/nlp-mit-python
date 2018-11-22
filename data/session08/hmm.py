import nltk
import nltk.corpus.reader.tagged as tagged
import nltk.tag.hmm as hmm

# Jede Zeile ist ein Satz, jedes Wort ist durch Leerzeichen abgetrennt und jedes Wort hat ein Tag, das durch "/" angehängt ist,
# also z.B. 
# Die/ART Römer/NN nennen/VVFIN es/PPER Persa/FM ./$.
# (https://www.nltk.org/api/nltk.corpus.reader.html?highlight=tagged#nltk.corpus.reader.tagged.TaggedCorpusReader)
gold_corpus = tagged.TaggedCorpusReader(".", ["ridges8_gold.txt"])
# Lege einen neues HMM Trainings-Objekt mit Standard-Parametern an
trainer = hmm.HiddenMarkovModelTrainer()
# trainiere auf den Goldstandard-Korpus
# (https://www.nltk.org/api/nltk.tag.html?highlight=hiddenmarkovmodeltrainer#nltk.tag.hmm.HiddenMarkovModelTrainer.train)
model = trainer.train(gold_corpus.tagged_sents())

# Nutze das Modell um ein paar Testsätze zu taggen.
print(model.tag(["Majoran", "ist", "frisch"]))
print(model.tag(["Majoran", "ist", "cool"]))