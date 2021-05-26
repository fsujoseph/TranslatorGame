# Translator Game

## Project Description

This project utilizes Google Translate's API service to create a game that helps the user learn a new language. There are 2 modes:

1. Given a word, guess what it is in the language you are learning.

2. Given a sentence, guess what the word is that fills in the blank.

The cool thing about this project is that it allows the user to select the theme of the current words/sentences the user is being tested on. For example, the topic
initializes as Oregon State University (my school), but has an option to enter the name of a valid Wikipedia article and change the pool of words/sentences to that
topic. This is done by using a Wikipedia web scraping microservice my teammate developed. In turn, I provide a translation service as a microservice.

There is also an option to check the answer in case you are stuck. The programs tracks your current score, high score, and saves it for next time.

This project was great for learning about the different strategies of building software products in the real world. It was also my first experience using Tkinter
and helped polish my skills for the next time I develop a Python GUI.

## Improvements

I would like to create a more dynamic GUI in the future. It's pretty barebones right now. It gets the job done, but the layout is boring to look at and could use
improvement. I would also like to spend more time debugging. If the user enters an invalid Wikipedia article it will most likely encounter an error. I also had
to develop a set of code that cleans out data from the scraped Wikipedia data because the raw data contains symbols, newlines, sources, etc. A lot of the article 
doesn't end up being used and there's a chance something that doesn't make sense makes it into the clean data set. 
