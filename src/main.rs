// use std::collections::BTreeMap;
use std::io::{stdin,stdout,Write};

mod spoonerize_utils;

use spoonerize_utils::word_obj::WordObj;
use spoonerize_utils::file_import::read_file_to_word_object_vector;
use spoonerize_utils::rhyme::check_rhyme;



fn main() {

    print!("Loading... ");
    let _ = stdout().flush().unwrap();

    let words = read_file_to_word_object_vector("resource/cmudict-0.7b.txt");

    println!("Done.");
    println!("{} words imported.\n",words.len());

    let user_input = get_user_input("Enter words to get their pronunciations: ");
    let pronunciations = get_word_pronunciation(&user_input, &words);

    for word in &pronunciations {
        println!("{}: {:?}",word.word_, word.pronunciation_);
    }
    println!();

    let alliterations = check_alliteration(&user_input[0], &words);
    println!("Checking alliterations for the first input word {}.",&user_input[0]);
    println!("{} alliterations found:", alliterations.len());
    let continue_input = get_user_input("Print alliterations? [y/n] "); 
    if continue_input[0] == "Y".to_string() {   
        for word in &alliterations {
            println!("{}",word.word_);
        }
        println!();
    }
    else { println!(); }

    let rhymes = check_rhyme(&user_input[0], &words, 2);                        // from some simple testing, 2 is the minimum the rhyme tolerance can be to actually work
    println!("Checking rhymes for the first input word {}.",&user_input[0]);
    println!("{} rhymes found:", rhymes.len());
    let continue_input = get_user_input("Print rhymes? [y/n] "); 
    if continue_input[0] == "Y".to_string() {   
        for word in &rhymes {
            println!("{}",word.word_);
        }
        println!();
    }
    else { println!(); }

    // b_tree_test()

}



// !!!!! should the pronunciation symbol be used? and/or the first char of the actual word???
// check if there are any other word that alliterate with an input word (only the first pronunciation symbol is used)
fn check_alliteration(word_in: &String, pronunciation_reference: &Vec<WordObj>) -> Vec<WordObj> {
    let mut output: Vec<WordObj> = Vec::new();              // initialize the Vec<WordObj> for returning the pronunciations

    let mut ref_found = false;                              // set up a boolean to keep track of if a input word is in the reference list
    let mut temp_ref_word: WordObj = WordObj::new();        // initialize a variable for the reference word
    for ref_word in pronunciation_reference {               // check every word in the reference list
        if *word_in == ref_word.word_ {                     // if the input word is in the reference list
            temp_ref_word = ref_word.clone();               // set the reference word to a clone of the reference WordObj
            ref_found = true;                               // if the word was added, keep track of that
        }
    }
    let mut alliteration_found = false;                     // initialize variable to keep track of if there was an alliteration in the reference list
    if ref_found {                                          // if there was a reference word found
        for ref_word in pronunciation_reference {           // go through every word in the reference list
            if temp_ref_word.pronunciation_[0] == ref_word.pronunciation_[0] && temp_ref_word.word_ != ref_word.word_ {
                                                            // if the first pronunciation symbol of the temp_ref_word and the current word from the reference list are the same
                                                            // and the current word is not the temp_ref_word 
                output.push(ref_word.clone());              // push a clone of the current word to the output list
                alliteration_found = true;                  // keep track of there being an alliterative match
            }
        }
        if !alliteration_found {                            // if there was no alliterative match
            return output                                   // return the empty Vec<WordObj> (using 'return' keyword here to enforce return type)
        }
    }
    output                                                  // return the Vec<WordObj> of the word alliteration matche
}

// enter a bunch of words and return their pronunciations
fn get_word_pronunciation(words_in: &Vec<String>, pronunciation_reference: &Vec<WordObj>) -> Vec<WordObj> {
    
    let mut output: Vec<WordObj> = Vec::new();          // initialize the Vec<WordObj> for returning the pronunciations

    for check_word in words_in {                        // for each of the input words, check what it's pronunciation is
        let mut added = false;                          // set up a boolean to keep track of if a input word has a pronunciation
        for ref_word in pronunciation_reference {       // check every word in the reference list
            if *check_word == ref_word.word_ {          // if the input word is in the reference list
                output.push(ref_word.clone());          // add a clone of the WordObj the represents the input word
                added = true;                           // if the word was added, keep track of that
            }
        }
        if !added {                                     // if the word was not added
            output.push(WordObj::new());                // add an empty WordObj
        }
    }
    output                                              // return the Vec<WordObj> of the word pronunciations
}

// get user input and return a Vec<String> of all 
fn get_user_input(input_prompt: &'static str ) -> Vec<String> {
    
    let mut s = String::new();                                              // initialize a new String
    print!("{}", input_prompt);                                             // print the input prompt
    let _ = stdout().flush().unwrap();                                      // flush stdout to keep input on same line as print
    stdin().read_line(&mut s).expect("Did not enter a correct string");     // read in the input and put it in the String
    if let Some('\n') = s.chars().next_back() {                             // check to see if there are \n or \r characters in the String and remove them 
        s.pop();
    }
    if let Some('\r') = s.chars().next_back() {
        s.pop();
    }

    let word_vec = s.split(" ");                                            // split the string by whitespace

    let mut output: Vec<String> = Vec::new();                               // initialize new Vec<String>
    for word in word_vec {                                                  // for each word from the input string
        output.push( word.to_string().to_uppercase() );                     // convert that word to an uppercase String
    }

    output                                                                  // return the Vec<String>
} 

// fn b_tree_test() {
//     let mut test_tree = BTreeMap::new();

//     let a = "aaron";
//     let a: String = a.to_string().to_uppercase();
//     // let a: String = a.to_uppercase();
//     let a = a.as_str();
//     let b = vec!["EH1", "R", "AH0", "N"];

//     test_tree.insert(a,b);

//     let a = "aaron's";
//     let a: String = a.to_string();
//     let a: String = a.to_uppercase();
//     let a = a.as_str();
//     let b = vec!["EH1", "R", "AH0", "N", "Z"];

//     test_tree.insert(a,b);

//     println!("len test: {}",test_tree.len());

//     for (word, pronuc) in test_tree {
//         println!("{}, {:?}", word, pronuc);
//     }

// }