#general packages for data mgmt and concurrency
import os
from os import listdir
from os.path import isfile, join
import re
import json
import csv
import requests
from bs4 import BeautifulSoup, NavigableString
from tqdm import tqdm
from pprint import pprint

import multiprocessing as mp
import subprocess
import concurrent.futures


#data gathering and visualization


from urllib.parse import parse_qs, urlparse
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats


import wikipedia
from googlesearch import search
import googleapiclient.discovery


#text mgmt and NLP packages
from collections import Counter
from string import punctuation
import contractions
from difflib import SequenceMatcher

import gensim
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
stemmer = SnowballStemmer('english')

import spacy
from spacy.tokens import DocBin
from spacy.symbols import ORTH, LEMMA
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokenizer import Tokenizer
from spacy.util import compile_prefix_regex, compile_infix_regex, compile_suffix_regex
from spacy.tokens import Doc, Token, Span
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS




