https://github.com/Allegheny-Ethical-CS/FakeNewsDetection/.github/workflows/CI/badge.svg

# Fake News Detection

## Sample Activity for the AI Course at Allegheny College

# Table of contents

* [About](#about)
* [Features](#features)
* [Installation](#installation)
* [Run](#run)
* [Reading Material](#reading-material)
* [Ethical discussions](#ethical-discussions)
* [Future work](#future-work)
* [Data used](#data-used)
* [Contact](#contact)

## About

Media outlets and social media platforms run rampant with "fake news," or information that has not been fact-checked, especially as they become more opinionated and stray away from centrist, fact-based reporting. This is an increasing issue in reporting, as the public receives most of their information in this way and depend on these outlets to be informed. According to [BBC](https://www.bbc.co.uk/bitesize/articles/zjykkmn), false information can take many forms (satire, clickbait, propaganda, and mistakes), and it can be classified as disinformation or misinformation. It is very difficult for the public to identify any media outlet or social media post as any of these classifications without reading competing claims or doing their own research. Therefore, the purpose of this project is to show how a potential Fake News Detection tool can be built and used by various platforms to warn users of the content before they read.

This ethical tool will search through Tweets and attempt to label them as "right", "left", "centrist" and also add a level of fake news detection to them. While Twitter is currently working on this feature, it is not completely employed at the moment. The goal of this feature is to minimize the amount of fake news that the public receives from social media outlets.  This tool aims to eventually be able to use machine learning algorithms to aid in its fake news detection. This detection is done by searching the selected user's tweets for various words which indicate fake news, such as "most", "least", etc.


The project is funded by Mozilla Foundation and it will be used in Data Analytics course at Allegheny College. Please visit the [Allegheny Ethical CS](https://csethics.allegheny.edu/) for more information.


## Features

- Twitter API to search for a user, their screen name, hashtag, or keyword.
  - API from [Bluebird](https://github.com/labteral/bluebird)

- Tweet classification(binary)
  - Naive Bayes
  - Linear SVM
  - Credit to Zach Leonardo on [Polarized](https://github.com/leonardoz15/Polarized)

 - Tweet classification
    - fake
    - true
    - Credit to Favio Vazquez on [fake-news](https://github.com/FavioVazquez/fake-news)


## Installation

- Clone the source code onto your machine

    With HTTPS:

    ```https://github.com/Allegheny-Mozilla-Fellows/FakeNewsDetection.git```

    or With SSH:

    ```git@github.com:Allegheny-Mozilla-Fellows/FakeNewsDetection.git```


## Run

After pulling the repo, install textblob and its data and install the virtual environment requirements:


```shell
pip install textblob
```

and then,
```shell
python3 -m textblob.download_corpora
```

and then, 
```shell
pipenv install --dev
```

After installing these packages, you will run the program with the command
 ```pipenv run streamlit run streamlit_web.py```

After running this command, you will be prompted to enter the name of a given senator, which the API will cross-reference with current Twitter users. You will then confirm the name of the senator and choose your preferred diagram for output.



## Future work

Currently, this project examines tweets using a Twitter API provided by Bluebird. This project can be furthered by adding more classifications to the tweets or adding features to visualize how many tweets contain false information, and its effect on society, the media, and democracy. Another great addition to the project would be utilizing other methods to detect fake news, such as coding different algorithms, developing a Bot, or using AI.

## Reading Material

Here is the list of articles that may give the user more insights into fake news detection.

- [Fake News Detection Algorithms Using Keywords](https://news.mit.edu/2018/mit-csail-machine-learning-system-detects-fake-news-from-source-1004)

- [NLP Fake News Detection is Vulnerable to Attacks](https://arxiv.org/pdf/1901.09657.pdf)

- [Fake News Classification is More Difficult than Identifying it](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1036&context=datasciencereview)

- [Facebook Will Use Fake News Detection](https://www.wired.com/story/facebook-click-gap-news-feed-changes/)

- [Twitter Will Use Fake News Detection](https://www.analyticsvidhya.com/blog/2019/12/detect-fight-neural-fake-news-nlp/)


## Ethical Discussions

- What happens if one news outlet or platform produces more fake news than another? Will that alter the way we perceive news and/or classify facts?

- Why might algorithms be particularly harmful for detecting fake news?

- Should we enforce using fake news detecting algorithms? Do media outlets and social media platforms have an obligation to detect fake news?

- What are some of the ways we can prevent biases in fake news detection algorithms as developers and as users?


## Data used

The data used in this project is retrieved from the Twitter website.


## Contact

If you have any questions or concerns about this project please contact:

- Dr. Jumadinova(jjumadinova@allegheny.edu)
- Rachael Harris (harrisr@allegheny.edu)
