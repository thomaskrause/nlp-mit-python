import nltk
import nltk.tag.hmm as hmm

gold_corpus = nltk.corpus.ConllCorpusReader('.', 'tiger.conll09',
                                     ['ignore', 'words', 'ignore', 'ignore', 'pos'],
                                     encoding='utf-8')
# Lege einen neues HMM Trainings-Objekt mit Standard-Parametern an
trainer = hmm.HiddenMarkovModelTrainer()
model = trainer.train(gold_corpus.tagged_sents())

# Nutze das Modell um ein paar Testsätze zu taggen.
print(model.tag(["Majoran", "ist", "frisch"]))
print(model.tag(["Majoran", "ist", "cool"]))