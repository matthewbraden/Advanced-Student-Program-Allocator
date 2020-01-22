## @file SALst.py
#  @brief This edits a student allocated list
#  @author Matthew Braden
#  @date 2/11/2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *

## @brief Class for student allocation list
#  @details Class that contains student allocation functions
class SALst:

    s = []
    ## @brief Initializes data
    #  @details Initializes an empty list
    @staticmethod
    def __init__():
        SALst.s = []

    ## @brief Adds student data
    #  @details Adds a new student to the list
    #  @param m Student string
    #  @param i SInfoT
    @staticmethod
    def add(m, i):
        if (m, i) in SALst.s:
            raise KeyError
        SALst.s.append((m, i))

    ## @brief Removes student data
    #  @details Removes a student from SALst
    #  @param m String of students
    @staticmethod
    def remove(m):
        if (m, i) not in SALst.s:
            raise KeyError
        if (m, i) in SALst.s:
            SALst.s.remove((m, i))

    ## @brief Returns a bool
    #  @details Returns if a student is in SALst
    #  @param m String of students
    @staticmethod
    def elm(m):
        return ((m, i) in SALst.s)

    ## @brief Info student data
    #  @details Returns the information of students data
    #  @param m Students string
    @staticmethod
    def info(m):
        if (m, i) not in SALst.s:
            raise ValueError
        if (m, i) in SALst.s:
            return i

    ## @brief Sorts student data
    #  @details Adds a new student to the list
    #  @param f SInfoT
    @staticmethod
    def sort(f):
        sortLst = sorted(f, key = lambda s: SALst.s.get_gpa(m, s) , reverse = True)
        return sortLst
    #sorted line 63 was found from https://tinyurl.com/y9xdx4ep

    ## @brief Average the gpa
    #  @details Averages the gpa of genders
    #  @param f SInfoT
    @staticmethod
    def average(f):
        for ((m, i) in s) and f(i):
            if not i:
            raise ValueError
        sum = 0
        for ((m, i) in s) and f(i):
            fset = i
            for j in fset:
                sum += j.gpa
        ave = sum / len(fset)
        return ave

    ## @brief Allocates students
    #  @details Puts the students in one of their three choices
    @staticmethod
    def allocate():
        free = SALst.sort(f)
        if t.freechoice and (t.gpa >= 4.0):
            for m in free:
                ch = SALst.info(m).choices
                AALst.add_stdnt(ch.next(), m)

        student = SALst.sort(f)
        if (not t.freechoice) and (t.gpa >= 4.0):
            for m in student:
                ch = SALst.info(m).choices
                alloc = False
                while (not alloc) and (not ch.end()):
                    d = ch.next()
                    if (AALst.num_alloc(d)) < DCapALst.capacity(d):
                        AALst.add_stdnt(d, m)
                        alloc = True
                if not alloc:
                    raise RuntimeError

    ## @brief Gets gpa
    #  @details Returns the students gpa
    #  @param m String of students
    #  @param s List of data
    @staticmethod
    def get_gpa(m, s):
        if (m, i) in s:
            return i.gpa
