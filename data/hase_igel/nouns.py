# Unsere Funktion nimmt eine Liste als Parameter
def find_nouns(list_of_words):
    nouns = list()
    # Das erste Wort ist wahrscheinlich großgeschrieben, fällt aber aus unserer Definition raus
    for i in range(1, len(list_of_words)):
    	current_word = list_of_words[i]
    	if current_word[0].isupper():
        	# list_of_words[i-1]: Das vorherige Wort
            if not list_of_words[i-1].endswith("."):
                nouns.append(current_word)
    return nouns


with open("hase_igel.txt") as f:
    story = f.read()
    words = story.split()
    nouns = find_nouns(words)

with open("hase_igel_nouns.txt", "w") as result:
    for noun in nouns:
        result.write(noun + ", ")
