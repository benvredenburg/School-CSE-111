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
    assert get_atomic_mass("Ac") == approx(227)
    assert get_atomic_mass("Ag") == approx(107.8682)
    assert get_atomic_mass("Al") == approx(26.9815386)
    assert get_atomic_mass("Am") == approx(243)
    assert get_atomic_mass("Ar") == approx(39.948)
    assert get_atomic_mass("As") == approx(74.9216)
    assert get_atomic_mass("At") == approx(210)
    assert get_atomic_mass("Au") == approx(196.966569)
    assert get_atomic_mass("B") == approx(10.811)
    assert get_atomic_mass("Ba") == approx(137.327)
    assert get_atomic_mass("Be") == approx(9.012182)
    assert get_atomic_mass("Bh") == approx(272)
    assert get_atomic_mass("Bi") == approx(208.9804)
    assert get_atomic_mass("Bk") == approx(247)
    assert get_atomic_mass("Br") == approx(79.904)
    assert get_atomic_mass("C") == approx(12.0107)
    assert get_atomic_mass("Ca") == approx(40.078)
    assert get_atomic_mass("Cd") == approx(112.411)
    assert get_atomic_mass("Ce") == approx(140.116)
    assert get_atomic_mass("Cf") == approx(251)
    assert get_atomic_mass("Cl") == approx(35.453)
    assert get_atomic_mass("Cm") == approx(247)
    assert get_atomic_mass("Cn") == approx(285)
    assert get_atomic_mass("Co") == approx(58.933195)
    assert get_atomic_mass("Cr") == approx(51.9961)
    assert get_atomic_mass("Cs") == approx(132.9054519)
    assert get_atomic_mass("Cu") == approx(63.546)
    assert get_atomic_mass("Db") == approx(268)
    assert get_atomic_mass("Ds") == approx(281)
    assert get_atomic_mass("Dy") == approx(162.5)
    assert get_atomic_mass("Er") == approx(167.259)
    assert get_atomic_mass("Es") == approx(252)
    assert get_atomic_mass("Eu") == approx(151.964)
    assert get_atomic_mass("F") == approx(18.9984032)
    assert get_atomic_mass("Fe") == approx(55.845)
    assert get_atomic_mass("Fl") == approx(289)
    assert get_atomic_mass("Fm") == approx(257)
    assert get_atomic_mass("Fr") == approx(223)
    assert get_atomic_mass("Ga") == approx(69.723)
    assert get_atomic_mass("Gd") == approx(157.25)
    assert get_atomic_mass("Ge") == approx(72.64)
    assert get_atomic_mass("H") == approx(1.00794)
    assert get_atomic_mass("He") == approx(4.002602)
    assert get_atomic_mass("Hf") == approx(178.49)
    assert get_atomic_mass("Hg") == approx(200.59)
    assert get_atomic_mass("Ho") == approx(164.93032)
    assert get_atomic_mass("Hs") == approx(270)
    assert get_atomic_mass("I") == approx(126.90447)
    assert get_atomic_mass("In") == approx(114.818)
    assert get_atomic_mass("Ir") == approx(192.217)
    assert get_atomic_mass("K") == approx(39.0983)
    assert get_atomic_mass("Kr") == approx(83.798)
    assert get_atomic_mass("La") == approx(138.90547)
    assert get_atomic_mass("Li") == approx(6.941)
    assert get_atomic_mass("Lr") == approx(262)
    assert get_atomic_mass("Lu") == approx(174.9668)
    assert get_atomic_mass("Lv") == approx(293)
    assert get_atomic_mass("Mc") == approx(288)
    assert get_atomic_mass("Md") == approx(258)
    assert get_atomic_mass("Mg") == approx(24.305)
    assert get_atomic_mass("Mn") == approx(54.938045)
    assert get_atomic_mass("Mo") == approx(95.96)
    assert get_atomic_mass("Mt") == approx(276)
    assert get_atomic_mass("N") == approx(14.0067)
    assert get_atomic_mass("Na") == approx(22.98976928)
    assert get_atomic_mass("Nb") == approx(92.90638)
    assert get_atomic_mass("Nd") == approx(144.242)
    assert get_atomic_mass("Ne") == approx(20.1797)
    assert get_atomic_mass("Nh") == approx(284)
    assert get_atomic_mass("Ni") == approx(58.6934)
    assert get_atomic_mass("No") == approx(259)
    assert get_atomic_mass("Np") == approx(237)
    assert get_atomic_mass("O") == approx(15.9994)
    assert get_atomic_mass("Og") == approx(294)
    assert get_atomic_mass("Os") == approx(190.23)
    assert get_atomic_mass("P") == approx(30.973762)
    assert get_atomic_mass("Pa") == approx(231.03588)
    assert get_atomic_mass("Pb") == approx(207.2)
    assert get_atomic_mass("Pd") == approx(106.42)
    assert get_atomic_mass("Pm") == approx(145)
    assert get_atomic_mass("Po") == approx(209)
    assert get_atomic_mass("Pr") == approx(140.90765)
    assert get_atomic_mass("Pt") == approx(195.084)
    assert get_atomic_mass("Pu") == approx(244)
    assert get_atomic_mass("Ra") == approx(226)
    assert get_atomic_mass("Rb") == approx(85.4678)
    assert get_atomic_mass("Re") == approx(186.207)
    assert get_atomic_mass("Rf") == approx(267)
    assert get_atomic_mass("Rg") == approx(280)
    assert get_atomic_mass("Rh") == approx(102.9055)
    assert get_atomic_mass("Rn") == approx(222)
    assert get_atomic_mass("Ru") == approx(101.07)
    assert get_atomic_mass("S") == approx(32.065)
    assert get_atomic_mass("Sb") == approx(121.76)
    assert get_atomic_mass("Sc") == approx(44.955912)
    assert get_atomic_mass("Se") == approx(78.96)
    assert get_atomic_mass("Sg") == approx(271)
    assert get_atomic_mass("Si") == approx(28.0855)
    assert get_atomic_mass("Sm") == approx(150.36)
    assert get_atomic_mass("Sn") == approx(118.71)
    assert get_atomic_mass("Sr") == approx(87.62)
    assert get_atomic_mass("Ta") == approx(180.94788)
    assert get_atomic_mass("Tb") == approx(158.92535)
    assert get_atomic_mass("Tc") == approx(98)
    assert get_atomic_mass("Te") == approx(127.6)
    assert get_atomic_mass("Th") == approx(232.03806)
    assert get_atomic_mass("Ti") == approx(47.867)
    assert get_atomic_mass("Tl") == approx(204.3833)
    assert get_atomic_mass("Tm") == approx(168.93421)
    assert get_atomic_mass("Ts") == approx(294)
    assert get_atomic_mass("U") == approx(238.02891)
    assert get_atomic_mass("V") == approx(50.9415)
    assert get_atomic_mass("W") == approx(183.84)
    assert get_atomic_mass("Xe") == approx(131.293)
    assert get_atomic_mass("Y") == approx(88.90585)
    assert get_atomic_mass("Yb") == approx(173.054)
    assert get_atomic_mass("Zn") == approx(65.38)
    assert get_atomic_mass("Zr") == approx(91.224)


def test_parse():
    """Test the chemistry.parse_formula function."""
    # TODO: write this function.
    assert parse_formula('H2O') == {'H': 2, 'O': 1}
    assert parse_formula('Pb3Y4U10') == {'Pb': 3, 'Y': 4, 'U': 10}
    assert parse_formula('C2(H3U4)5O2') == {'C': 2, 'H': 15, 'U': 20, 'O': 2}
    assert (parse_formula("PO4H2(CH2)12CH3")) == {'P': 1, 'O': 4, 'H': 29, 'C': 13}


def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    assert molar_mass(parse_formula("H2O")) == approx(18.01528)
    assert molar_mass(parse_formula("C6H6")) == approx(78.11184)
    assert molar_mass(parse_formula("PO4H2(CH2)12CH3")) == approx(280.34072)


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["CSE 111 - W07 Milestone.py"])
