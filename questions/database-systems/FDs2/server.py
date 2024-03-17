import itertools
import random
import math

"""utilities"""
import pathlib
import sys
from cs411 import * # tada
""" prairielearn code """

alphabet = "ABCDEF"

def generate(data):
    # generate 3 one-to-one FD's
    fds = generate_fds(3,alphabet,1)
    # add 2 two-to-one FD.
    fds.update(generate_fds(2,alphabet,2)) # uncomment to make problem harder.
    
    prettyprint = lambda x: (x[0] if len(x)==1 else "("+",".join(map(str,x)) +")")
    
    # pretty string representation
    data["params"]["fds"] = " ".join([prettyprint(x)+"->"+prettyprint(fds[x]) for x in fds])
    
    data["correct_answers"]["candidates"] = ",".join(sorted(get_candidate_keys(alphabet,fds)))

def parse(data):
    data["submitted_answers"]["candidates"] = ",".join(sorted(["".join(sorted(x)) for x in data["raw_submitted_answers"]["candidates"].replace(" ","").split(",")]))