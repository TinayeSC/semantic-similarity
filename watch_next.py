#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:33:22 2023

@author: sam
"""

#importing spacy
import spacy 

#loading the module
nlp = spacy.load('en_core_web_md')

#defining an empty str to store all the movies onto
movies = ""

#importing the extrenal file movies.txt and saving the movies as a variable
with open("movies.txt","r+") as m:
    for lines in m:
        movies+= lines
        
#converting the string into a list seperated by each movie        
movies = movies.split("\n")
# for movie in movies:
#     print(movie)
    

#defining the movie we want to find reccomendations for
recommend_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


#defining a function to return the movie title and its descrpition if it is most similar to 
# the inputted movie    
def watch_next(movie= recommend_movie):
    #defining an empty dictionary to store the movies and their similarity 
    similar_movies = {}
    
    #defining an empty list to store similarities 
    qty_similarities = []
    
    #using spacy to convert the movie description to be usable by nlp 
    watched_movie = nlp(movie)
    
    # a for loop that iterates over every movie, adding the movie description and its 
    #similarity to the dictionary and the empty list 
    for movie in movies:
        similarity = nlp(movie).similarity(watched_movie)
        similar_movies[f"{movie}"] = similarity
        qty_similarities.append(similarity)
    
    #using the max() command to find the movie with the highest similarity 
    most_similar = max(qty_similarities)
    
    #finding the key that corresponds to the highest value (highest similarity )
    similar_movie = str({i for i in similar_movies if similar_movies[i]==most_similar})
   
    #printing the information found
    print(f"Spacy's similarity module thinks that you should watch {similar_movie[2:9]}. ")
            
    
    print("\n")
    print("Here is the description")
    print("\n")
    print(similar_movie)
    print("\n \n \n \n \n")
    print(f"{similar_movie[2:9]} is {most_similar} similar to the movie you watched. ")
    print("\n \n \n \n \n")
        
        
        
        
        
        
watch_next()