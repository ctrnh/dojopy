import os
import shutil
import subprocess
import sys

from os.path import dirname, abspath, join


# from jill.install import install_julia

# script_dir = os.path.dirname(os.path.realpath(__file__))
#
#
# def _find_julia():
#     # TODO: this should probably fallback to query jill
#     return shutil.which("julia")
#
#
def install(*, confirm=False):
    """
    Install Julia (if required) and Julia packages required for diffeqpy.
    """
    print("install ###############################################")
    result = subprocess.run(
        ["echo", "Hello, World!"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    print(result.stdout)

    result = subprocess.run(
        ["sudo", "bash", join(dirname(abspath(__file__)), "install_dojopy.bash")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    print(result.stdout)


#     julia = _find_julia()
#     if not julia:
#         print("No Julia version found. Installing Julia.")
#         install_julia(confirm=confirm)
#         julia = _find_julia()
#         if not julia:
#             raise RuntimeError(
#                 "Julia installed with jill but `julia` binary cannot be found in the path"
#             )
#     env = os.environ.copy()
#     env["PYTHON"] = sys.executable
#     subprocess.check_call([julia, os.path.join(script_dir, "install.jl")], env=env)
#
#
# def _ensure_installed(*kwargs):
#     if not _find_julia():
#         # TODO: this should probably ensure that packages are installed too
#         install(*kwargs)
