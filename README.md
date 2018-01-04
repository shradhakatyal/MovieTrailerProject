# Movie Trailer Project

A movie trailer project that uses Python to generate static webpage. A class Movie is used to create objects of different movies that are then listed on the webpage. The posters of the movies are displayed and on clicking it a YouTube trailer is played. This project has been developed for <a href="https://in.udacity.com/">Udacity's</a> __Full Stack Nanodegree course__.

## Getting Started

The _following instructions_ will help you setup the project on your machine.

### Prerequisites

Python should be available on your machine for the project to work. To download and install python, see https://wiki.python.org/moin/BeginnersGuide/Download

### Demo

_To see a demo of the project, click <a href="https://shradhakatyal.github.io/MovieTrailerProject/fresh_tomatoes.html">here!</a>_

### Quick Start

After downloading the files, the project can be run by adding fresh\_tomatoes.py and media.py to the top of the python file. Add information like title, storyline, poster\_image\_url and trailer\_youtube\_url and create an object by calling  media.Movie() and by passing the four arguments. Call the fresh\_tomatoes.open\_movies\_page() function and pass the movie object as an argument. Run your python file to generate the webpage. For the purpose of <a href="https://shradhakatyal.github.io/MovieTrailerProject/fresh_tomatoes.html">demo</a>, entertainment\_center.py can be used.

#### Steps
Python must be installed on your system. _See Prerequisites_
1. Download fresh\_tomatoes.py, media.py and entertainment\_center.py
2. Download the css file- movie.css
3. Save all three python files in the same folder and the css file under a separate folder css.
4. The file entertainment\_center.py has to be run. There are two ways to run this file.

_Using the python IDLE_
5. Open the file entertainment\_center.py in the IDLE.
6. Click on __run module__ present inside __run__.

_Using the command line_
5. Open the command line
6. Go to the directory where entertainment\_center.py is saved using cd.
```
Example:
>cd Desktop\MovieTrailerProject
```
7. Run the file by appending the file name to .\
```
Example:
>.\entertainment_center.py
```

## Information

media.py contains the Movie class which has four class variables and one function \_\_init\_\_ that is used to initialize the class variables. The four class variables are: title, storyline, poster\_image\_url and trailer\_youtube\_url.

fresh\_tomatoes.py contains the html markup and two functions open\_movies\_page and create\_movie\_tiles\_content that are used to add and display movie content on the static webpage.

entertainment\_center.py imports the two files and is used to create objects of type Movie. The function open\_movies\_page is called by passing the list of movie objects as an argument.

css folder contains movie.css which has been used to style the html page.

## Copyright
The __starter code__ for this project has been provided by <a href="https://in.udacity.com/">Udacity</a>
