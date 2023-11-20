from ....data_models import InterpolatedDataModel
from .reference import MainsterModel
import importlib.resources


class RPE(InterpolatedDataModel,MainsterModel):
    def __init__(self):
        datafile = importlib.resources.path(__package__,"mua-mainster-rpe.txt")
        super().__init__("nm","1/cm",datafile)
