"""Model-fitting implementations, organized by scope and algorithm."""

from fitters_for_pyGrater.fitters.multi_component_fov_sed_mcmc import (
    FOVAdditiveSEDMCMCFitter,
)
from fitters_for_pyGrater.fitters.multi_component_sed_dynesty import (
    AdditiveSEDNestedFitter,
)
from fitters_for_pyGrater.fitters.multi_component_sed_mcmc import (
    AdditiveSEDMCMCFitter,
)
from fitters_for_pyGrater.fitters.multi_component_sed_visibility_mcmc import (
    SEDVisibilityMCMCFitter,
)
from fitters_for_pyGrater.fitters.single_ring_multi_composition_sed_dynesty import (
    SingleRingMultiCompositionNestedFitter,
)
from fitters_for_pyGrater.fitters.single_ring_sed_correlated_flux_dynesty import (
    SEDCorrelatedFluxNestedFitter,
)
from fitters_for_pyGrater.fitters.single_ring_sed_dynesty import SEDNestedFitter
from fitters_for_pyGrater.fitters.single_ring_sed_interferometry_mcmc import (
    SEDInterferometryMCMCFitter,
)
from fitters_for_pyGrater.fitters.single_ring_sed_interferometry_scipy import (
    SEDInterferometryFitter,
)
from fitters_for_pyGrater.fitters.single_ring_sed_mcmc import SEDMCMCFitter
from fitters_for_pyGrater.fitters.single_ring_sed_scipy import SEDFitter

SingleRingSEDFitter = SEDFitter
SingleRingSEDMCMCFitter = SEDMCMCFitter
SingleRingSEDDynestyFitter = SEDNestedFitter
MultiComponentSEDMCMCFitter = AdditiveSEDMCMCFitter
MultiComponentSEDDynestyFitter = AdditiveSEDNestedFitter

__all__ = [
    "AdditiveSEDMCMCFitter",
    "AdditiveSEDNestedFitter",
    "FOVAdditiveSEDMCMCFitter",
    "MultiComponentSEDMCMCFitter",
    "MultiComponentSEDDynestyFitter",
    "SEDCorrelatedFluxNestedFitter",
    "SEDFitter",
    "SEDInterferometryFitter",
    "SEDInterferometryMCMCFitter",
    "SEDMCMCFitter",
    "SEDNestedFitter",
    "SEDVisibilityMCMCFitter",
    "SingleRingMultiCompositionNestedFitter",
    "SingleRingSEDFitter",
    "SingleRingSEDMCMCFitter",
    "SingleRingSEDDynestyFitter",
]
