# Generating Perfect Spoonerisms
This repository organizes the work done to auto-generate perfect spoonerisms and optimize that auto-generation. 

A [spoonerism, from Wikipedia](https://en.wikipedia.org/wiki/Spoonerism), is "named after the Oxford don and ordained minister William Archibald Spooner". A spoonerism is when a set of words' initial sounds are switched among each other and new words or funny-sounding pseudo-words are created; a classic example from Mr. Spooner being: "is it kisstomary to cuss the bride?". These spoonerisms don't necessarily create new words, they can just make utterances that sound humorous. Kisstomary isn't a word, and if it were, the effect of this spoonerism might actually be less humorous, or just simply confusing. 

There is another set of spoonerisms, which are the subject of this project. They arise when the shuffled words either get spelled or pronounced as valid words, or nearly-valid words. I call these "perfect" spoonerisms. Perfect spoonerisms are either spoonerisms in how they are pronounced, or how they are spelled, or both. I might end up calling the spoonerisms that work both on spelling and pronounciation "**more** perfect" spoonerisms. My prime example of a **more** perfect spoonerism is "caring parrots paring carrots". It's the best I have come across. It conjures an image, makes sense as a short phrase, and is somewhat humorous on its own, though admittedly less so than some of the best non-perfect spoonerisms out there. Again, note this example has the spellings preserved *and* the pronunciation preserved. It is pure coincidence that the four words are parallel in both sound and letter. I liked this so much I made it into a t-shirt, which was illustrated by Tracey Sutliff, who can be found as @ill_trace on Instagram, and the pattern can be found in the project files as "cppc.pdf". Use it wherever you like, but not without crediting the artist and myself, please. 

To think more formally, you can think of a four word spoonerism as two pairs of words notated *Ax By Bx Ay*, where *{A,B}* are two initial sounds of words that do not rhyme, and *{x,y}* are the sounds or spellings of a word after its initial sound or letters. It might seem this is equivalent to rhyming; it's not. I like to think of it as a "super" rhyme, where all of the ending sounds are the same, not just the last few of them. "Caring parrots ping carrots" isn't a spoonerism, because caring and ping aren't similar enough. You wouldn't have a "tip of the slongue" and mistake ping for caring because they aren't similar, despite technically rhyming.

The benefit of thinking of spoonerisms in this more formal form is that two useful facts become evident:

 - Useful fact 1. You do not have to start with rhyming words, and you do not have to start with words that have the same first       letter. Any two words might yield a spoonerism, the only limitation placed upon you once you select two words is that you have to find another pair of words that have the same pair of first sounds or letters as the second and first, and each share the ending sounds with each of the first words, respectively. This means that spoonerisms are not too much more difficult to test and invent than rhymes, except for that you might have to attempt them about 26 times as frequently, because once you found a super rhyme matching the first word's letter, you also have to have it match the second word's letter. 
     
- Useful fact 2. Any set of four words, when you have found a spoonerism, are still spoonerisms in three additional configurations. 
     
      Ax By                 By Ax                Bx Ay                   Ay Bx
      Bx Ay (original),     Ay Bx (mirrored sideways),    Ax By (mirrored up-down),    By Ax(mirrored both sideways and up-down)

And with the examples typed out with my favorite example:

       Caring Parrots         Parrots Caring        Paring Carrots           Carrots Paring       
       Paring Carrots,        Carrots Paring,       Caring Parrots,          Parrots Caring
       
It seems the first is the only funny one of the four. But the benefit of this permuting expansion is that once you have found a set of four words that craft a spoonerism, you have four chances to make one that's actually funny or meaningful. 

I haven't done the work of this for six word spoonerisms, mostly because I haven't found good six word spoonerisms. Stay tuned, or feel free to commit to that effort.     

## So what is this project actually about?

The plan for the work is to make a spoonerism generator code in Python and create a website and/or app to allow users to generate their own perfect spoonerisms with this code. I imagine there are even better perfect spoonerisms out there, just waiting for either a lucky human brain or an obsessive computerized one to find them. I'm always thinking about spoonerisms, but since I am not always lucky, I thought a computer might be of help, and furthermore anyone who assists me on this project on making infinite spoonerisms. 

When this stage is completed, I will make a Youtube video about the project and describing the process, and promote it so that people make their own spoonerisms and provide helpful feedback on the spoonerisms provided.

## Next steps:

After that website/app/other thing is live and well-used, it is my expectation that we can use survey results from the generated spoonerisms to craft an improved generator that selects among spoonerisms for those more likely to be funny than those generated at random. I don't know exactly what makes a set of words likely to be funny, and this is probably a classically-difficult problem in computer science, but I argue there are a number of features about spoonerisms that assist us in creating them with computers, above other funny phrase types like puns or jokes or cadences. Those features I summarize as: *the output adheres to a rigid format, the procedure contains relatively few degrees of freedom, the output be produced algorithmically, and the outputs have a lot in common with each other.*

### Rigid format: 
Spoonerisms are of the form AX BY BX BY, as described above. The first and third, as well as the second and fourth, are of the same length and rhyme with eachother. There is also a kind of alliteration, though each alliterating word is separated.

### Degrees of freedom: 
The composition of each word shares many attributes with each other word, and there aren't too many things that can change when you're making a spoonerism from a starter set of words. There are only two values of initial sounds/letters for a spoonerism containing four words, and only two ending sounds/letters. 

### Can be produced algorithmically: 
My program as it is constructed so far starts with one word, finds a word that "super rhymes" with it, then randomly picks a new word, then recursively finds rhymes for that third word until it has the same first letter as the second initial word. This process can be achieved relatively quickly by a computer, and over and over again with new results. Future work might expand this to create a master list of all possible spoonerisms, if such a thing is possible. 

### Outputs have a lot in common with each other: 
Spoonerisms can be compared for certain characteristics, and they can be compared easily because the things they might have in common they very frequently have in common. For example, there are at most four parts of speech in each spoonerism. The order of these might be important, and be associated with greater levels of humor or significance. Is it particularly likely that a funny spoonerism occurs in "adjective, predicate-noun, verb, object-noun, as it does in "caring parrots paring carrots"? Does it matter that the words are all two syllables? Does it matter that paring carrots is a sensible phrase that occurs frequently whenever at least one of those words occurs? Any of these elements might yield information that can be used to predict good spoonerisms, then report the output of a random process through the filter of those predictions, as a simulation of that data generating process. 

## End notes:

This project is open, and free for anyone to use or alter, though if you interract through this github you'll be able to benefit from others' contributions as well. I'll work out how this project is licensed soon. 


>The files are dictionaries from the CMU pronunciation dictionary.
>
>It's required statement is pasted below:
>Copyright (C) 1993-2015 Carnegie Mellon University. All rights reserved.
>
>Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
>1. Redistributions of source code must retain the above copyright
>   notice, this list of conditions and the following disclaimer.
>   The contents of this file are deemed to be source code.
>2. Redistributions in binary form must reproduce the above copyright
>   notice, this list of conditions and the following disclaimer in
>   the documentation and/or other materials provided with the
>   distribution.
>
>This work was supported in part by funding from the Defense Advanced
>Research Projects Agency, the Office of Naval Research and the National
>Science Foundation of the United States of America, and by member
>companies of the Carnegie Mellon Sphinx Speech Consortium. We acknowledge
>the contributions of many volunteers to the expansion and improvement of
>this dictionary.
>
>THIS SOFTWARE IS PROVIDED BY CARNEGIE MELLON UNIVERSITY ``AS IS'' AND
>ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
>THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
>PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL CARNEGIE MELLON UNIVERSITY
>NOR ITS EMPLOYEES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
>SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
>LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
>DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
>THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
>(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
>OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
