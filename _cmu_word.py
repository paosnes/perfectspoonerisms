# this will be for defining the class that is a "word" for the purposes of the spooneriser

class CMUWord:
    '''
    A CMU dictionary word.
    Contains the spelling and pronunciation of a word.
    '''
    def __init__(self, word, pronunciation):
        # make sure everything is uppercase
        self.word = word.upper()
        self.pronunciation = [symbol.upper() for symbol in pronunciation]


    def __str__(self):
        out_string = ""
        out_string += f"Word: {self.word}\n"
        out_string += f"Pronunciation: {self.pronunciation}\n"
        return out_string
        


class SpoonerizerWord( CMUWord ):
    '''
    Inherits from CMUWord.
    Adds the following class variables for use with spoonerizing:
        Beginning
        Ending
    '''

    def __init__(self, word, pronunciation, cmu_consonants, cmu_vowels):
        super().__init__(word, pronunciation)

        self.beginning = self.__find_beginning(cmu_consonants,cmu_vowels)
        self.ending = self.__find_ending(cmu_consonants,cmu_vowels)

    def __str__(self): 
        out_string = super().__str__()
        out_string += f"Beginning: {self.beginning}\n"
        out_string += f"Ending: {self.ending}\n"
        return out_string


    def __find_beginning(self, cmu_consonants, cmu_vowels):
        '''
        The beginning of a word is defined as follows:
            If a word starts with a consonant, the beginning is that consonant up to, and including, the next vowel.
            If a word does not start with a consonant, it has no "beginning" for the sake of spoonerisms. 
        '''
        
        if cmu_consonants.is_consonant( self.pronunciation[0] ):    # if the first symbol in the word's pronunciation is a consonant
            for symbol in self.pronunciation:                       # scan through all of the pronunciation
                if cmu_vowels.is_vowel( symbol ):                   # once a vowel is found
                    index = self.pronunciation.index( symbol )      # take note of where that vowel is
                    return self.pronunciation[ : index ]            # return everything from the beginning of the word (including the vowel)
        else:
            return None                                             # if the first symbol of the word is not a consonant, return None 

    def __find_ending(self, cmu_consonants, cmu_vowels):
        '''
        The ending of a word is defined as follows: 
            If the word starts with a consonant, the ending is everything after that consonant.
            If the word does not start with a consonant, the ending is the whole word.
        This function finds the subset of pronunciation symbols that make up the ending of a word.
        '''

        if cmu_consonants.is_consonant( self.pronunciation[0] ):    # if the first symbol in the word's pronunciation is a consonant
            for symbol in self.pronunciation[1:]:                   # scan through the pronunciation until you find a vowel
                if cmu_vowels.is_vowel( symbol ):                   # once a vowel is found
                    index = self.pronunciation.index( symbol )      # take note of that vowels position in the list
                    return self.pronunciation[ index : ]            # return all the pronunciation symbols after, and including that vowel
                elif symbol is self.pronunciation[-1]:              # if you get all the way to the end without finding a vowel
                    return self.pronunciation                       # the ending of the word is the whole word
        else:
            return self.pronunciation


# Using both the CMUVowel and CMUConsonant classes help passively error check for if someone 

class CMUVowels:
    '''
    Contins the list of all the cmu vowels.

    is_vowel(symbol) -> returns True if symbol is a vowel, else False
    '''

    vowel_list = ("AA", "AA0", "AA1", "AA2", "AE", "AE0", "AE1", "AE2", "AH", "AH0", "AH1",
                      "AH2", "AO", "AO0", "AO1", "AO2", "AW", "AW0", "AW1", "AW2", "AY", "AY0",
                      "AY1", "AY2", "EH", "EH0", "EH1", "EH2", "ER", "ER0", "ER1", "ER2", "EY",
                      "EY0", "EY1", "EY2", "IH", "IH0", "IH1", "IH2", "IY", "IY0", "IY1", "IY2",
                      "OW", "OW0", "OW1", "OW2", "OY", "OY0", "OY1", "OY2", "UH", "UH0", "UH1",
                      "UH2", "UW", "UW0", "UW1", "UW2")

    def is_vowel(self, symbol):
        if symbol.upper() in self.vowel_list:
            return True
        else:
            return False

class CMUConsonants:
    '''
    Contains the list of all the cmu consonants.

    is_consonant(symbol) -> returns True if symbol is a consonant, else False
    '''

    consonant_list = ("B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L", "M", "N", "NG", "P", "R",
                          "S", "SH", "T", "TH", "V", "W", "Y", "Z", "ZH")

    def is_consonant(self, symbol):
        if symbol.upper() in self.consonant_list:
            return True
        else:
            return False


def main():

    # === Usage and testing ===

    vowels = CMUVowels()
    consonants = CMUConsonants()

    print("What is \'K\'?")
    print(f"Is K a vowel?: {vowels.is_vowel('k')}")
    print(f"Is K a consonant?: {consonants.is_consonant('K')}\n")

    print("What is \'AA\'?")
    print(f"Is A a vowel?: {vowels.is_vowel('aa')}")
    print(f"Is A a consonant?: {consonants.is_consonant('AA')}\n")

    apple = SpoonerizerWord("apple", ["ae1", "p", "ah0", "l"], consonants, vowels)
    print(apple)

    carrot = SpoonerizerWord("CARROT", ["K", "AE1", "R", "AH0", "T"], consonants, vowels)
    print(carrot)

    anatomy = SpoonerizerWord("ANATOMY", ["AH0", "N", "AE1", "T", "AH0", "M", "IY0"], consonants, vowels)
    print(anatomy)


if __name__ == "__main__":
    main()