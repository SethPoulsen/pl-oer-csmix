import random
import numpy as np
from scipy.stats import norm


def generate(data):
    # define distribution
    mean = random.randint(1, 8)
    sd = random.choice([1.5, 2.1, 2.5, 3.2, 3.5])
    n = norm(loc=mean, scale=sd)

    # create random probabilities that will define the answer
    lt_prob = random.uniform(0.001, 0.499)
    rt_prob = random.uniform(0.501, 0.999)
    a_prob = random.uniform(0.001, 0.499)
    b_prob = random.uniform(0.501, 0.999)

    # reverse engineer "cutoffs" from "answer" probabilities
    lt = np.round(n.ppf(lt_prob), 2)
    rt = np.round(n.ppf(rt_prob), 2)
    a = np.round(n.ppf(a_prob), 2)
    b = np.round(n.ppf(b_prob), 2)

    # calculate answer probabilities
    p1 = n.cdf(lt)
    p2 = 1 - n.cdf(rt)
    p3 = n.cdf(b) - n.cdf(a)

    # set external parameters
    data["params"]["mean"] = mean
    data["params"]["sd"] = sd
    data["params"]["lt"] = lt
    data["params"]["rt"] = rt
    data["params"]["a"] = a
    data["params"]["b"] = b

    # define answers
    data["correct_answers"]["p1"] = p1
    data["correct_answers"]["p2"] = p2
    data["correct_answers"]["p3"] = p3


def grade(data):
    data["feedback"]["show_full_answer"] = False
    if data["score"] == 1:
        data["feedback"]["show_full_answer"] = True
