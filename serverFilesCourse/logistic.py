import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def logit(p):
    return np.log(p / (1 - p))


def log_odds(x1, x2, beta_0, beta_1, beta_2):
    return beta_0 + beta_1 * x1 + beta_2 * x2


def odds(x1, x2, beta_0, beta_1, beta_2):
    return np.exp(log_odds(x1, x2, beta_0, beta_1, beta_2))


def prob_1(x1, x2, beta_0, beta_1, beta_2):
    return sigmoid(log_odds(x1, x2, beta_0, beta_1, beta_2))


def prob_0(x1, x2, beta_0, beta_1, beta_2):
    return 1 - prob_1(x1, x2, beta_0, beta_1, beta_2)


def classify(x1, x2, beta_0, beta_1, beta_2, alpha=0.5):
    prob = prob_1(x1, x2, beta_0, beta_1, beta_2)
    return np.where(prob > alpha, 1, 0).item()


def x2_bound(x1, beta_0, beta_1, beta_2):
    return (-beta_0 / beta_2) + (-beta_1 / beta_2) * x1


def x1_bound(x2, beta_0, beta_1, beta_2):
    return (-beta_0 / beta_1) + (-beta_2 / beta_1) * x2
