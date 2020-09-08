#!/usr/bin/python3

import numpy as np
import random

# os.chdir("perfectspoonerisms")  #change this to your current working directory for the project.

class spoonerize():
    '''
    Syntax notes:
        -in function body, caps variable names are variables that should be capitalized while they're in the function.
        -in function argument names, caps variable names denote variables that are supposed to be capitalized.
        -in function argument names, non-capped variables get converted to caps in function body
        -all functions should take words as input, convert for their uses, then convert back to caps words ***THIS IS NOT COMPLETED***
    '''
    def __init__(self):
        '''
        -Initializes spoonerizer variables. Creates vowel_list, a list of vowel symbols, consonant_list for consonants.
        -Creates word_to_sym and sym_to_word, local dictionaries that help convert capital letter words to symbol tuples,
        and vice versa
        -Creates full_list, an array which contains capitalized WORD, its symbol list, and the symbol-number list
        -Creates num_array which is the last two rows of full_list
        -Shuffles num_array so it can be treated as random order of words.
        '''

        self.vowel_list = ("AA", "AA0", "AA1", "AA2", "AE", "AE0", "AE1", "AE2", "AH", "AH0", "AH1",
                      "AH2", "AO", "AO0", "AO1", "AO2", "AW", "AW0", "AW1", "AW2", "AY", "AY0",
                      "AY1", "AY2", "EH", "EH0", "EH1", "EH2", "ER", "ER0", "ER1", "ER2", "EY",
                      "EY0", "EY1", "EY2", "IH", "IH0", "IH1", "IH2", "IY", "IY0", "IY1", "IY2",
                      "OW", "OW0", "OW1", "OW2", "OY", "OY0", "OY1", "OY2", "UH", "UH0", "UH1",
                      "UH2", "UW", "UW0", "UW1", "UW2")
        self.consonant_list = ("B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L", "M", "N", "NG", "P", "R",
                          "S", "SH", "T", "TH", "V", "W", "Y", "Z", "ZH")

        self.word_to_sym, self.sym_to_word = self.import_cmudict()
        self.sym_to_num_dict, self.num_to_sym_dict = self.import_cmusymbols()

        full_list = np.array([[x, y, self.sym_to_num(y)] for x, y in self.word_to_sym.items()])
        print(full_list)
        self.num_array = full_list[:, 2]
        random.shuffle(self.num_array)

    def import_cmudict(self):
        '''
        -Imports cmudict from WD, processes line by line: Removes lines starting with ;;;, splits entries
        -Creates word_to_sym, a dictionary of WORD and symbol list
        -Creates sym_to_word, a dictionary of symbol list and WORD
        **Peter learned here that dictionaries are unlike lists. When you assign dict elements, they append after last.
        :return: word_to_sym, sym_to_word
        '''
        word_to_sym, sym_to_word = {}, {}   ##p  {} makes dictionaries.
        with open('cmudict-0.7c.txt', 'r') as file:
            for line in file:
                l = line.strip().split()
                if l[0] != ';;;':
                    word_to_sym[l[0]] = (l[1:])
                    sym_to_word[tuple(l[1:])] = l[0]

        return word_to_sym, sym_to_word

    def import_cmusymbols(self):
        '''
        -Creates s_list
        -Opens CMU symbols, just a list of all 84 symbols.
        -Appends each line from symbol dict to s_list
        -Creates n_list which is a list of the numbers in range(len(s_list))
        -Creates sym_to_num_dict, a dictionary of symbol to number
        -Creates num_to_sym_dict, a dictionary of number to symbol
        :return: sym_to_num_dict, num_to_sym_dict
        '''
        s_list = []  ##p makes new list s_list
        with open('cmudict-0.7b.symbols.txt', 'r') as file:  ##p opens cmudict-0.7b.symbols.txt, reads, names it "file"
            for line in file:  ##p starts loop for each line in file
                l = line.strip()  ##p makes l variable of removed spaces from line in file
                s_list.append(l)  ##p adds it to end of s_list. s_list is a list of all the symbols

        n_list = list(range(len(s_list)))  ##p makes a list of the range of the length of s_list. In other words, tells you all the positions of all the lines in s_list
        sym_to_num_dict = {s_list[x]: n_list[x] for x in range(len(s_list))}  ##p makes a dictionary of the symbol and the number on n_list
        self.num_to_sym_dict = {n_list[x]: s_list[x] for x in range(len(s_list))}  ##p makes a dictionary of the number on n_list and the symbol (reversed of prior)
        return sym_to_num_dict, self.num_to_sym_dict  ##p returns symbol dictionary

    def main(self, word1=None, word2=None):
        '''
        -A nested function that processes input based on whether there are zero, one, or two words.
        -If both arguments are None, returns no_word()
        -If word2 is none returns one_word(word1.upper())
        -Otherwise returns two_word(word1.upper(), word2.upper())
        :param word1: default None, assigned if entered
        :param word2: default None, assigned if entered
        :return: Eventually returns two_word(word1, word2)
        '''
        if (word1 == None) and (word2 == None):
            print("you entered zero words")
            return self.no_word()
        elif word2 == None:
            print("you entered one word")
            return self.one_word(word1.upper())
        else:
            print("you entered two words")
            return self.two_word(word1.upper(), word2.upper())

    def no_word(self):
        '''
        -Takes no input, assigns CARING to be first word of num_array and converts it to WORD.
        :return: CARING, which is a random word. passes to one_word(CARING)
        '''
        CARING = self.sym_to_word.get(tuple(self.num_to_sym(self.num_array[0])))
        return self.one_word(CARING)

    def one_word(self, word1=None):
        '''
        -sets PARING to a rhymed word of word1, passes word1 and PARING to two_word
        -checks that word1 exists. helps make error message more helpful
        :param word1: Requires word1, not necessarily capitalized.
        :return: passes two_word(WORD1, PARING)
        '''
        if word1 == None:
            print("Gotta enter a word for the one_word function, bud")
            return
        PARING = self.rhymer_nonrandom(word1.upper())
        print("I'm gonna rhyme ", word1.upper(), " with ", PARING)
        return self.two_word(word1.upper(), PARING)

    def two_word(self, word1=None, word2=None):
        '''
        -Checks for words, error if a word is empty.
        -Checks words are different, error if same.
        -Checks endings are equal for word1, word2. If same, applies matcher to word1, word2.
            Matcher makes carrot,parrot from caring,paring
        -Checks beginnings same, will eventually form paring and parrot from caring and carrot.
        :param word1: first word, aka caring
        :param word2: second word, aka either carrots, parrots, paring, or NA
        :return: either errors or the printed output of 4 spoonerisms. return ends command
        '''
        if (word1==None) or (word2 == None):
            print("Gotta enter a word, bud")
            return
        if word1.upper() == word2.upper():
            print("You have to enter either different words, or fewer words.")
            return
        if self.ending(self.word_to_sym.get(word1.upper())) == self.ending(self.word_to_sym.get(word2.upper())):
            carrot, parrot = self.matcher_endings(word1, word2)
            caring, paring = word1.upper(), word2.upper()
            print("Your spoonerisms are:")
            print(caring, parrot, paring, carrot)
            print(parrot, caring, carrot, paring)
            print(paring, carrot, caring, parrot)
            print(carrot, paring, parrot, caring)
            print("Thank you for using Peter's spoonerism generator")
            return
        if self.beginning_checker(word1, word2) == True:
            paring, parrot = self.matcher_beginnings(word1, word2)
            caring, carrot = word1.upper(), word2.upper()
            print("Your spoonerisms are:")
            print(caring, parrot, paring, carrot)
            print(parrot, caring, carrot, paring)
            print(paring, carrot, caring, parrot)
            print(carrot, paring, parrot, caring)
            return# Add to this section what to do when you add alliterative words.


    def ending(self, symbol_list):
        '''
        -Takes symbol list
        -if the first symbol is a consonant, return the rest of the word starting from the first vowel, otherwise return the whole word.
        :param symbol_list: Requires list of symbols, not word
        :return: ending of word, by syllable.
        '''
        if symbol_list[0] in self.consonant_list:
            for letter in symbol_list[1:]:
                if letter in self.vowel_list:
                    place = symbol_list.index(letter)
                    return symbol_list[place:]
                elif letter is symbol_list[-1]:
                    return symbol_list
        else:
            return symbol_list

    def beginning(self, symbol_list):
        '''
        -Returns first consonants of word until the first vowel, if any.
        :param symbol_list: Requires symbol list
        :return: first consonant symbols
        '''
        if symbol_list[0] in self.consonant_list:
            for letter in symbol_list:
                if letter in self.vowel_list:
                    place = symbol_list.index(letter)
                    return symbol_list[:place]
        else:
            return None

    def sym_to_num(self, list):  ##p makes a function that takes words and returns symbol words
        return [self.sym_to_num_dict.get(symbol) for symbol in list]

    def num_to_sym(self, list):  ##p makes a function that takes an array of numbers and gets symbol array
        return [self.num_to_sym_dict.get(num) for num in list]

    def beginning_checker(self, word1, word2):
        '''
        Takes 2 words and returns true if they have the same beginning consonants.
        :param word1:
        :param word2:
        :return:
        '''
        if self.beginning(self.word_to_sym.get(word1.upper())) == self.beginning(self.word_to_sym.get(word2.upper())):
            return True
        else:
            return False

    def matcher_beginnings(self, caring, carrots):
        caring, carrots = caring.upper(), carrots.upper()
        paring = self.rhymer_nonrandom()

    def matcher_endings(self, caring, paring):
        '''
        Takes caring and paring, returns two ending-sharing words that start with caring[0] and paring[0].
        :param caring:
        :param paring:
        :return:
        '''
        caring, paring = caring.upper(), paring.upper()
        carrots, parrots = self.caring_gets_carrotparrot(caring)
        carrots, parrots = self.word_to_sym.get(carrots), self.word_to_sym.get(parrots)
        if self.beginning_checker(paring, self.sym_to_word.get(tuple(parrots))) == True:
            print("i found a spoonerism")
            print(self.sym_to_word.get(tuple(carrots)), self.sym_to_word.get(tuple(parrots)))
            carrots = self.sym_to_word.get(tuple(carrots))
            parrots = self.sym_to_word.get(tuple(parrots))
            return carrots, parrots
        else:
            print(self.sym_to_word.get(tuple(carrots)), self.sym_to_word.get(tuple(parrots)), "doesn't work")
            return self.matcher_endings(caring, paring)

    def rhymer_nonrandom(self, word):
        word = self.word_to_sym.get(word.upper())
        for x in self.num_array:
            if self.ending(word) == self.ending(self.num_to_sym(x)):
                if word != self.num_to_sym(x):
                    return self.sym_to_word.get(tuple(self.num_to_sym(x)))

    def caring_gets_carrotparrot(self, caring):
        caring = caring.upper()  ##p uppercases word
        np.random.shuffle(self.num_array)  ##p shuffles num_array
        for carrot in self.num_array:  ##p sets up for loop for each value of the dictionary of numbers
            if self.beginning_checker(caring, self.sym_to_word.get(tuple(self.num_to_sym(carrot)))):
                carrot = self.sym_to_word.get(
                    tuple(self.num_to_sym(carrot)))  ##p gets the word of the symbol of the number of x
                parrot = self.rhymer_nonrandom(carrot)  ##P rhymes x, sets it to x1
                if parrot != None:  ##p if x1 isn't empty:
                    return carrot, parrot


# spoonerize().ending("peter")
# spoonerize().main("nipple")
spoonerize().main("oats")