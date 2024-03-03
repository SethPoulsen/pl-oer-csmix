import numpy as np
from utils import repr_x_pl
from utils import repr_y_pl
from utils import grade
from metrics import rmse
from inspect import getsource


def generate(data):

    # generate model parameters
    b0, b1, b2 = np.round(np.random.uniform(1, 10, 3), 0).astype(int)

    # generate data
    n = 12
    x1 = np.round(np.random.uniform(1, 2, n), 1)
    x2 = np.round(np.random.uniform(3, 4, n), 1)
    y = b0 + b1 * x1 + b2 * x2

    # fake estimated coefficients
    b0_hat, b1_hat, b2_hat = np.around([b0, b1, b2] + np.random.normal(size=3), 1)

    # calculate predictions
    y_pred = b0_hat + b1_hat * x1 + b2_hat * x2

    # calculate rmse
    test_rmse = rmse(y, y_pred)

    # set external parameters
    data["params"]["b0_hat"] = b0_hat
    data["params"]["b1_hat"] = b1_hat
    data["params"]["b2_hat"] = b2_hat
    data["params"]["x1_code"] = repr_x_pl(x1, name="x1")
    data["params"]["x2_code"] = repr_x_pl(x2, name="x2")
    data["params"]["y_code"] = repr_y_pl(y)
    data["params"]["rmse_code"] = getsource(rmse)

    # define answers
    data["correct_answers"]["test_rmse"] = test_rmse
