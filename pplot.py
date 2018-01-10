#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()


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
        ax.plot(a)


def pts(x, y, p=None):
    '''pts = plot time series (with obs, preds)'''
    if len(x.shape) == 2 and x.shape[1] == 1:
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
