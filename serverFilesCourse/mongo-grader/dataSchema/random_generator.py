from random import choice, randint
import string
import csv
import os


def file_to_list(filename) -> list:
    """read csv as list of lists"""
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, filename)
    f = open(abs_file_path)
    return list(csv.reader(f))

def get_random_firstNames(sample: int) -> any:
    """sample some names from firstname csv"""
    names = [x[0] for x in file_to_list("./data_lists/firstname.csv")]
    return [choice(names) for x in range(sample)]

def get_random_lastNames(sample: int) -> any:
    """sample some names from lastname csv"""
    names = [x[0] for x in file_to_list("./data_lists/lastname.csv")]
    return [choice(names) for x in range(sample)]

def get_random_fullNames(sample: int) -> any:
    fn = get_random_firstNames(sample)
    ln = get_random_lastNames(sample)
    names = []
    
    for idx, name in enumerate(fn):
        names.append(name + " " +ln[idx])

    return names

def get_random_medicine(sample: int) -> any:
    med = [x[0] for x in file_to_list("./data_lists/medicine.csv")]
    return [choice(med) for x in range(sample)]

def get_random_roomID(sample: int, digit=4) -> list:
    rids = []
    for _ in range(sample):
        rid = choice(string.ascii_uppercase)
        for i in range(digit):
            rid += str(randint(0, 9))
        rids.append(rid)
    return rids

def get_random_company(sample: int) -> any:
    med = [x[0] for x in file_to_list("./data_lists/company.csv")]
    return [choice(med) for x in range(sample)]

def get_random_country(sample: int) -> any:
    med = [x[0] for x in file_to_list("./data_lists/country.csv")]
    return [choice(med) for x in range(sample)]