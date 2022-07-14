import numpy as np
import numpy.testing as npt


def test_normalvariate():
    from numpy.random import normal
    
    mu=15
    sigma=5
    N=10_000_000
    vals = normal(mu,sigma,N)
    
    npt.assert_approx_equal(mu, np.mean(vals), significant=3)
    npt.assert_approx_equal(sigma, np.std(vals), significant=3)
    