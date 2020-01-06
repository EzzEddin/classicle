[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Class*icle* :book:
Class*icle* is a Natural Language Processing project that can classify your article out of five classes: business, entertainment, politics, sport, tech. It is read like _classical_ and it is a merge between the prefix of **class**ify and the suffix of art**icle**.

## Demo
![classicle_demo](https://user-images.githubusercontent.com/11898152/71850472-08b1d800-30dd-11ea-964d-aea73a131f95.gif)

## How to use class*ical*
1. Clone this project and cd into the classifybutton folder
```
$ git clone https://github.com/EzzEddin/classicle.git
$ cd classifybutton
```

2. Using python3, run the following:
```
$ python3 manage.py runserver 127.0.0.1:8002
```
3. Go to the browser and write the server link, in the url, that you specified in the last command `127.0.0.1:8002`
4. The page you saw at the demo will apear so you can put your article in there to classify

## How class*icle* works
Class*icle* is a project run on a django server just by clicking on *classify* button, it will run the python script which has the deep learning model


## Setup
Install dependencies:
- tensorflow
- keras
- pickle
- numpy 
- csv
- wget (optional)

## Data
The data I used for training and testing is bbc-news articles available [here](http://mlg.ucd.ie/datasets/bbc.html).

## License

MIT, Copyright (C) 2020 by Ezz El Din Abdullah

