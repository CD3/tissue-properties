import importlib.resources

from ....base_classes import InterpolatedDataModel
from ....units import Q_
from .reference import MainsterModel


class RPE(InterpolatedDataModel, MainsterModel):
    def __init__(self):
        with importlib.resources.path(__package__, "mua-mainster-rpe.txt") as datafile:
            super().__init__(
                "absorption coefficient", "1/cm", "wavelength", "nm", datafile
            )

    # We are overriding the call operator so that we can name the argument
    # The CLI uses the inspect module to find all of the models we have implemented
    # and then get a list of their inputs. If we don't override this method, the
    # argument name will be "arg" because that is what InterpolatedDataModel declares.
    def __call__(self, wavelength: str | Q_):
        return super().__call__(wavelength)
