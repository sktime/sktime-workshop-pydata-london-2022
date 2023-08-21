<a href="https://sktime.net"><img src="https://github.com/alan-turing-institute/sktime/blob/main/docs/source/images/sktime-logo-no-text.jpg?raw=true)" width="175" align="right" /></a>

Welcome to the sktime tutorial at PyData London 2022
====================================================

### How to implement your own estimator

:tv: [watch on youtube](https://youtu.be/S_3ewcvs_pg)

This tutorial is about [sktime] - a unified framework for machine learning with time series. sktime features various time series algorithms and modular tools for sktime is a widely used scikit-learn compatible library for learning with time series. sktime is easily extensible by anyone, and interoperable with the pydata/numfocus stack. 

This **advanced tutorial** explains how to write your own sktime estimator, e.g., forecaster, classifier, transformer, by using sktime’s extension templates and testing framework. A custom estimator can live in any local code base, and will be compatible with sktime pipelines, or scikit-learn.

[sktime]: https://sktime.net

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-workshop-pydata-london-2022/main?filepath=notebooks)

If you are unfamiliar with `sktime`, it is recommended to work through the **general sktime introduction tutorial** first:

:movie_camera: **[general sktime intro tutorial](https://github.com/sktime/sktime-tutorial-pydata-global-2021) from PyData Global 2021**\
:tv: [youtube video of sktime intro at PyData Global 2021](https://www.youtube.com/watch?v=ODspi8-uWgo)

:movie_camera: **Check out our [previous tutorial on hierarchical & probabilistic forecasting](https://github.com/sktime/sktime-tutorial-pydata-berlin-2022) from PyData Berlin 2022!**

## :bulb: Description

Writing sktime compatible estimators is meant to be easy.

This tutorial will explain: 
* sktime base class and estimator architecture 
* basic software design patterns used in extension
* how to use the extension templates
* how to validate your custom estimator
* testing in third party extensions and packages

Users can write sktime compatible estimators without a full developer setup, or any need to contribute the estimator to the sktime codebase. The custom estimator can be used with any tuning, pipeline, composition, or reduction functionality in sktime, and will be compatible with scikit-learn, too. This philosophy enables interoperability with third projects, proprietary code bases, or custom extension packages to sktime.

How this works technically: sktime ensures that all estimators of a certain type, e.g., forecasters, adhere to the same interface contracts, by using the base class and strategy patterns.

Separate to this user sided contract is the extension contract, which "extenders", users implementing their own estimators, have to satisfy. This is based on the template pattern which keeps boilerplate from the extension contract, and clearly defined "fill in your code" instructions in sktime´s extension templates.

The extension templates are python files with gaps that the extender is meant to fill in with the logic of a new estimator, with clear instructions in comments, and without any boilerplate. Finally, the sktime test suite provides few-line-validation for any custom estimator.

A full developer setup is typically not required to implement a custom estimator compatible with sktime.

:movie_camera: **Check out our [previous tutorial (probabilistic & hierarchical forecasting)](https://github.com/sktime/sktime-tutorial-pydata-berlin-2021) from PyData Berlin 2022!**\
:movie_camera: **Check out our [previous tutorial (general intro)](https://github.com/sktime/sktime-tutorial-pydata-global-2021) from PyData Global 2021!**\
:movie_camera: **Check out our [previous tutorial (general intro, legacy version)](https://github.com/sktime/sktime-tutorial-pydata-amsterdam-2020) from PyData Amsterdam 2020!**

## :rocket: How to get started

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages (`sktime`, `pytest`, `seaborn`, `jupyter`) in an environment, and open the notebooks with that environment. For detail instructions, see below. For troubleshooting, see sktime's more detailed [installation instructions].
* or, use python venv, and/or an editable install of this repo as a package. Instructions below.

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-workshop-pydata-london-2022/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.net/en/latest/installation.html

## :wave: How to contribute

If you're interested in contributing to sktime, you can find out more how to get involved [here](https://www.sktime.net/en/stable/get_involved.html).

Any contributions are welcome, not just code!

## Installation instructions in detail

### Cloning the repository

To clone the repository locally:

`git clone https://github.com/sktime/sktime-workshop-pydata-london-2022.git`


### Using conda env

#### option 1: installing requirements manually

1. Create a python virtual environment:  
`conda create -y -n pydata_sktime python=3.9`
2. Install required packages:  
`conda install -y -n pydata_sktime pip sktime pytest seaborn jupyter pmdarima`
3. Activate your environment:  
`conda activate pydata_sktime`
4. If using jupyter: make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`

#### option 2: installing repo as package

1. Create a python virtual environment:  
`conda create -y -n pydata_sktime python=3.9`
2. Make sure the environment has pip:  
`conda install -y -n pydata_sktime pip`
3. Activate your environment:  
`conda activate pydata_sktime`
4. Install the package in development mode:  
`pip install -e .`
5. If using jupyter: make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`

### Using python venv

#### option 1: installing requirements manually

1. Create a python virtual environment:  
`python -m venv .venv`
2. Activate your environment:  
`source .venv/bin/activate`
3. Install the requirements:  
`pip install sktime pytest seaborn jupyter pmdarima`
4. If using jupyter: make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`

#### option 2: installing repo as package

1. Create a python virtual environment:  
`python -m venv .venv`
2. Activate your environment:  
`source .venv/bin/activate`
3. Install the package in development mode:  
`pip install -e .`
4. If using jupyter: make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`
