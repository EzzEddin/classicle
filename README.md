[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Class*icle* :book:
Class*icle* is a Natural Language Processing project that can classify your article out of five classes: business, entertainment, politics, sport, tech. It is read like _classical_ and it is a merge between the prefix of **class**ify and the suffix of art**icle**.

## Demo
![classicle_demo](https://user-images.githubusercontent.com/11898152/71850472-08b1d800-30dd-11ea-964d-aea73a131f95.gif)

## How to use class*icle*
1. Clone this project and cd into the classifybutton folder:
```
$ git clone https://github.com/EzzEddin/classicle.git
$ cd classifybutton
```

2. Using python3, run the following:
```
$ python3 manage.py runserver 127.0.0.1:8002
```
3. Go to the browser and write the server link, in the url, that you specified in the last command `127.0.0.1:8002`
4. The page you saw at the demo will apear so you can put your article in there to classify.

### Setup
Install dependencies:
- django
- tensorflow
- keras
- pickle
- numpy 
- csv
- wget (optional)

## How class*icle* works
Class*icle* is a project run on a django server just by clicking on *classify* button, it will run the python script which has the deep learning model.

## Data
The data I used for training and testing is bbc-news articles available [here](http://mlg.ucd.ie/datasets/bbc.html).

## Acknowledgements
The deployment and deep learning model in this project are inspired by [Browser-based Models with TensorFlow.js](https://www.coursera.org/learn/browser-based-models-tensorflow/home/welcome) course and [Natural Language Processing in TensorFlow](https://www.coursera.org/learn/natural-language-processing-tensorflow/home/welcome) course while running the model written in python script by a click on a button at django server is inspired by this [blog](https://www.hackanons.com/2019/04/run-python-script-on-clicking-html.html).
I also want to thank my friend Nour for answering my questions whether in development or testing. Thank you, [guru](https://github.com/noureddin).


## License
MIT, Copyright (C) 2020 by Ezz El Din Abdullah

