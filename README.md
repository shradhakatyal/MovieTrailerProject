# Movie Trailer Project

A movie trailer project that uses Python to generate static webpage. A class Movie is used to create objects of different movies that are then listed on the webpage. The posters of the movies are displayed and on clicking it a YouTube trailer is played. This project has been developed for Udacity's Full Stack Nanodegree course.

## Getting Started

The following instructions will help you setup the project on your machine.

### Prerequisites

Python should be available on your machine for the project to work. To download and install python, see https://wiki.python.org/moin/BeginnersGuide/Download

### Download

### Quick Start

After downloading the files, the project can be run by adding fresh\_tomatoes.py and media.py to the top of the pyhton file. Add information like title, storyline, posterimage and youtubetrailer and create an object by calling  media.Movie() and by pasisng the four arguments.Call the fresh\_tomatoes.open\_movies\_page() function and pass the movie object as an argument. Run your python file to generate the webpage. For the purpose of demo, entertainment\_center.py can be used.

## Information

media.py contains the Movie class which has four class variables and one function \_\_init\_\_ that is used to initialize the class variables. The four class variables are:title, storyline, poster\_image\_url and trailer\_youtube\_url.
fresh\_tomatoes.py contains the html markup and two functions open\_movies\_page and create\_movie\_tiles\_content that are used to add and display movie content on the static webpage.
entertainment\_center.py imports the two files and is used to create objects of type Movie. The function open\_movies\_page is called by passing the list of movie objects as an argument.
