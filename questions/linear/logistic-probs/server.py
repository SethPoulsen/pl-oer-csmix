import numpy as np
import logistic


def generate(data):

    beta_low = -5
    beta_high = 5
    x_low = -1
    x_high = 1

    beta_0 = np.round(np.random.uniform(beta_low, beta_high), 2)
    beta_1 = np.round(np.random.uniform(beta_low, beta_high), 2)
    beta_2 = np.round(np.random.uniform(beta_low, beta_high), 2)
    x1a = np.round(np.random.uniform(x_low, x_high), 2)
    x2a = np.round(np.random.uniform(x_low, x_high), 2)
    x1b = np.round(np.random.uniform(x_low, x_high), 2)
    x2b = np.round(np.random.uniform(x_low, x_high), 2)
    x1c = np.round(np.random.uniform(x_low, x_high), 2)
    x2c = np.round(np.random.uniform(x_low, x_high), 2)
    x1d = np.round(np.random.uniform(x_low, x_high), 2)
    x2d = np.round(np.random.uniform(x_low, x_high), 2)
    alpha = np.round(np.random.uniform(0.51, 0.99), 2)

    parameters = {
        "beta_0": beta_0,
        "beta_1": beta_1,
        "beta_2": beta_2,
        "x1a": x1a,
        "x2a": x2a,
        "x1b": x1b,
        "x2b": x2b,
        "x1c": x1c,
        "x2c": x2c,
        "x1d": x1d,
        "x2d": x2d,
        "alpha": alpha,
    }

    answers = {
        "a": logistic.prob_1(x1a, x2a, beta_0, beta_1, beta_2),
        "b": logistic.prob_1(x1b, x2b, beta_0, beta_1, beta_2),
        "c": logistic.prob_0(x1c, x2c, beta_0, beta_1, beta_2),
        "d": logistic.prob_0(x1d, x2d, beta_0, beta_1, beta_2),
    }

    data["params"] = parameters
    data["correct_answers"] = answers
