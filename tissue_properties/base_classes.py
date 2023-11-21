import numpy
import scipy
from .units import Q_
class ReferencedDataModel:
    reference = None

    def __init__(self):
        pass

    def get_reference(self):
        return self.reference

class InterpolatedDataModel:
    def __init__(self, aunit:str, vunit:str, filename=None):
        self.filename = filename
        self.interpolator = None
        self.argument_unit = aunit
        self.value_unit = vunit
        if self.filename is not None:
            self.load_data_from_file(self.filename)


    def load_data_from_file(self,filename):
        data = numpy.loadtxt(filename)
        self.interpolator = scipy.interpolate.interp1d(data[:,0],data[:,1])

    def __call__(self,arg:str | Q_):
        arg = Q_(arg)
        arg.ito(self.argument_unit)
        val = Q_( self.interpolator(arg.magnitude), self.value_unit)
        return val

