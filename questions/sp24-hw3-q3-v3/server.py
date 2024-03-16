import itertools
import random
import math

"""utilities"""
import pathlib
import sys

from cs411 import * # tada

# Goals:
# Upon generation, check for serial schedules
# If serial, re-generate.

# After this, check whether the solution entails downgrading or deadlock, and compare those to options
# to determine whether to re-generate.

""" prairielearn code """

transaction_lookup = {"repeatable read":repeatable_read_scheduler,"read committed":read_committed_scheduler,"Two Phase Locking":two_phase_locking_scheduler,"Two Phase Locking (2PL)":two_phase_locking_downgrade_scheduler, "Strict Two Phase Locking (S2PL)":repeatable_read_scheduler}

def check_deadlock(sol):
    return sol[-1].type == 8 # WAIT
    
def check_downgrading(sol): # Check the solution for downgrading. Do we Sk(A) after we Xk(A)?
    fulls = set({})
    for a in sol:
        if a.type == 4: # Xlock
            fulls.add(f"{a.thread}, {a.attribute}")
        elif a.type == 3: # Slock
            if (f"{a.thread}, {a.attribute}" in fulls):
                return True
    return False

def check_serial(sch): # Easy enough, just check if the numbers are all in contiguous blocks.
    # A schedule is a list of actions with thread, type, and attribute.
    ct = sch[0].thread
    uts = set({})
    for a in sch:
        if (a.thread != ct):
            uts.add(ct)
            ct = a.thread
            if (ct in uts):
                return False
    return True
    
def check_desirable(data, sch, sol):
    data["params"]["isSerial"] = False
    data["params"]["hasDeadlock"] = False
    data["params"]["hasDowngrading"] = False
    serial = check_serial(sch)
    deadlock = check_deadlock(sol)
    downgrading = check_downgrading(sol)
    if (serial != data["options"]["serial"]): 
        return False
    if (deadlock != data["options"]["deadlock"]):
        return False
    if (downgrading != data["options"]["downgrading"]):
        return False
    return True
    
def propose_schedule(data): # Generates a completely random schedule - no restrictions applied in this method.
    sched = generate_schedule(data["options"]["relation"],len(data["options"]["transactions"]),data["options"]["schedule_length"])
    sol = place_locks_and_wait(sched,[transaction_lookup[x] for x in data["options"]["transactions"]],data["options"]["relation"])
    return sched, sol
    
def generate(data):
    sched, sol = propose_schedule(data)
    while (not check_desirable(data, sched, sol)):
        sched, sol = propose_schedule(data)
    data["correct_answers"]["schedule"]=print_schedule(sol)
    data["params"]["schedule"]=print_schedule(sched)
    prot = data["options"]["transactions"][1]
    data["params"]["isolevels"]=" ".join([f"<li>The scheduler runs under the {prot} protocol.</li>"])
    data["params"]["relation"]=",".join(data["options"]["relation"])

def parse(data):
    try:
        data["submitted_answers"]["schedule"] = print_schedule(parse_schedule(data["raw_submitted_answers"]["schedule"]))
    except:
        data["format_errors"]["schedule"] = "Invalid syntax!"