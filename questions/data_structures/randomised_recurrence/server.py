import random
import pandas as pd
import prairielearn as pl
import numpy
import sympy
from sympy.parsing.sympy_parser import parse_expr

def generate(data):

    # define sympy variables
    n = sympy.var('n')
    c = sympy.var('c')
    
    # question 1: T(0) = 1, T(n) = T(n - 1) + A1 * c
    A1 = random.randint(2, 12)
    # closed form
    fn1 = str(A1) + "* c * n + 1"

    # question 2: T(1)=B2, T(n) = A2 * T(n - 1) + B2 * n
    A2 = random.randint(2, 12)
    B2 = random.randint(2, 30)
    # closed form COURTESY OF WILLIAM ZHANG
    #fn2 = f"({-(a-1)}*n + {a}**(n+1) - {a}) * ({b}/{(a-1)**2})" # does this syntax work?
    fn2 = str(B2) + "*(" + str(A2) + "**(n+1)-" + str(A2) + "*(n+1)+n)/(" + str(A2) + "-1)**2"

    # question 3: T(1)=B3, T(n) = A3 * T(n / A3) + B3 * n
    A3 = random.randint(2, 12)
    B3 = random.randint(2, 30)
    # closed form
    fn3 = str(B3) + "*(n*log(n," + str(A3) + ") + n)"

    #parse and set answers
    exprrn1 = parse_expr(fn1, evaluate=False)
    exprrn2 = parse_expr(fn2, evaluate=False)
    exprrn3 = parse_expr(fn3, evaluate=False)
    data["correct_answers"]["recurrence1"] = pl.to_json(exprrn1)
    data["correct_answers"]["recurrence2"] = pl.to_json(exprrn2) 
    data["correct_answers"]["recurrence3"] = pl.to_json(exprrn3) 

    #params for rendering
    data["params"]["A1"] = A1
    data["params"]["A2"] = A2
    data["params"]["B2"] = B2
    data["params"]["A3"] = A3
    data["params"]["B3"] = B3
    data["params"]["n"] = sympy.latex(n)
    data["params"]["c"] = sympy.latex(c)


