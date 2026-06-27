"""Minimal nested-sampling template."""

from fitters_for_pyGrater.fitters.single_ring_sed_dynesty import (
    SEDNestedFitter,
)

fitter = SEDNestedFitter(...)
RUN_MODE = "resume"  # "fresh", "resume", or "load"
checkpoint = "single_sed_nested.checkpoint"
results = "single_sed_nested_results.npz"

if RUN_MODE == "load":
    fitter.load_results(results)
elif RUN_MODE == "resume":
    fitter.resume_backend_nested(
        checkpoint, npoints=300, dlogz=0.1, checkpoint_every=300)
    fitter.save_results(results)
else:
    fitter.run(
        npoints=300, dlogz=0.1, checkpoint_file=checkpoint,
        checkpoint_every=300)
    fitter.save_results(results)

fitter.plot_nested_diagnostics(
    "single_sed_nested_plots", prefix="single_sed_nested")
fitter.save_results("single_sed_nested_results.npz")
