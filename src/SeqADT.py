## @file SeqADT.py
#  @brief Creates the Sequence data type
#  @author Matthew Braden
#  @date 2/11/2019

## @brief Class for the sequence of students
#  @details Class that contains start, next and end functions
class SeqADT:

    s = 0
    i = 0

    ## @brief Initializes data
    #  @details Initializes the sequence of students
    #  @param x Value of amount of students in sequence
    @staticmethod
    def __init__(x):
        SeqADT.s = x
        SeqADT.i = 0
        return SeqADT.s

    ## @brief Start of the sequence
    #  @details Starts the students sequence
    @staticmethod
    def start():
        SeqADT.i = 0

    ## @brief Next in sequence
    #  @details Returns a value of the next item in the sequence
    @staticmethod
    def next():
        if SeqADT.i  >= len(SeqADT.s):
            raise StopIteration
        SeqADT.i  += 1
        return SeqADT.s[SeqADT.i]

    ## @brief Ends the sequence
    #  @details Finishes the students sequence and returns a bool
    @staticmethod
    def end():
        return SeqADT.i >= len(SeqADT.s)
