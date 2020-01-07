#[derive(Debug, Clone)]
pub struct WordObj {
    pub word_: String,
    pub pronunciation_: Vec<String>,
    // pub enphasis_: Vec<usize>,                   // add this
}
impl WordObj {
    pub fn new() -> Self {
        Self {
            word_: String::new(), 
            pronunciation_: Vec::new(),
        }
    }
    pub fn build(word: String, pronunciation: Vec<String>) -> Self {
        Self {
            word_: word,
            pronunciation_: pronunciation,
        }
    }
}