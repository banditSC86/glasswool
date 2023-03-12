import operator

import numpy as np
from numpy.random import default_rng

from glasswool.glasswool import glasswool


def test_glass_wool():
    # Test basic functionality with single maximum standard deviation
    numruns = 1000
    maxstd = 2.0
    rng = default_rng(12345)
    test_vals = rng.standard_normal(numruns)
    test_fun = glasswool

    # Check against numpy implementation
    def np_glass_wool(x_in, maxstd, side='both'):
        x = x_in.copy()
        op = {'lower': operator.neg, 'upper': operator.pos, 'both': operator.abs}[side]
        while 1:
            z = op(x - np.nanmean(x)) / np.nanstd(x)
            if np.nanmax(z) > maxstd:
                imax = np.nanargmax(z)
                x[imax] = np.nan
            else:
                break
        return x

    def check_vals(vals, good_vals):
        assert np.sum(np.isnan(vals)) == np.sum(np.isnan(good_vals))
        assert np.nanmin(vals) == np.nanmin(good_vals)
        assert np.nanmax(vals) == np.nanmax(good_vals)

    # Check default behavior
    good_vals = np_glass_wool(test_vals, maxstd)
    vals = test_fun(test_vals, maxstd)
    check_vals(vals, good_vals)
    vals = test_fun(test_vals, maxstd, side='both')
    check_vals(vals, good_vals)
    vals = test_fun(test_vals, (maxstd, maxstd), side='both')
    check_vals(vals, good_vals)

    # Check lower side
    vals = test_fun(test_vals, maxstd, side='lower')
    good_vals = np_glass_wool(test_vals, maxstd, side='lower')
    check_vals(vals, good_vals)

    # Check upper side
    vals = test_fun(test_vals, maxstd, side='upper')
    good_vals = np_glass_wool(test_vals, maxstd, side='upper')
    check_vals(vals, good_vals)

    # Handle a nan in the input
    test_vals[4] = np.nan
    vals = test_fun(test_vals, maxstd)
    good_vals = np_glass_wool(test_vals, maxstd)
    check_vals(vals, good_vals)
