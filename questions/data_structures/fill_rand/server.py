import prairielearn as pl
import sympy
from sympy.parsing.sympy_parser import parse_expr
#import cv2
import numpy as np
import random, copy
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import io
from collections import deque


def getTwoNeighbors():
    choices = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    return random.sample(choices,k=2)

def getDirectionText(neigh):
    
    nx,ny = neigh

    # assemble words for directions
    directionLetters = ''
    directionWords = ''
    if ny == -1:
        directionLetters += 'N'
        directionWords += 'north'
    if ny == 1:
        directionLetters += 'S'
        directionWords += 'south'
    if nx == -1:
        directionLetters += 'W'
        directionWords += 'west'
    if nx == 1:
        directionLetters += 'E'
        directionWords += 'east'

    return directionWords, directionLetters

def generate(data):

    info = {}
    info['locations'] = getTwoNeighbors() # returns a list of 2 neighbor offsets, 0,0 is pixel
    info['center'] = (random.randint(2,5),random.randint(2,5))
    info['place'] = [getDirectionText(k)[0] for k in info['locations']]
    info['NWSE'] = [getDirectionText(k)[1] for k in info['locations']]

    data['params']['locations'] = info['locations']
    data['params']['center'] = info['center']
    data['params']['place'] = info['place']
    data['params']['NWSE'] = info['NWSE']

    sympy.var("x, y")

    x1 = f"x + " + str(info['locations'][0][0])
    x1 = parse_expr(x1, evaluate=False)
    data["correct_answers"]["x1"] = pl.to_json(x1)
    y1 = f"y + " + str(info['locations'][0][1])
    y1 = parse_expr(y1, evaluate=False)
    data["correct_answers"]["y1"] = pl.to_json(y1)

    x2 = f"x + " + str(info['locations'][1][0])
    x2 = parse_expr(x2, evaluate=False)
    data["correct_answers"]["x2"] = pl.to_json(x2)
    y2 = f"y + " + str(info['locations'][1][1])
    y2 = parse_expr(y2, evaluate=False)
    data["correct_answers"]["y2"] = pl.to_json(y2)

    grid = np.zeros((8,8), dtype=bool)
    d = deque()
    cx,cy = info['center']
    grid[cx,cy] = True
    d.append((cx,cy))
    while d:
        currx,curry = d.popleft()
        for nx,ny in info['locations']:
            nextx,nexty = currx+nx,curry+ny
            if nextx in range(8) and nexty in range(8) and not grid[nextx,nexty]:
                grid[nextx,nexty] = True
                d.append((nextx,nexty))

    transpgrid = grid.T
    grid = grid.tolist()
    data['params']['grid'] = pl.to_json(grid)

    '''
    none = []
    for k in range(8):
        curr = False
        for j in range(8):
           curr = curr or grid[j][k]
        none.append(not curr)
    '''

    none = [not any(transpgrid[k]) for k in range(8)]
    
    data['params']['none'] = pl.to_json(none)

    

def label(loc,let):
    plt.text(loc[0]-0.1, loc[1]-0.1, "Neighbor", ha="center", family='sans-serif', size=14)
    plt.text(loc[0]-0.1, loc[1]-0.3, let , ha="center", family='sans-serif', size=14)


def file(data):

    if data['filename']=='neigh.png':

        neighs = data['params']['locations'] # a list of neighbor offsets
        dirs = data['params']['NWSE']

        fig, ax = plt.subplots()
        
        patches = []

        for k,n in enumerate(neighs):

            n=[n[0],-1*n[1]]

            # add a fancy box
            fancybox = mpatches.FancyBboxPatch(
                np.array(n) - [0.5, 0.5], 0.8, 0.8,
                boxstyle=mpatches.BoxStyle("Round", pad=0.1),ec='k',fc='xkcd:light blue')
            patches.append(fancybox)
            label(np.array(n), dirs[k])

        
        fancybox = mpatches.FancyBboxPatch(
            np.array([0,0]) - [0.5, 0.5], 0.8, 0.8,
            boxstyle=mpatches.BoxStyle("Round", pad=0.1),ec='k',fc='xkcd:light violet')
        patches.append(fancybox)
        plt.text(0-0.1, 0-0.1, "Current", ha="center", family='sans-serif', size=14)
        plt.text(0-0.1, 0-0.3, "Pixel", ha="center", family='sans-serif', size=14)

        for p in patches:
            ax.add_patch(p)

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        buf = io.BytesIO()                           # make a bytes object (a buffer)
        plt.savefig(buf, format="png")               # save the figure data into the buffer
        return buf

    if data['filename']=='grid.png':
        cx,cy = data['params']['center']

        fig, ax = plt.subplots()

        patches = []

        for col in range(8):
            for row in range(8):
                # add a rectangle
                rect = mpatches.Rectangle(np.array([col,(-1)*row]) - [0.5, 0.5], 1, 1, ec="k",fc='none')
                patches.append(rect)
                cellnum = str(col) + str(row)
                plt.text(col, -1*(row-0.1), cellnum, ha="center", family='sans-serif', size=14,color='tab:gray')

        rect = mpatches.Rectangle(np.array([cx,(-1)*cy]) - [0.5, 0.5], 1, 1, ec="k", fc="xkcd:light orange")
        patches.append(rect)

        for p in patches:
            ax.add_patch(p)

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        buf = io.BytesIO()                           # make a bytes object (a buffer)
        plt.savefig(buf, format="png")               # save the figure data into the buffer
        return buf
                
                
