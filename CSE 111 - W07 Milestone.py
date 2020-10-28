from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest
import math


def test_names():
    """Test the chemistry.get_name function."""
    # TODO: write this function.
    assert get_name("Ac") == "Actinium"
    assert get_name("Ag") == "Silver"
    assert get_name("Al") == "Aluminum"
    assert get_name("Am") == "Americium"
    assert get_name("Ar") == "Argon"
    assert get_name("As") == "Arsenic"
    assert get_name("At") == "Astatine"
    assert get_name("Au") == "Gold"
    assert get_name("B") == "Boron"
    assert get_name("Ba") == "Barium"
    assert get_name("Be") == "Beryllium"
    assert get_name("Bh") == "Bohrium"
    assert get_name("Bi") == "Bismuth"
    assert get_name("Bk") == "Berkelium"
    assert get_name("Br") == "Bromine"
    assert get_name("C") == "Carbon"
    assert get_name("Ca") == "Calcium"
    assert get_name("Cd") == "Cadmium"
    assert get_name("Ce") == "Cerium"
    assert get_name("Cf") == "Californium"
    assert get_name("Cl") == "Chlorine"
    assert get_name("Cm") == "Curium"
    assert get_name("Cn") == "Copernicium"
    assert get_name("Co") == "Cobalt"
    assert get_name("Cr") == "Chromium"
    assert get_name("Cs") == "Cesium"
    assert get_name("Cu") == "Copper"
    assert get_name("Db") == "Dubnium"
    assert get_name("Ds") == "Darmstadtium"
    assert get_name("Dy") == "Dysprosium"
    assert get_name("Er") == "Erbium"
    assert get_name("Es") == "Einsteinium"
    assert get_name("Eu") == "Europium"
    assert get_name("F") == "Fluorine"
    assert get_name("Fe") == "Iron"
    assert get_name("Fl") == "Flerovium"
    assert get_name("Fm") == "Fermium"
    assert get_name("Fr") == "Francium"
    assert get_name("Ga") == "Gallium"
    assert get_name("Gd") == "Gadolinium"
    assert get_name("Ge") == "Germanium"
    assert get_name("H") == "Hydrogen"
    assert get_name("He") == "Helium"
    assert get_name("Hf") == "Hafnium"
    assert get_name("Hg") == "Mercury"
    assert get_name("Ho") == "Holmium"
    assert get_name("Hs") == "Hassium"
    assert get_name("I") == "Iodine"
    assert get_name("In") == "Indium"
    assert get_name("Ir") == "Iridium"
    assert get_name("K") == "Potassium"
    assert get_name("Kr") == "Krypton"
    assert get_name("La") == "Lanthanum"
    assert get_name("Li") == "Lithium"
    assert get_name("Lr") == "Lawrencium"
    assert get_name("Lu") == "Lutetium"
    assert get_name("Lv") == "Livermorium"
    assert get_name("Mc") == "Moscovium"
    assert get_name("Md") == "Mendelevium"
    assert get_name("Mg") == "Magnesium"
    assert get_name("Mn") == "Manganese"
    assert get_name("Mo") == "Molybdenum"
    assert get_name("Mt") == "Meitnerium"
    assert get_name("N") == "Nitrogen"
    assert get_name("Na") == "Sodium"
    assert get_name("Nb") == "Niobium"
    assert get_name("Nd") == "Neodymium"
    assert get_name("Ne") == "Neon"
    assert get_name("Nh") == "Nihonium"
    assert get_name("Ni") == "Nickel"
    assert get_name("No") == "Nobelium"
    assert get_name("Np") == "Neptunium"
    assert get_name("O") == "Oxygen"
    assert get_name("Og") == "Oganesson"
    assert get_name("Os") == "Osmium"
    assert get_name("P") == "Phosphorus"
    assert get_name("Pa") == "Protactinium"
    assert get_name("Pb") == "Lead"
    assert get_name("Pd") == "Palladium"
    assert get_name("Pm") == "Promethium"
    assert get_name("Po") == "Polonium"
    assert get_name("Pr") == "Praseodymium"
    assert get_name("Pt") == "Platinum"
    assert get_name("Pu") == "Plutonium"
    assert get_name("Ra") == "Radium"
    assert get_name("Rb") == "Rubidium"
    assert get_name("Re") == "Rhenium"
    assert get_name("Rf") == "Rutherfordium"
    assert get_name("Rg") == "Roentgenium"
    assert get_name("Rh") == "Rhodium"
    assert get_name("Rn") == "Radon"
    assert get_name("Ru") == "Ruthenium"
    assert get_name("S") == "Sulfur"
    assert get_name("Sb") == "Antimony"
    assert get_name("Sc") == "Scandium"
    assert get_name("Se") == "Selenium"
    assert get_name("Sg") == "Seaborgium"
    assert get_name("Si") == "Silicon"
    assert get_name("Sm") == "Samarium"
    assert get_name("Sn") == "Tin"
    assert get_name("Sr") == "Strontium"
    assert get_name("Ta") == "Tantalum"
    assert get_name("Tb") == "Terbium"
    assert get_name("Tc") == "Technetium"
    assert get_name("Te") == "Tellurium"
    assert get_name("Th") == "Thorium"
    assert get_name("Ti") == "Titanium"
    assert get_name("Tl") == "Thallium"
    assert get_name("Tm") == "Thulium"
    assert get_name("Ts") == "Tennessine"
    assert get_name("U") == "Uranium"
    assert get_name("V") == "Vanadium"
    assert get_name("W") == "Tungsten"
    assert get_name("Xe") == "Xenon"
    assert get_name("Y") == "Yttrium"
    assert get_name("Yb") == "Ytterbium"
    assert get_name("Zn") == "Zinc"
    assert get_name("Zr") == "Zirconium"


def test_atomic_masses():
    """Test the chemistry.get_atomic_mass function."""
    # TODO: write this function.
    pass


def test_parse():
    """Test the chemistry.parse_formula function."""
    # TODO: write this function.
    pass


# def test_molar_mass():
#     """Test the chemistry.molar_mass function."""
#     assert molar_mass(parse_formula("H2O")) == approx(18.01528)
#     assert molar_mass(parse_formula("C6H6")) == approx(78.11184)
#     assert molar_mass(parse_formula("PO4H2(CH2)12CH3")) == approx(280.34072)


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["test_chemistry.py"])
