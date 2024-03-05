import heapq
import numpy as np
import random
import pandas as pd
import prairielearn as pl


def generate(data):
    while True:
        arr = random.sample(range(100), 10)
        heapify = arr[:]
        heapq.heapify(heapify)
        insert = []
        for i in arr:
            heapq.heappush(insert, i)

        if heapify != insert:
            break

    x = pd.DataFrame(arr, columns=["key"])

    x.index = np.arange(x.shape[0]) + 1

    x = x.T

    data["params"]["input"] = pl.to_json(x)

    data["correct_answers"]["arr"] = export_vector(heapify)

    return data


def grade(data):
    inp = pl.from_json(data["params"]["input"])

    cor = pl.from_json(data["correct_answers"]["arr"])

    sub = pl.from_json(data["submitted_answers"].get("arr"))

    inp = np.squeeze(np.array(inp))

    cor = np.squeeze(np.array(cor))

    sub = np.squeeze(np.array(sub))

    data["partial_scores"]["arr"] = {}

    if sub is None:
        score = 0

    elif not np.all(np.sort(sub) == np.sort(inp)):
        score = 0

    # Valid sumbission
    else:
        # Correct answer
        if np.all(sub == cor):
            score = 4

        elif is_heap(sub):
            if is_sorted(sub):
                score = 1

            else:
                score = 2

        else:
            score = 0

    data["partial_scores"]["arr"] = {"score": score / 4}
    data["score"] = score / 4

    return data


def is_heap(h):
    x, y = list(h), list(h)

    heapq.heapify(y)

    x, y = np.array(x), np.array(y)

    return np.all(x == y)


def is_sorted(h):
    return np.all(h == np.sort(h))


def export_vector(x):
    return pl.to_json(np.atleast_2d(x))
