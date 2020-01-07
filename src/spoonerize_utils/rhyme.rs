use super::word_obj::WordObj;

// !!!!!! this needs to be modified (how many symbols count as a 'rhyme'?, one symbol isn't enough)
// check if there are any words that rhyme with the input word 
pub fn check_rhyme(word_in: &String, pronunciation_reference: &Vec<WordObj>, mut tolerance: usize) -> Vec<WordObj> {
    let mut output: Vec<WordObj> = Vec::new();              // initialize the Vec<WordObj> for returning the pronunciations

    let mut ref_found = false;                              // set up a boolean to keep track of if an input word is in the reference list
    let mut temp_ref_word: WordObj = WordObj::new();        // initialize a variable for the reference word
    for ref_word in pronunciation_reference {               // check every word in the reference list
        if *word_in == ref_word.word_ {                     // if the input word is in the reference list
            temp_ref_word = ref_word.clone();               // set the reference word to a clone of the reference WordObj
            ref_found = true;                               // if the word was added, keep track of that
        }
    }

    if temp_ref_word.pronunciation_.len() > tolerance {                                 // if the temp_ref_word is shorter than the tolerance, adjust the tolerance to be the length of the whole ref word
        tolerance = temp_ref_word.pronunciation_.len();                                 
    }

    let mut rhyme_found = false;                                                        // initialize variable to keep track of if there was an alliteration in the reference list
    if ref_found {                                                                      // if there was a reference word found
        for ref_word in pronunciation_reference {                                       // go through every word in the reference list
            let temp_ref_first_elm = temp_ref_word.pronunciation_.len() - tolerance;
            // let mut ref_word_first_elm = 0;
            if ref_word.pronunciation_.len() < tolerance {
                continue;
            }
            let ref_word_first_elm = ref_word.pronunciation_.len() - tolerance;


            // let temp_ref_last_elm = temp_ref_word.pronunciation_.len() - 1;
            // let ref_word_last_elm = ref_word.pronunciation_.len() - 1;
            let mut tol_counter = 0;                                                    // counter var to make sure that the word rhymes
            for i in 0..tolerance {                                                     // go through the last n pronuciation symbols of both words

                if temp_ref_word.pronunciation_[temp_ref_first_elm + i] == ref_word.pronunciation_[ref_word_first_elm + i] 
                    && temp_ref_word.word_ != ref_word.word_ {
                                                                // if the first pronunciation symbol of the temp_ref_word and the current word from the reference list are the same
                                                                // and the current word is not the temp_ref_word 
                    tol_counter += 1;
                    // output.push(ref_word.clone());           // push a clone of the current word to the output list
                    // rhyme_found = true;                      // keep track of there being an alliterative match
                }

            }

            if tol_counter == tolerance {
                output.push(ref_word.clone());              // push a clone of the current word to the output list
                rhyme_found = true;                         // keep track of there being an alliterative match
            }
        }
        if !rhyme_found {                                   // if there was no alliterative match
            return output                                   // return the empty Vec<WordObj> (using 'return' keyword here to enforce return type)
        }
    }
    output                                                  // return the Vec<WordObj> of the word alliteration matche
}