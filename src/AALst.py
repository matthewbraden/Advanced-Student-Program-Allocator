## @file AALst.py
#  @brief Creates class for allocation
#  @author Matthew Braden
#  @date 2/11/2019

from StdntAllocTypes import *

## @brief Class for allocation list
#  @details Class that contains allocation information
class AALst:

    s = []

    ## @brief Initializes data
    #  @details Initializes the list of departments
    @staticmethod
    def __init__():
        for d in DepT:
            AALst.s = (d, [])

    ## @brief Adds a student
    #  @details Adds a student to the AALst
    #  @param dep The DeptT from StdntAllocTypes
    #  @param m String of students
    @staticmethod
    def add_stdnt(d, m):
        for (d, L) in AALst.s:
            AALst.s.append((d, m))

    ## @brief Returns a string
    #  @details Returns a sequence of students as a string
    #  @param d The DeptT from StdntAllocTypes
    @staticmethod
    def lst_alloc(d):
        if (d, L) in AALst.s:
            return L

    ## @brief Returns a value
    #  @details Returns the number of students in a department
    #  @param d The DeptT from StdntAllocTypes
    @staticmethod
    def num_alloc(d):
        if (d, L) in AALst.s:
            return len(L)
