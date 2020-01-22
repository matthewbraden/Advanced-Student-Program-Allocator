## @file Read.py
#  @brief This edits a student allocated list
#  @author Matthew Braden
#  @date 2/11/2019

from DCapALst import *
from SALst import *

## @brief Loads students data
#  @details Reads students data from a file and puts it into a list
#  @param s Filename of file being used
def load_stdnt_data(s):
    file = open(s, "r")
    stdnt = file.read()
    stdnt = stdnt.replace(",", "")
    stdnt = stdnt.replace("[", "")
    stdnt = stdnt.replace("]", "")
    stdnt = stdnt.splitlines()
    file.close()
    SALst.__init__()
    stdnt_data = SALst.s
    for i in stdnt:
        stdnti = i.split()
        stdnt_lst = []
        for j in stdnti:
            stdnt_lst.append(j)
        stdnt_data.append(stdnt_lst)

## @brief Loads departments data
#  @details Reads departments data from a file and puts it into a list
#  @param s Filename of file being used
def load_dept_data(s):
    file = open(s, "r")
    dept = file.read()
    dept = dept.replace(",", "")
    dept = dept.splitlines()
    file.close()
    DCapALst.__init__()
    dept_data = DCapALst.s
    for i in dept:
        depti = i.split()
        dept_lst = []
        for j in depti:
            dept_lst.append(j)
        dept_data.append(dept_lst)
