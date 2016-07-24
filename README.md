# markov-chain-sentences
Simple Python implementation of Markov chains used to create sentences.

Upon instantiation the code creates a list of all valid words to start a sentence with, and a graph of every valid way to continue a sentence using the provided data. The code traverses tha graph randomly from a starting word until a word with no children is discovered. To prevent cycles the verticies can only be traversed once.
