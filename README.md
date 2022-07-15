# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/thalos12/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation

Currently the software can be installed via pip.

First, download the files form the repository:

```
git clone git@github.com:Thalos12/python-intermediate-inflammation.git
```

Then, install the software running the following in the `python-intermediate-inflammation` folder:

```
pip install .
```

## Basic usage

The software can be called from the command line as 

```
python inflammation-analysis.py <infiles> ARGS
```

where <infiles> can be one or more inflammation data files and ARGS stands for all optional arguments.
If no arguments are provided, apart from the fila names, the software will show plots of the overall trend of the inflammation in patients, one for each file.

To learn of all the optional arguments, just run the software without arguments or use the `-h` as follows:

```
python inflammation-analysis.py -h
```

## Contibuting

We welcome any contribution to improve the software.

## Getting help

Please open a new issue if you encounter problems running the software. However, please check that a similar one does not exist. If it does, please do not open a new issue.

# License

We adopt the GPL3.0. Please see the `LICENSE` file.