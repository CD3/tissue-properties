import importlib.resources

from ....base_classes import InterpolatedDataModel
from ....units import Q_
from .reference import CIEModel203


class DirectTransmission(InterpolatedDataModel, CIEModel203):
    def __init__(self):
        datafile = importlib.resources.path(
            __package__, "direct_transmission-human_eye-cie203_2012.txt"
        )
        super().__init__("direct ocular transmission", "", "wavelength", "um", datafile)

    # We are overriding the call operator so that we can name the argument
    # The CLI uses the inspect module to find all of the models we have implemented
    # and then get a list of their inputs. If we don't override this method, the
    # argument name will be "arg" because that is what InterpolatedDataModel declares.
    def __call__(self, wavelength: str | Q_):
        return super().__call__(wavelength)
