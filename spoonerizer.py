import pandas as pd                                                                     ##p imports the library pandas and shortens how we will call it to "pd"
import numpy as np                                                                      ##p imports the library numpy and shortens how we will call it to "np"
import sys
import random
import os
os.chdir("perfectspoonerisms")  #change this to your current working directory for the project.
class importer():
    def main(self):
        a, b = self.import_cmudict()
        c, d = self.import_cmusymbols()
        return a, b, c, d

    def import_cmudict(self):                                                           ##p makes new function import_cmudict() which opens dictionary, returns symbols and word.
        word_to_sym, sym_to_word = {}, {}                                               ##p makes new variables word_to_sym, sym_to_word
        with open('cmudict-0.7c.txt', 'r') as file:                 ##p opens up cmudict-0.7c.txt, calls it "file"
            for line in file:                                                           ##p starts for loop for each line in file
                l = line.strip().split()                                                ##p for line, strip to elements w/o leading spaces or commas
                if l[0] != ';;;':                                                       ##p removes comments from CMU file, as ";" is interpreted in python
                    word_to_sym[l[0]] = (l[1:])                                         ##p Initializes word_to_sym as dictionary, associates first element of l with the rest starting from second element.
                    sym_to_word[tuple(l[1:])] = l[0]                                    ##p Initializes sym_to_word as dictionary, associates all but first elements as immutable tuple

        return word_to_sym, sym_to_word                                                 ##p returns lines retreieved that do not start with ;;;, made in prior lines.

    def import_cmusymbols(self):                                                        ##p makes new function import_cmusymbols()
        s_list = []  ##p makes new list s_list
        with open('cmudict-0.7b.symbols.txt', 'r') as file:         ##p opens cmudict-0.7b.symbols.txt, reads, names it "file"
            for line in file:                                                           ##p starts loop for each line in file
                l = line.strip()                                                        ##p makes l variable of removed spaces from line in file
                s_list.append(l)                                                        ##p adds it to end of s_list. s_list is a list of all the symbols

        n_list = list(range(len(s_list)))                                               ##p makes a list of the range of the length of s_list. In other words, tells you all the positions of all the lines in s_list
        sym_to_num_dict = {s_list[x]: n_list[x] for x in range(len(s_list))}                 ##p makes a dictionary of the symbol and the number on n_list
        num_to_sym_dict = {n_list[x]: s_list[x] for x in range(len(s_list))}                 ##p makes a dictionary of the number on n_list and the symbol (reversed of prior)
        return sym_to_num_dict, num_to_sym_dict                                                   ##p returns symbol dictionary
word_to_sym, sym_to_word, sym_to_num_dict, num_to_sym_dict = importer().main()
vowel_list = ("AA", "AA0", "AA1", "AA2", "AE", "AE0", "AE1", "AE2", "AH", "AH0", "AH1",
                  "AH2", "AO", "AO0", "AO1", "AO2", "AW", "AW0", "AW1", "AW2", "AY", "AY0",
                  "AY1", "AY2", "EH", "EH0", "EH1", "EH2", "ER", "ER0", "ER1", "ER2", "EY",
                  "EY0", "EY1", "EY2", "IH", "IH0", "IH1", "IH2", "IY", "IY0", "IY1", "IY2",
                  "OW", "OW0", "OW1", "OW2", "OY", "OY0", "OY1", "OY2", "UH", "UH0", "UH1",
                  "UH2", "UW", "UW0", "UW1", "UW2")
consonant_list = ("B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L", "M", "N", "NG", "P", "R",
              "S", "SH", "T", "TH", "V", "W", "Y", "Z", "ZH")

class spoonerize():
    def __init__(self):
        full_list = np.array([[x, y, self.sym_to_num(y)] for x, y in word_to_sym.items()]) ##p makes an array with 4 sets of elements. word, symbol word, symbols as list, symbol numbers as list
        self.num_array = full_list[:, 2]                                                 ##p makes num_array of the last elements in the array
        random.shuffle(self.num_array)
    #def random_word(self, words=1):                                                     ##p defines function that makes as manyv random words as inputed, if no input defaults to 1
    #    for x in range(words):                                                          ##p starts loop for the number of words selected
    #        np.random.shuffle(self.num_array)                                           ##p shuffles number array
    #        rword = self.num_array[0]                                                   ##p sets rword as the first element of num_array
    #        rword = self.num_to_sym(rword)                                              ##p reverts to symbols
    #        rword = sym_to_word.get(tuple(rword))                                       ##p gets words from word_to_sym, sets to rword
    #        print('This is the random word: ', rword)                                   ##p outputs "this is the random word: ___"
    #        self.main(rword)                                                            ##p also calls main function, which rhymes it and makes extra words that don't necessarily spoonerize yet

    def main(self, word1=None, word2=None):
        # randomize list
        if(word1 == None) and (word2 == None):
            print("you entered zero words")
            return self.no_word()
        elif word2 == None:
            print("you entered one word")
            return self.one_word(word1)
        else:
            print("you entered two words")
            return self.two_word(word1, word2)

    def no_word(self):
        caring = sym_to_word.get(tuple(self.num_to_sym(self.num_array[0])))
        return self.one_word(caring)
    def one_word(self, word1):
        paring = self.rhymer_nonrandom(word1)
        return self.two_word(word1, paring)
    def two_word(self, word1, word2):
        if self.ending(word_to_sym.get(word1.upper())) == self.ending(word_to_sym.get(word2.upper())):
            carrot, parrot = self.matcher(word1, word2)
            caring, paring = word1.upper(), word2.upper()
            print("Your spoonerisms are:")
            print(caring, parrot, paring, carrot)
            print(parrot, caring, carrot, paring)
            print(paring, carrot, caring, parrot)
            print(carrot, paring, parrot, caring)
            print("Thank you for using Peter's spoonerism generator")
            return

    def ending(self, symbol_list):
        if symbol_list[0] in consonant_list:
            for letter in symbol_list[1:]:
                if letter in vowel_list:
                    place = symbol_list.index(letter)
                    return symbol_list[place:]
                elif letter is symbol_list[-1]:
                    return symbol_list
        else:
            return symbol_list

    def beginning(self, symbol_list):
        if symbol_list[0] in consonant_list:
            for letter in symbol_list:
                if letter in vowel_list:
                    place = symbol_list.index(letter)
                    return symbol_list[:place]
        else:
            return None

    def sym_to_num(self, word):                                                           ##p makes a function that takes words and makes symbol words
        return [sym_to_num_dict.get(letter) for letter in word]                           ##p returns a get of sym_to_num_dict for the letter for each letter in the word provided

    def num_to_sym(self, array):                                                          ##p makes a function that takes an array of numbers and gets symbol array
        return [num_to_sym_dict.get(num) for num in array]                                   ##p gets symbols for each number array

    def beginning_checker(self,word1,word2):                                                 ##p makes function that takes two words and checks if the first letters are the same. Returns true/false
        if self.beginning(word_to_sym.get(word1)) == self.beginning(word_to_sym.get(word2)):                                                        ##p checks if first letter is the same for both words.
            return True
        else:
            return False

    def matcher(self, caring, paring):
        caring, paring = caring.upper(), paring.upper()
        carrots, parrots = self.caring_gets_carrotparrot_beginning(caring)
        carrots, parrots = word_to_sym.get(carrots), word_to_sym.get(parrots)
        #if word_to_sym.get(paring)[0] == parrots[0]:
        if self.beginning_checker(paring, sym_to_word.get(tuple(parrots))) == True:
            print("i found a spoonerism")
            print(sym_to_word.get(tuple(carrots)), sym_to_word.get(tuple(parrots)))
            carrots = sym_to_word.get(tuple(carrots))
            parrots = sym_to_word.get(tuple(parrots))
            return carrots, parrots
        else:
            print(sym_to_word.get(tuple(carrots)), sym_to_word.get(tuple(parrots)), "doesn't work")
            return self.matcher(caring, paring)

    def rhymer_nonrandom(self, word):
        print(word)
        word = word_to_sym.get(word.upper())
        for x in self.num_array:
            if self.ending(word) == self.ending(self.num_to_sym(x)):
               if word != self.num_to_sym(x):
                   return sym_to_word.get(tuple(self.num_to_sym(x)))

    def rhymer(self, word):                                                              ##p defines new function rhymer
        word = word.upper()                                                              ##p capitalizes word
        word = word_to_sym.get(word)                                                     ##p gets word from word_to_sym, returns symbols. word is now the symbols
        word = self.sym_to_num(word)                                                     ##p converts symbols to numbers
        random.shuffle(self.num_array)                                                   ##p shuffles the array containing word symbol number sets. np.random.shuffle alters num_array without =
        for x in range(len(word), 0, -1):                                                ##p starts loop for each in range of the size of the word reducing til 0, starting at length of word
            for y in self.num_array:                                                     ##p starts loop for each in num_array, which has been randomly shuffled.
                # if len(y[1:]) == x:                                                    ##p if the word is the same as the one selected starting from the second symbol
                if y[1:] == word[1:]:                                                    ##p if first word from num_array is the same as x starting from the second position
                    if y != word:                                                        ##p if it's not equal to the word we started with
                        new_word = y                                                     ##p sets new word equal to the one that satisfies the conditions.
                        return sym_to_word.get(tuple(self.num_to_sym(new_word)))         ##p returns the new word reverted to symbols reverted to letters.

    def caring_gets_carrotparrot(self, caring):                                                              ##p caring_gets_carrotparrot finds carrot and parrot from caring, but parrot not matched with paring by char[0]
        caring = caring.upper()                                                              ##p uppercases word
        caring = word_to_sym.get(caring)                                                     ##p gets symbols of word
        caring = self.sym_to_num(caring)                                                     ##p converts to numbers

        fl = caring[0]                                                                     ##p set fl to first symbol of word

        np.random.shuffle(self.num_array)                                                ##p shuffles num_array

        for carrot in self.num_array:                                                         ##p sets up for loop for each value of the dictionary of numbers
            if carrot[0] == fl:                                                               ##p if fl is the first symbol of x
                carrot = sym_to_word.get(tuple(self.num_to_sym(carrot)))                           ##p gets the word of the symbol of the number of x
                parrot = self.rhymer(carrot)                                                       ##P rhymes x, sets it to x1
                if parrot != None:                                                           ##p if x1 isn't empty:
                    return carrot, parrot
    def caring_gets_carrotparrot_beginning(self, caring):
        caring = caring.upper()  ##p uppercases word
        np.random.shuffle(self.num_array)                                                ##p shuffles num_array
        for carrot in self.num_array:  ##p sets up for loop for each value of the dictionary of numbers
            if self.beginning_checker(caring, sym_to_word.get(tuple(self.num_to_sym(carrot)))):
                carrot = sym_to_word.get(tuple(self.num_to_sym(carrot)))  ##p gets the word of the symbol of the number of x
                parrot = self.rhymer_nonrandom(carrot)  ##P rhymes x, sets it to x1
                if parrot != None:  ##p if x1 isn't empty:
                    return carrot, parrot
#spoonerize().ending("peter")
x, y = spoonerize().main("nipple")