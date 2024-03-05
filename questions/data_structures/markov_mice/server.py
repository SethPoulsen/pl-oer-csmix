import prairielearn as pl
import sympy
from sympy.parsing.sympy_parser import parse_expr
#import cv2
import numpy as np
import random, copy
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.path import Path
        
import io
from collections import deque



def generate(data):

    refRooms = ['A','B','C','D']
    rooms = np.arange(4)
    e = np.identity(4)
    np.random.shuffle(e)
    rooms = np.matmul(e,rooms)

    doors = np.zeros((4,4))
    doors[0,1] = doors[1,0] = random.randint(0,2)
    doors[0,2] = doors[2,0] = random.randint(1,2)
    doors[1,2] = doors[2,1] = random.randint(0,1)
    doors[1,3] = doors[3,1] = random.randint(1,2)
    doors[2,3] = doors[3,2] = random.randint(1,2)

    p = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            p[i,j] = doors[i,j]/np.sum(doors[i])

    p = np.matmul(np.matmul(e,p),e.transpose())

    rooms = [int(x) for x in rooms]
    roomName = dict(zip(rooms,refRooms))

    # Answer to each matrix entry converted to JSON
    data['correct_answers']['trans'] = pl.to_json(p)
    data['params']['roomNames'] = pl.to_json(roomName)
    data['params']['doors'] = pl.to_json(doors)

    [startroom,tworoom] = random.sample(list(rooms),2)
    data['params']['startroom'] = refRooms[startroom]
    data['params']['tworoom'] = refRooms[tworoom]
    tot = 0
    for k in range(4):
        tot += p[startroom,k]*p[k,tworoom]
    data['correct_answers']['two'] = p[startroom,tworoom] + tot


def buildCodes(doors):
    codes = [Path.MOVETO,
            Path.LINETO]
    if doors == 0:
        for x in range(3):
            codes.append(Path.LINETO)
    if doors == 1:
        codes.append(Path.LINETO)
        codes.append(Path.MOVETO)
        codes.append(Path.LINETO)
    if doors == 2:
        codes.append(Path.MOVETO)
        codes.append(Path.LINETO)
        codes.append(Path.MOVETO)
  
    codes.append(Path.LINETO)
    return codes

def file(data):

    if data['filename']=='house.png':

        doors = pl.from_json(data['params']['doors'])
        names = pl.from_json(data['params']['roomNames'])


        verts = [  0.,  0.25,  0.75, 1.25, 1.75,  2. ]

        pat = []
        house = patches.Rectangle(np.array([0,0]), 4, 4, ec="k",fc='none', lw=2)
        pat.append(house)

        verts01 = [(y,3) for y in verts]
        verts02 = [(y+2,3) for y in verts]
        verts12 = [(2,y+1) for y in verts]
        verts13 = [(y,1) for y in verts]
        verts23 = [(y+2,1) for y in verts]
        allverts = [verts01,verts02,verts12,verts13,verts23]
        codes01 = buildCodes(doors[0,1])
        codes02 = buildCodes(doors[0,2])
        codes12 = buildCodes(doors[2,1])
        codes13 = buildCodes(doors[3,1])
        codes23 = buildCodes(doors[2,3])
        allcodes = [codes01,codes02,codes12,codes13,codes23]

        for k in range(5):
            pat.append(patches.PathPatch(Path(allverts[k], allcodes[k]),lw=2))

        fig = plt.figure()
        ax = fig.add_subplot()
        for p in pat:
            ax.add_patch(p)

        plt.text(2, 3.4, names['0'], ha="center", family='sans-serif', size=14,color='tab:gray')
        plt.text(1, 2, names['1'], ha="center", family='sans-serif', size=14,color='tab:gray')
        plt.text(3, 2, names['2'], ha="center", family='sans-serif', size=14,color='tab:gray')
        plt.text(2, 0.4, names['3'], ha="center", family='sans-serif', size=14,color='tab:gray')
        plt.axis('equal') 
        plt.axis('off')
        plt.tight_layout()


        buf = io.BytesIO()                           # make a bytes object (a buffer)
        plt.savefig(buf, format="png")               # save the figure data into the buffer
        return buf

                
