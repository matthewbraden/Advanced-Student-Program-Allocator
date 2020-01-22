## @file test_All.py
#  @brief This tests the programs functions
#  @author Matthew Braden
#  @date 2/11/2019
import pytest

from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *
from Read import *

## @brief Class testing function
#  @details Test for the module SeqADT
class TestSeqADT:

    def test_next_sequence_function(self):
        seq = SeqADT([5, 6, 7, 8])
        assert seq.next() == 6

    def test_end_sequence(self):
        seq = SeqADT([10, 5, 6, 31])
        assert seq.end() == True

    def test_fail_for_start(self):
        seq = SeqADT([])
        assert seq.start() == None

    def test_next_sequence_fail(self):
        seq = SeqADT([])
        assert seq.next() == None

    def test_boundary_end(self):
        seq = SeqADT([])
        assert seq.end() == True

## @brief Class testing function
#  @details Test for the module DCapALst
class TestDCapALst:

    def test_raises_error_for_add(self):
        with pytest.raises(KeyError):
            DCapALst([[software, 100]]).add(DeptT.software, 100)

    def test_raises_error_for_remove(self):
        with pytest.raises(KeyError):
            DCapALst().remove(software, 100)

    def test_elm_function_boundary(self):
        dept = DCapALst()
        assert dept.elm() == True

    def test_elm_function(self):
        dept = DCapALst().add(DeptT.software, 100)
        assert dept.elm(software) == True

    def test_elm_to_fail(self):
        dept = DCapALst()
        assert dept.elm(software) == False

    def test_raises_error_for_capacity(self):
        while pytest.raises(KeyError):
            DCapALst().capacity(Software)

    def test_capacity_function(self):
        dept = DCapALst()
        assert dept.capacity(Software) == 100


## @brief Class testing function
#  @details Test for the module SALst
class TestSALst:

    def test_raises_error_for_add(self):
        with pytest.raises(KeyError):
            SALst([["student1", (brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True)]]).add("student1", (brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True))

    def test_raises_error_for_remove(self):
        with pytest.raises(KeyError):
            SALst().remove("student1")

    def test_for_elm(self):
        SAL = SALst().add("student1", (brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True))
        assert SAL.elm("student1") == True

    def test_for_elm_failures(self):
        SAL = SALst()
        assert SAL.elm("student1") == False

    def test_elm_boundary(self):
        SAL = SALst()
        assert dept.elm() == True

    def test_for_info_error(self):
        with pytest.raises(ValueError):
            SALst().info("student1")

    def test_for_get_gpa(self):
        gpa = SALst()
        assert gpa.get_gpa() == 0

    def test_for_sort(self):
        sort = SALst().sort((brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True), (smithj2, John, Smith, male, 7.0, [mechanical, electrical, materials, mechanical, electrical], False))
        assert sort == (smithj2, John, Smith, male, 7.0, [mechanical, electrical, materials, mechanical, electrical], False), (brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True)

    def test_for_allocate_boundary(self):
        alloc = SALst().allocate((brownc, Charlie, Brown, male, 3.9, [engphys, software, chemical, materials], True))
        assert not (alloc == [engphys: brownc])

    def test_for_average(self):
        ave = SALst()
        assert ave.average((brownc, Charlie, Brown, male, 6.0, [engphys, software, chemical, materials], True), (smithj2, John, Smith, male, 7.0, [mechanical, electrical, materials, mechanical, electrical], False)) == 6.5
        
