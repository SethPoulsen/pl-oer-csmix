import matplotlib.pyplot as plt
import matplotlib.cm as cm
import io
import random
import sys
sys.path.append('./tests')
import processingFigure as proc


def file(data):
    if data['filename']=='figure.png':
        figname = data['params']['name']
        filepath = 'tests/'+figname
        A, ymat = proc.permuteImage(filepath)

        fig, ax = plt.subplots()
        ax.imshow(ymat,cmap=cm.Greys_r)
        ax.axis('off')

        # Save the figure and return it as a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
 

    return buf


def generate(data):

    names_for_user = [
            {"name": "A", "description": "matrix operator to permute the rows and columns of the image ", "type": "2d numpy array"},
            {"name": "ymat","description": "permuted image", "type": "2d numpy array"}
     ]
    names_from_user = [
            {"name": "xmat","description": "unpermuted image", "type": "2d numpy array"}
     ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user

    fignumber1 = random.randint(1, 9)
    figname1 = 'n' + str(fignumber1) + '.png'



    data['params']['number'] = fignumber1
    data['params']['name'] = figname1

    return data
