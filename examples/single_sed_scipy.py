"""Minimal single-component SciPy SED fit."""

import numpy as np

from fitters_for_pyGrater.fitters.single_ring_sed_scipy import SEDFitter
from pyGrater import Grain, Star
from pyGrater.density import two_power_law
from pyGrater.phase_functions import isotropic
from pyGrater.size_distributions import power_law_distribution

grain = Grain(composition="c_olivine_Fe_Poor")
star = Star(star_name="HD113766")
wavelengths = np.array([8.0, 10.0, 12.0])
observed_flux = np.array([1.0, 1.2, 1.1])
flux_error = np.full_like(observed_flux, 0.1)

params = {
    "r0": (0.5, 5.0),
    "h0": lambda p: 0.05 * p["r0"],
    "alphain": 10.0,
    "alphaout": -5.0,
    "beta": 1.0,
    "gamma": 1.0,
    "a_min": (1e-7, 1e-5),
    "a_max": 1e-3,
    "kappa": (3.0, 4.5),
    "A_norm": (1e20, 1e35),
    "N_sizes_integral": 100,
}

fitter = SEDFitter(
    grain, star, two_power_law, power_law_distribution, isotropic,
    wavelengths, observed_flux, flux_error, params)
fitter.fit()
