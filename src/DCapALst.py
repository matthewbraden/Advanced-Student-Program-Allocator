## @file DCapALst.py
#  @brief Creates class for departments
#  @author Matthew Braden
#  @date 2/11/2019

from StdntAllocTypes import *

## @brief Class for departments list
#  @details Class that contains all information about the departments
class DCapALst:

    s = []
    ## @brief Initializes data
    #  @details Initializes the list of departments
    @staticmethod
    def __init__():
        DCapALst.s = []

    ## @brief Adds data
    #  @details Adds a department to the DCapALst
    #  @param d The DeptT from StdntAllocTypes
    #  @param n The capacity of the department
    @staticmethod
    def add(d, n):
        if (d, n) in DCapALst.s:
            raise KeyError
        DCapALst.s.append((d, n))

    ## @brief Removes data
    #  @details Removes a department from the DCapALst
    #  @param d The DeptT from StdntAllocTypes
    @staticmethod
    def remove(d):
        if (d, n) not in DCapALst.s:
            raise KeyError
        if (d, n) in DCapALst.s:
            DCapALst.s.remove((d, n))

    ## @brief Returns a bool
    #  @details Returns weather or not the department is in DCapALst
    #  @param d The DeptT from StdntAllocTypes
    @staticmethod
    def elm(d):
        return ((d, n) in DCapALst.s)

    ## @brief Returns the capacity
    #  @details Checks if department is in the DCapALst and returns capacity
    #  @param d The DeptT from StdntAllocTypes
    @staticmethod
    def capacity(d):
        if (d, n) not in DCapALst.s:
            raise KeyError
        if (d, n) in DCapALst.s:
            return n
