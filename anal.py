import matplotlib.pyplot as plt
import numpy as np

def make_position_histogram(filepath, cmap='bone'):
    """ Choosing proper number of bins is important, apparently"""
    # Read the full path from 'data/single_ball.dat'
    scores = read_pos(filepath)
    xx = [pos[0] for pos in scores]
    yy = [pos[1] for pos in scores]

    # Number of bins is defined here by the suqare of number of measurements
    xedges = np.linspace(min(xx), max(xx), np.sqrt(len(xx)))
    yedges = xedges

    # 
    H, xedges, yedges = np.histogram2d(xx, yy, bins=(xedges, yedges))

    # Scale the colors with vmax
    im = plt.imshow(H, vmin=0, vmax=10*H.mean(),\
				interpolation='nearest',
				origin='low',
				cmap=plt.get_cmap(cmap),
				extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    plt.show()

def read_pos(filepath):
    out = []
    with open(filepath) as fin:
	next(fin)
	for line in fin:
	    vals = line.split()
	    out.append([float(val) for val in vals])

    return out

if __name__ == '__main__':
    """ %run this.file.py """
    pass
