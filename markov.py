import random , copy

'''
Creates a graph of possible word sequences based on the provided list of sentences
and uses those to create new strings by randomizing a path through said graph.
'''
class MarkovChainSentence():
    
    def __init__(self, sentences):
        self.words = self.extract_words(sentences)
        self.start_words = [(sentence.split(' ')[0].lower()) for sentence in sentences]

    '''
    Returns a dict on the form {word: [next_word1, next_word1, next_word2]}.
    To avoid computing floating frequencies it simply creates duplicate edges where needed.
    '''
    def extract_words(self, sentences):
        words = {}
        for sentence in sentences:
            following_words = []
            for word in sentence.split(' '):
                if word not in words:
                    words[word] = []
                following_words.append(word)
                following_words = words[word]

        return words

    '''
    Traverses the graph and saves the path taken to create a sentence
    '''
    def create_sentence(self):
        remaining_words = copy.deepcopy(self.words)
        word = random.choice(self.start_words)
        quote = word
        while(remaining_words[word]):
            old_word = word
            word = random.choice(remaining_words[word])
            #Since duplicate edges are allowed a filter is required to remove all parallell edges
            remaining_words[old_word] = [x for x in remaining_words[old_word] if x != word]
            quote += ' ' + word

        return quote
