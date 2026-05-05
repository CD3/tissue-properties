# A python library for calculating/looking up various tissue properties for laser bioeffect calculations

To simulate the exposure of tissue (skin or retina) to laser radiation, several properties characterizing the thermo-optical response of the tissue are needed.
These include absorption coefficients, transmission coefficients, conductivity, density, specific heat, etc. This library is a collection of tissue property data
sets that have been reported in the literature.

# Installing

Install with pip (or your favorite virtual environment manager)

```bash
pip install tissue-properties
```

# Usage

All models accept wavelength as a `pint` `Quantity` object or a plain string such as
`"532 nm"`. Results are always `Quantity` objects with appropriate units. Every model
also exposes a `.get_reference()` method that returns the source paper as a BibTeX
string.

```python
from tissue_properties.units import Q_
```

## Absorption Coefficient

### Mainster (1970) — tabulated, 400–1361 nm

Data extracted from Figure 3 of Mainster et al., JOSA 60(2), 1970.

```python
from tissue_properties.optical.absorption_coefficient import mainster

rpe = mainster.RPE()
choroid = mainster.Choroid()

print("# wavelength (nm)  RPE (1/cm)  Choroid (1/cm)")
for wavelength in range(400, 1405, 5):
    l = Q_(wavelength, "nm")
    print(l, rpe(l), choroid(l))

print(rpe.get_reference())
```

### Schulmeister (2017) — analytic formulas

```python
from tissue_properties.optical.absorption_coefficient import schulmeister

rpe = schulmeister.RPE()                     # melanin power-law
choroid = schulmeister.Choroid()             # melanin + blood composite
henles = schulmeister.HenlesFiberLayer()     # macular pigment

wavelength = Q_(532, "nm")
print(rpe(wavelength))
print(choroid(wavelength))
print(henles(wavelength))
```

## Ocular Transmission

### CIE 203 (2012) — tabulated

```python
from tissue_properties.optical.ocular_transmission import cie203

total = cie203.TotalTransmission()
direct = cie203.DirectTransmission()

wavelength = Q_(532, "nm")
print(total(wavelength))             # dimensionless fraction
print(total(wavelength).to("percent"))
print(direct(wavelength))
```

### Mainster (1970) — tabulated, 400–1400 nm

```python
from tissue_properties.optical.ocular_transmission import mainster

transmission = mainster.Transmission()

print(transmission("532 nm"))
print(transmission("1064 nm"))
```

### Schulmeister (2017) — effective transmission

Accounts for scattered light reaching the retina for finite beam spot sizes.
As `spot_size → ∞` the result approaches total transmission; as `spot_size → 0`
it approaches direct transmission.

```python
from tissue_properties.optical.ocular_transmission import schulmeister

T_eff = schulmeister.EffectiveTransmission()

wavelength = Q_(532, "nm")
print(T_eff(wavelength, Q_(0, "um")))       # zero spot → ~direct transmission
print(T_eff(wavelength, Q_(200, "um")))     # typical focused beam
print(T_eff(wavelength, Q_(10000, "um")))   # large spot → ~total transmission
```

## Refractive Index

### Navarro (1985) — analytic Herzberger dispersion

Four ocular media components from Navarro, Santamaría & Bescós, JOSA A 2(8), 1985.

```python
from tissue_properties.optical.refractive_index import navarro

cornea = navarro.Cornea()
aqueous = navarro.Aqueous()
lens = navarro.Lens()
vitreous = navarro.Vitreous()

wavelength = Q_(550, "nm")
print(cornea(wavelength))
print(aqueous(wavelength))
print(lens(wavelength))
print(vitreous(wavelength))
```

### Vincelette (2008) — Sellmeier formula for reduced eye

Validated for the 1150–1350 nm near-infrared region (Vincelette et al., JBO 13, 2008).

```python
from tissue_properties.optical.refractive_index import vincelette

reduced_eye = vincelette.ReducedEye()

print(reduced_eye("1064 nm"))
print(reduced_eye("1200 nm"))
```
