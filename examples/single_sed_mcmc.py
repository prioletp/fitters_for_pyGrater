"""Single-component MCMC with a persistent backend and restart example."""

from pathlib import Path

from fitters_for_pyGrater.fitters.single_ring_sed_mcmc import SEDMCMCFitter

# Build the fitter exactly as in single_sed_scipy.py.
fitter = SEDMCMCFitter(...)
backend = Path("single_sed_backend.h5")

fitter.fit_then_mcmc(
    nwalkers=32,
    nsteps=2000,
    backend_path=backend,
    init="best_fit",
    best_fit_fwhm_frac=0.02,
)

# Restart from the last saved walker positions:
# fitter.restart_mcmc(
#     backend,
#     nsteps=1000,
#     backend_path=backend,
# )
