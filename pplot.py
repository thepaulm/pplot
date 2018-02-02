#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()


#
# Graphs
#
def pta(*args, color_rotate=True):
    '''pta = plot them all'''
    count = len(args)
    w = 20
    h = 4 * count
    fig = plt.figure(1, figsize=(w, h))
    for i, a in enumerate(args):
        ax = fig.add_subplot(count, 1, i+1)
        if color_rotate:
            for _ in range(i):
                ax.plot([], [])
        ax.plot(a)


def ptt(*args):
    '''ptt = plot them together'''
    w = 20
    h = 4
    fig = plt.figure(1, figsize=(w, h))
    ax = fig.add_subplot(1, 1, 1)
    for a in args:
        if not isinstance(a, list) and 1 in a.shape:
            a = a.squeeze()
        ax.plot(a)


def pts(x, y, p=None):
    '''pts = plot time series (with obs, preds)'''
    if len(x.shape) == 2 and 1 in x.shape:
        x = x.squeeze()
    if len(x.shape) == 1:
        x = np.array(x)
        y = np.append(np.array([np.nan for _ in range(len(x))]), y)
        if p is not None:
            p = np.append(np.array([np.nan for _ in range(len(x))]), p)
            ptt(x, y, p)
        else:
            ptt(x, y)
    else:
        plots = []
        nans = 0
        for tx, ty in zip(x, y):
            tx = np.append(np.array([np.nan for _ in range(nans)]), tx)
            ty = np.append(np.array([np.nan for _ in range(len(tx))]), ty)
            plots.append(tx)
            plots.append(ty)
            if p is not None:
                tp = np.append(np.array([np.nan for _ in range(len(tx))]), p[nans])
                plots.append(tp)
            nans += 1
        ptt(*plots)


#
# Cartesian / Euclidian
#
def rects(*rs):
    figsize = (10, 7)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(b=True, which='major')
    c = '#aaaaaa'
    for r in rs:
        xs = [p[0] for p in r]
        ys = [p[1] for p in r]
        ax.scatter(xs, ys)
        ax.plot([xs[0], xs[1]], [ys[0], ys[1]], '-', linewidth=1, color='r')
        ax.plot([xs[1], xs[3]], [ys[1], ys[3]], '-', linewidth=1, color=c)
        ax.plot([xs[3], xs[2]], [ys[3], ys[2]], '-', linewidth=1, color=c)
        ax.plot([xs[2], xs[0]], [ys[2], ys[0]], '-', linewidth=1, color=c)
