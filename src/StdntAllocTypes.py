## @file StdntAllocTypes.py
#  @brief Creates classes for different types
#  @author Matthew Braden
#  @date 2/11/2019

from SeqADT import *

## @brief Enumerated class of different genders
#  @details Class that contains genders related to a value
class GenT(enum):
    male = 0
    female = 1

## @brief Enumerated class of different departments
#  @details Class that contains departments related to a value
class DeptT(enum):
    civil = 0
    chemical = 1
    electrical = 2
    mechanical = 3
    software = 4
    materials = 5
    engphys = 6

## @brief NamedTuple class of different categories
#  @details Class that contains categories for student info with the data type
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT(DeptT)
    freechoice: bool
