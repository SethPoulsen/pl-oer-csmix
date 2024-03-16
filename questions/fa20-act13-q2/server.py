import itertools
import random
import math

"""utilities"""
import pathlib
import sys
from cs411 import * # tada

"""prairielearn code"""

# the letters we're using. needs to be known globally.
alphabet = "ABCDEF"

# the names of the params where we put the fds for students to find the closure of AND the answer-name of the string-inputs
# this is the same as alphabet now, but maybe not in the future

params = "ABCDEF"

def generate(data):
    
    # generate 3 one-to-one FD's
    fds = generate_fds(3,alphabet,1)
    # add 2 two-to-one FD.
    fds.update(generate_fds(2,alphabet,2))
    
    for a in params:
        data["params"][a]=random.choice(alphabet) # start off with one guaranteed random, this way we can't end up with empty set.
        for c in set(alphabet)-set(data["params"][a]):
            if (random.random()>0.66): # this is hacky! it can (rarely) generate duplicates. the student won't mind, though.
                data["params"][a]+=c
        data["params"][a] = "".join(sorted(data["params"][a])) # looks nicer
    
    
    # pretty string representation
    data["params"]["fds"] = print_fds(fds)
    
    # figure out the answers
    for x in params:
        data['correct_answers'][x] = ",".join(sorted(get_closure(fds,data["params"][x])))

def parse(data):
    for x in alphabet:
        data["submitted_answers"][x] = ",".join(sorted(data["raw_submitted_answers"][x].replace(" ","").split(",")))
