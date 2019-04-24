# coding: utf8
from __future__ import unicode_literals


ADJECTIVE_RULES = [
    ["ین", ""],
    ["\u200cترین", ""],
    ["ترین", ""],
    ["\u200cتر", ""],    
    ["تر", ""],
    ["\u200cای", ""],
#     ["ایی", "ا"],
#     ["ویی", "و"],
#     ["ی", ""],
#     ["مند", ""],
#     ["گین", ""],
#     ["مین", ""],
#     ["ناک", ""],
#     ["سار", ""],
#     ["\u200cوار", ""],
#    ["وار", ""]
]


NOUN_RULES = [
    ['ایان', 'ا'],
    ['ویان', 'و'],
    ['ایانی', 'ا'],
    ['ویانی', 'و'],
    ['گان', 'ه'],
    ['گانی', 'ه'],
    ['گان', ''],
    ['گانی', ''],
    ['ان', ''],
    ['انی', ''],
    ['ات', ''],
    ['ات', 'ه'],
    ['ات', 'ت'],
    ['اتی', ''],
    ['اتی', 'ه'],
    ['اتی', 'ت'],
    # ['ین', ''],
    # ['ینی', ''],
    # ['ون', ''],
    # ['ونی', ''],
    ['\u200cها', ''],
    ['ها', ''],
    ['\u200cهای', ''],
    ['های', ''],
    ['\u200cهایی', ''],
    ['هایی', ''],    
]


VERB_RULES = [
]


PUNCT_RULES = [
    ["“", "\""],
    ["”", "\""],
    ["\u2018", "'"],
    ["\u2019", "'"]
]
