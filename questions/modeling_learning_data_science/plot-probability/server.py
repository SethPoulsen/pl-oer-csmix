import io
import prairielearn as pl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from matplotlib import use

use("Agg")

# data
CLUSTER_STD = 10
N_SAMPLES = 100
N_FEATURES = 3
N_CLUSTERS = 3

# tree
MAX_DEPTH = 2

# randomness
SEED = np.random.randint(1000)


def generate(data):

    X, y = make_blobs(
        n_samples=N_SAMPLES,
        n_features=N_FEATURES,
        cluster_std=CLUSTER_STD,
        centers=N_CLUSTERS,
        random_state=SEED,
    )
    X_new, _ = make_blobs(
        n_samples=1,
        n_features=N_FEATURES,
        cluster_std=CLUSTER_STD,
        centers=N_CLUSTERS,
    )
    X_new = np.round(X_new, 2)

    dt = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=1)
    dt.fit(X, y)
    probabilities = dt.predict_proba(X_new)

    data["params"]["X_new"] = repr([X_new[0].tolist()])
    data["correct_answers"]["p0"] = float(probabilities[0, 0])
    data["correct_answers"]["p1"] = float(probabilities[0, 1])
    data["correct_answers"]["p2"] = float(probabilities[0, 2])


def file(data):

    X, y = make_blobs(
        n_samples=N_SAMPLES,
        n_features=N_FEATURES,
        cluster_std=CLUSTER_STD,
        centers=N_CLUSTERS,
        random_state=SEED,
    )

    dt = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=1)
    dt.fit(X, y)

    if data["filename"] == "fig.png":
        buf = io.BytesIO()
        plot_tree(dt, filled=True)
        plt.savefig(buf, format="png")
        return buf
