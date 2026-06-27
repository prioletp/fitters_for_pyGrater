"""Optimized fitting tools for pyGrater models."""

from importlib import import_module


_PUBLIC_CLASSES = {
    "AdditiveSEDMCMCFitter": (
        "fitters_for_pyGrater.fitters.multi_component_sed_mcmc"),
    "AdditiveSEDNestedFitter": (
        "fitters_for_pyGrater.fitters.multi_component_sed_dynesty"),
    "FOVAdditiveSEDMCMCFitter": (
        "fitters_for_pyGrater.fitters.multi_component_fov_sed_mcmc"),
    "MultiComponentSEDMCMCFitter": (
        "fitters_for_pyGrater.fitters"),
    "MultiComponentSEDDynestyFitter": (
        "fitters_for_pyGrater.fitters"),
    "SEDCorrelatedFluxNestedFitter": (
        "fitters_for_pyGrater.fitters.single_ring_sed_correlated_flux_dynesty"),
    "SEDFitter": "fitters_for_pyGrater.fitters.single_ring_sed_scipy",
    "SEDInterferometryFitter": (
        "fitters_for_pyGrater.fitters.single_ring_sed_interferometry_scipy"),
    "SEDInterferometryMCMCFitter": (
        "fitters_for_pyGrater.fitters.single_ring_sed_interferometry_mcmc"),
    "SEDMCMCFitter": "fitters_for_pyGrater.fitters.single_ring_sed_mcmc",
    "SEDNestedFitter": "fitters_for_pyGrater.fitters.single_ring_sed_dynesty",
    "SEDVisibilityMCMCFitter": (
        "fitters_for_pyGrater.fitters.multi_component_sed_visibility_mcmc"),
    "SingleRingMultiCompositionNestedFitter": (
        "fitters_for_pyGrater.fitters.single_ring_multi_composition_sed_dynesty"),
    "SingleRingSEDFitter": "fitters_for_pyGrater.fitters",
    "SingleRingSEDMCMCFitter": "fitters_for_pyGrater.fitters",
    "SingleRingSEDDynestyFitter": "fitters_for_pyGrater.fitters",
}

__all__ = list(_PUBLIC_CLASSES)


def __getattr__(name):
    """Import a public fitter only when it is first requested."""
    try:
        module_name = _PUBLIC_CLASSES[name]
    except KeyError as exc:
        raise AttributeError(name) from exc
    value = getattr(import_module(module_name), name)
    globals()[name] = value
    return value
