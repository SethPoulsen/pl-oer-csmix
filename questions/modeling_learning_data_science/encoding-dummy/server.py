import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import prairielearn as pl


def sim_categorical_student_df(shuffle=True):

    # generate a random categorical variable with one missing value
    c1 = np.array(["cs", "ds", "stat"], dtype="object")
    c2 = np.array(["undergraduate", "graduate"], dtype="object")

    # generate all possible combinations
    c1_mesh, c2_mesh = np.meshgrid(c1, c2)

    # reshape and stack to get a 2D array
    X = np.column_stack((c1_mesh.ravel(), c2_mesh.ravel()))

    # randomly sample n rows
    if shuffle:
        np.random.shuffle(X)

    return pd.DataFrame(X, columns=["major", "level"])


def generate(data):

    # generate example data
    df_example = sim_categorical_student_df()

    # create df for display
    df_display = df_example
    df_html = df_display.to_html(
        index=False, border=0, classes="table table-sm table-striped", justify="left"
    )

    # generate data and encode it
    X = sim_categorical_student_df()
    encoder = OneHotEncoder(drop="first")
    encoded = encoder.fit_transform(X).toarray().astype(int).__repr__()

    # set external parameters
    data["params"]["df"] = df_html
    data["params"]["X"] = encoded

    # define answers
    data["correct_answers"]["major-00"] = X.iloc[0, 0]
    data["correct_answers"]["major-01"] = X.iloc[1, 0]
    data["correct_answers"]["major-02"] = X.iloc[2, 0]
    data["correct_answers"]["major-03"] = X.iloc[3, 0]
    data["correct_answers"]["major-04"] = X.iloc[4, 0]
    data["correct_answers"]["major-05"] = X.iloc[5, 0]
    data["correct_answers"]["year-00"] = X.iloc[0, 1]
    data["correct_answers"]["year-01"] = X.iloc[1, 1]
    data["correct_answers"]["year-02"] = X.iloc[2, 1]
    data["correct_answers"]["year-03"] = X.iloc[3, 1]
    data["correct_answers"]["year-04"] = X.iloc[4, 1]
    data["correct_answers"]["year-05"] = X.iloc[5, 1]
