#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:13:08 2023

@author: sam
"""

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"{word1}:{word2}:{word1.similarity(word2)}")
print(f"{word3}:{word2}:{word3.similarity(word2)}")
print(f"{word3}:{word1}:{word3.similarity(word1)}")


#The way which it decides which words are similair may be different
#to how humans associate words. Because cat and monkey seem less similair 
# to me than banana and monkey. But the algorithm probably thinks cat and monkey
# are similair because they are both mammals. 

tokens = nlp('cat apple monkey banana primates human')
for token1 in tokens:
 
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
      
      
      
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ", similarity)