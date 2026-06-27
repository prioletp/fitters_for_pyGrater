"""Template for multiple rings, compositions, or both."""

from fitters_for_pyGrater.fitters.multi_component_sed_mcmc import (
    AdditiveSEDMCMCFitter,
)

components = {
    "ring1_olivine": grain_olivine,
    "ring1_carbon": grain_carbon,
    "ring2_olivine": grain_olivine,
    "ring2_carbon": grain_carbon,
}

# Geometry can be shared by group while each composition keeps its own A_norm.
fitter = AdditiveSEDMCMCFitter(
    components=components,
    star=star,
    density_distribution=two_power_law,
    size_distribution=power_law_distribution,
    scattering_phase_function=isotropic,
    wavelengths=wavelengths,
    fluxes=observed_flux,
    fluxes_err=flux_error,
    params_by_component=params_by_component,
    component_groups={
        "ring1_olivine": "ring1",
        "ring1_carbon": "ring1",
        "ring2_olivine": "ring2",
        "ring2_carbon": "ring2",
    },
    group_shared_parameter_names={
        "ring1": ring1_shared_parameters,
        "ring2": ring2_shared_parameters,
    },
)
