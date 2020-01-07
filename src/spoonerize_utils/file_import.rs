use std::fs::File;
use std::io::Read;

// mod word_obj;
use super::word_obj::WordObj;

// read in a file of the correct format and convert it into a Vec<WordObj> to keep track of the word spelling and pronunciation 
pub fn read_file_to_word_object_vector(filelocation: &'static str) -> Vec<WordObj> {

    let lines = read_file_to_string_vector(filelocation);                                           // read in the file and return a Vec<String> where each string is a line of the file

    let mut all_words: Vec<WordObj> = Vec::new();                                                   // initialize the Vec<WordObj>
    for curr_line in lines {                                                                        // for every line in the vector of lines
        if curr_line[..3] == *";;;" { continue; }                                                   // continue if the line starts with ";;;" which is the custom comment symbol

        let mut word_pronunciation_pair = curr_line.split("  ");                                    // split the line at the double space after the word spelling
        
        let current_word: String = word_pronunciation_pair.next().unwrap().to_string();             // convert the first section into string: this is the word spelling

        let mut current_pronunciation: Vec<String> = Vec::new();                                    // create a vector for the pronunciation symbols
        let temp_pronunciation: String = word_pronunciation_pair.next().unwrap().to_string();       // convert the second half of the split into a string and split it by whitespace
        let temp_pronunciation_split = temp_pronunciation.split(" ");                               //   need to do this in two lines to prevent freeing a temporary variable before splitting
        for symbol in temp_pronunciation_split {                                                    // for each symbol in the split symbol iterator
            let temp_symbol: String = symbol.to_string();                                           // convert that symbol into a string
            current_pronunciation.push(temp_symbol);                                                // add it to the vector of pronunciation symbols for that word
        }
        
        // let temp_word_obj = WordObj {                                                               // build the WordObj struct
        //     word_: current_word,
        //     pronunciation_: current_pronunciation,
        // };
        let temp_word_obj = WordObj::build(current_word, current_pronunciation);

        all_words.push(temp_word_obj);                                                              // push that WordObj to the vector of all the WordObjs
    }

    all_words                                                                                       // return the Vec<WordObj>
}

// read in a text file into a string vector of all the lines of the file
fn read_file_to_string_vector(filelocation: &'static str) -> Vec<String> {
    let filelocation: String = filelocation.to_string();                        // take file location slice and convert to string
    let file = read_file(filelocation);                                         // read in the file and return a Vec<u8>
    let file = convert_file_to_string(file);                                    // convert Vec<u8> into a String
    let file = file.lines();                                                    // split the String into an iterator of all it's lines
    let mut all_lines: Vec<String> = Vec::new();                                // initialize vector of all the lines
    for line in file {
        all_lines.push(line.to_string());                                       // push all of the properly formated lines into Vec<String> of all the lines
    }
    all_lines                                                                   // return the Vec<String>
}

// convert a vector of u8 into a string
fn convert_file_to_string(file_data: Vec<u8>) -> String {
    let file = std::str::from_utf8(&file_data);                                 // create the Result<> by trying to convert the Vec<u8> to str using UTF-8 encoding

    let file = match file {                                                     // decide what to do based on the Result<> value
        Ok(file) => file.to_string(),                                           // if a str can be returned, convert it to a String and return that
        Err(_error) => {                                                        // if you can't convert to str (there was an error):
            let mut temp_file: Vec<char> = Vec::new();                          // create new empty Vec<char>
            for c in file_data {                                                // for every u8 in file_data
                temp_file.push(c as char);                                      // read the u8 as if it is a char
            }
            let temp_file: String = temp_file.into_iter().collect();            // take the Vec<char> and collect it into a String
            temp_file                                                           // set 'file' to that String
        }
    };

    file                                                                        // return the String
}   

// import a text file as a vector of u8
fn read_file(file_name: String) -> Vec<u8> {
    let mut file_content = Vec::new();                                          // initialize a new Vec<u8>
    let mut file = File::open(&file_name).expect("Unable to open file");        // try to open the file
    file.read_to_end(&mut file_content).expect("Unable to read");               // try to read the file
    file_content                                                                // return the Vec<u8>
}