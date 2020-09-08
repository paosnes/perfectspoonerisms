# this will be for all of the scripts that load in the cmu dict files and builds all of the cmu_word objects
# this will also have the option to export the built list of objects to json,
# load the same type of json that it exported (for speed),
# or just load all the input files, built the list of objects and use that in the code
from _cmu_word import SpoonerizerWord, CMUVowels, CMUConsonants

class CMUDictionary:
    '''
    The object that builds and stores all of the CMU dictionary information.
    '''

    def __init__(self, cmudict, cmusymbols=None):
        # 'cmudict-0.7c.txt'
        
        vowels = CMUVowels()
        consonants = CMUConsonants()

        self.words = self.__import_cmudict(cmudict, consonants, vowels)

    def __str__(self):
        out_string = ""
        out_string +=  "CMU Dictionary:\n"
        out_string += f"  Contains {len(self.words):,d} words.\n"
        out_string += f"  First word: {self.words[0].word}\n"                   # this is sorta sloppy, think of something better
        out_string += f"  Last word: {self.words[len(self.words)-1].word}\n"    # ^
        
        return out_string



    def __import_cmudict(self, cmudict, cmu_consonants, cmu_vowels):
        '''
        Imports the CMU_dict word document:
            All lines that start with ;;; are ignored.
            First element of each line treated as the word
            All proceeding elements treated as the ponunciation for that word

        Builds a list of SpoonerizerWords
        -> optomization needed 
        '''

        all_words = []  # <- there is likely a much better way to do this, dictionary? check performance
        with open(cmudict, 'r') as file:
            for line in file:
                l = line.strip().split()
                if l[0] != ';;;':
                    spoon_word = SpoonerizerWord(l[0], l[1:], cmu_consonants, cmu_vowels)
                    all_words.append( spoon_word )

        return all_words

    # I'm not sure we need CMU symbols anymore because of the checks in CMUVowel and CMUConsonant
    # Those classes will passively keep track of all the symbols that are possible 

    # def import_cmusymbols(self):
    #     '''
    #     -Creates s_list
    #     -Opens CMU symbols, just a list of all 84 symbols.
    #     -Appends each line from symbol dict to s_list
    #     -Creates n_list which is a list of the numbers in range(len(s_list))
    #     -Creates sym_to_num_dict, a dictionary of symbol to number
    #     -Creates num_to_sym_dict, a dictionary of number to symbol
    #     :return: sym_to_num_dict, num_to_sym_dict
    #     '''
    #     s_list = []  ##p makes new list s_list
    #     with open('cmudict-0.7b.symbols.txt', 'r') as file:  ##p opens cmudict-0.7b.symbols.txt, reads, names it "file"
    #         for line in file:  ##p starts loop for each line in file
    #             l = line.strip()  ##p makes l variable of removed spaces from line in file
    #             s_list.append(l)  ##p adds it to end of s_list. s_list is a list of all the symbols

    #     n_list = list(range(len(s_list)))  ##p makes a list of the range of the length of s_list. In other words, tells you all the positions of all the lines in s_list
    #     sym_to_num_dict = {s_list[x]: n_list[x] for x in range(len(s_list))}  ##p makes a dictionary of the symbol and the number on n_list
    #     self.num_to_sym_dict = {n_list[x]: s_list[x] for x in range(len(s_list))}  ##p makes a dictionary of the number on n_list and the symbol (reversed of prior)
    #     return sym_to_num_dict, self.num_to_sym_dict  ##p returns symbol dictionary


def main():

    # === Usage and testing ===

    words = CMUDictionary('cmudict-0.7c.txt') # 'cmudict-0.7b.symbols.txt'

    print(words)

    # for i in range(5):
    #     print(words.words[i])

if __name__ == "__main__":
    main()