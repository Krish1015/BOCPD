import numpy as np
import scipy.stats as ss


def const_prior(t, p: float = 0.25):
    """
    Constant prior for every datapoint
    Arguments:
        p - probability of event
    """
    return np.log(p)