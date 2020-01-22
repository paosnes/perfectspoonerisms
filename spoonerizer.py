import pandas as pd                                                                     ##p imports the library pandas and shortens how we will call it to "pd"
import numpy as np                                                                      ##p imports the library numpy and shortens how we will call it to "np"
import sys


class importer():
    def main(self):
        a, b = self.import_cmudict()
        c, d = self.import_cmusymbols()
        return a, b, c, d

    def import_cmudict(self):                                                           ##p makes new function import_cmudict() which opens dictionary, returns symbols and word.
        word_to_sym, sym_to_word = {}, {}                                               ##p makes new variables word_to_sym, sym_to_word
        with open('perfectspoonerisms//cmudict-0.7c.txt', 'r') as file:                 ##p opens up cmudict-0.7c.txt, calls it "file"
            for line in file:                                                           ##p starts for loop for each line in file
                l = line.strip().split()                                                ##p for line, strip to elements w/o leading spaces or commas
                if l[0] != ';;;':                                                       ##p removes comments from CMU file, as ";" is interpreted in python
                    word_to_sym[l[0]] = (l[1:])                                         ##p Initializes word_to_sym as dictionary, associates first element of l with the rest starting from second element.
                    sym_to_word[tuple(l[1:])] = l[0]                                    ##p Initializes sym_to_word as dictionary, associates all but first elements as immutable tuple

        return word_to_sym, sym_to_word                                                 ##p returns lines retreieved that do not start with ;;;, made in prior lines.

    def import_cmusymbols(self):                                                        ##p makes new function import_cmusymbols()
        s_list = []  ##p makes new list s_list
        with open('perfectspoonerisms//cmudict-0.7b.symbols.txt', 'r') as file:         ##p opens cmudict-0.7b.symbols.txt, reads, names it "file"
            for line in file:                                                           ##p starts loop for each line in file
                l = line.strip()                                                        ##p makes l variable of removed spaces from line in file
                s_list.append(l)                                                        ##p adds it to end of s_list. s_list is a list of all the symbols

        n_list = list(range(len(s_list)))                                               ##p makes a list of the range of the length of s_list. In other words, tells you all the positions of all the lines in s_list
        sym_to_num_dict = {s_list[x]: n_list[x] for x in range(len(s_list))}                 ##p makes a dictionary of the symbol and the number on n_list
        num_to_sym_dict = {n_list[x]: s_list[x] for x in range(len(s_list))}                 ##p makes a dictionary of the number on n_list and the symbol (reversed of prior)
        return sym_to_num_dict, num_to_sym_dict                                                   ##p returns symbol dictionary
word_to_sym, sym_to_word, sym_to_num_dict, num_to_sym_dict = importer().main()


class spoonerize():
    def __init__(self):
        full_list = np.array([[x, y, self.sym_to_num(y)] for x, y in word_to_sym.items()]) ##p makes an array with 4 sets of elements. word, symbol word, symbols as list, symbol numbers as list
        self.num_array = full_list[:, 2]                                                ##p makes num_array of the last elements in the array

    def random_word(self, words=1):                                                     ##p defines function that makes as manyv random words as inputed, if no input defaults to 1
        for x in range(words):                                                          ##p starts loop for the number of words selected
            np.random.shuffle(self.num_array)                                           ## shuffles number array
            rword = self.num_array[0]                                                   ##p sets rword as the first element of num_array
            rword = self.num_to_sym(rword)                                                ##p reverts to symbols
            rword = sym_to_word.get(tuple(rword))                                       ##p gets words from word_to_sym, sets to rword
            print('This is the random word: ', rword)                                   ##p outputs "this is the random word: ___"
            self.main(rword)                                                            ##p also calls main function, which rhymes it and makes extra words that don't necessarily spoonerize yet

    def main(self, word):
        word = word.upper()                                                             ##p capitalizes it
        nw = self.ryhmo(word)                                                           ##p rhymes it, sets to nw
        if nw != None:                                                                  ##p if nw isn't None then:
            print(word, nw)                                                             ##p print word, new word

            nw2, nw3 = self.matcher(word, nw)

            print(nw2, nw3, '\n')
        else:
            print('No Ryhme for You!!!\n'.upper())

    def sym_to_num(self, word):                                                           ##p makes a function that takes words and makes symbol words
        return [sym_to_num_dict.get(letter) for letter in word]                              ##p returns a get of sym_to_num_dict for the letter for each letter in the word provided

    def num_to_sym(self, array):                                                          ##p makes a function that takes an array of numbers and gets symbol array
        return [num_to_sym_dict.get(num) for num in array]                                   ##p gets symbols for each number array

    def sym0_checker(self,word1,word2):                                                 ##p makes function that takes two words and checks if the first letters are the same. Returns true/false
        if word1[0] == word2[0]:                                                        ##p checks if first letter is the same for both words.
            return True
        else:
            return False

    def matcher(self, caring, paring):
        caring, paring = caring.upper(), paring.upper()
        carrots, parrots = self.similo(caring)
        carrots, parrots = word_to_sym.get(carrots), word_to_sym.get(parrots)
        print(carrots, parrots)
        if word_to_sym.get(paring)[0] == parrots[0]:
            print("i found a spoonerism")
            carrots, parrots = sym_to_word.get(tuple(carrots)), sym_to_word.get(tuple(parrots))
            print(carrots, parrots)
            return carrots, parrots
        else:
            self.matcher(caring, paring)

    def ryhmo(self, word):                                                               ##p defines new function rhymo
        word = word.upper()                                                              ##p capitalizes word
        word = word_to_sym.get(word)                                                       ##p gets word from word_to_sym, returns symbols. word is now the symbols
        word = self.sym_to_num(word)                                                       ##p converts symbols to numbers
        np.random.shuffle(
            self.num_array)                                                              ##p shuffles the array containing word symbol number sets. np.random.shuffle alters num_array without =
        for x in range(len(word), 0, -1):                                                ##p starts loop for each in range of the size of the word reducing til 0, starting at length of word
            for y in self.num_array:                                                     ##p starts loop for each in num_array, which has been randomly shuffled.
                # if len(y[1:]) == x:                                                    ##p if the word is the same as the one selected starting from the second symbol
                if y[1:] == word[1:]:                                                    ##p if first word from num_array is the same as x starting from the second position
                    if y != word:                                                        ##p if it's not equal to the word we started with
                        new_word = y                                                     ##p sets new word equal to the one that satisfies the conditions.
                        return sym_to_word.get(tuple(self.num_to_sym(new_word)))             ##p returns the new word reverted to symbols reverted to letters.

    def similo(self, caring):                                                              ##p similo finds carrot and parrot from caring, but parrot not matched with paring by char[0]
        caring = caring.upper()                                                              ##p uppercases word
        caring = word_to_sym.get(caring)                                                     ##p gets symbols of word
        caring = self.sym_to_num(caring)                                                     ##p converts to numbers

        fl = caring[0]                                                                     ##p set fl to first symbol of word

        np.random.shuffle(self.num_array)                                                ##p shuffles num_array

        for carrot in self.num_array:                                                         ##p sets up for loop for each value of the dictionary of numbers
            if carrot[0] == fl:                                                               ##p if fl is the first symbol of x
                carrot = sym_to_word.get(tuple(self.num_to_sym(carrot)))                           ##p gets the word of the symbol of the number of x
                parrot = self.ryhmo(carrot)                                                       ##P rhymes x, sets it to x1
                if parrot != None:                                                           ##p if x1 isn't empty:
                    return carrot, parrot


x, y = spoonerize().matcher("sam", "ham")

