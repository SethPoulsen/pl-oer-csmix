import numpy as np
import pandas as pd


def knn_class_prob_one(x, y, x_new, k=5):
    neighbors = y[np.argsort(np.abs(x - x_new))[0:k]]
    p_class_1 = np.mean(neighbors)
    p_class_0 = 1 - p_class_1
    return p_class_0, p_class_1


def generate(data):
    # generate data
    n = 15
    x = np.arange(15) + 1
    y = np.random.randint(0, 2, n)
    df = pd.DataFrame({"x": x, "y": y})
    x_new = np.round(np.random.uniform(5, 13, 1), 2)[0]

    # make html table
    df_html = df.to_html(index=False, border=0, classes="table table-striped table-sm", justify="left")

    # get probs
    p0, p1 = knn_class_prob_one(x, y, x_new, k=5)

    # set external parameters
    data["params"]["df_html"] = df_html
    data["params"]["x_new"] = x_new

    # define answers
    data["correct_answers"]["p0"] = p0
    data["correct_answers"]["p1"] = p1
