import importlib.resources

from ....base_classes import InterpolatedDataModel
from ....units import Q_
from .reference import CIEModel203


class Water(InterpolatedDataModel, CIEModel203):
    def __init__(self):
        with importlib.resources.path(
            str(__package__), "absorption_coefficient-water-cie203_2012.txt"
        ) as datafile:
            super().__init__(
                "water absorption coefficient", "1/cm", "wavelength", "um", datafile
            )

    # We are overriding the call operator so that we can name the argument
    # The CLI uses the inspect module to find all of the models we have implemented
    # and then get a list of their inputs. If we don't override this method, the
    # argument name will be "arg" because that is what InterpolatedDataModel declares.
    def __call__(self, wavelength: str | Q_):
        return super().__call__(wavelength)
