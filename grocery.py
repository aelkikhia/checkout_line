
import sys

from collections import deque

"""
Type A always chooses shortest line, if tie, lowest register number

Type B always chooses  empty line or else be behind the customer with the
fewest number of items

Customers just finishing checking out do not count as being in line
(for either kind of customer).

arrival tie: fewest items, if tie on item num A then B

"""


def grocery(argv):
    """
    takes text file input first line is number of registers. All following
    lines are separated into three space divided columns in the order of
    (1)Customer type A/B (2) Line choosing time (3) number of items
    :param argv:
    :return:
    """
    # extract data from input file
    with open(sys.argv[1], 'r') as in_file:
        # get num registers
        num_registers = int(in_file.readline())

        customers = []
        # store and order the rest of the lines in the file...
        #TODO: generator seems out of the question.
        #TODO: data might not be in sequential order
        for line in in_file:
            line = line.split()
            customers.append(line)
    in_file.close()

    # set time variable
    time = 0

    # sort customers
    customers.sort(key=lambda s: (s[1], s[2], s[0]))

    # create registers
    registers = create_registers(num_registers)

    print (registers)
    print (customers)


def create_registers(num_registers):
    """
    returns data structure model for registers using a dictionary of deques
    :param num_registers: int
    :return: dict
    """
    return dict.fromkeys(range(1, 10), deque)


def checkout(num_items, rate=1):
    """
    checkout takes in number of items and the rate in which they are processed
    side note: put this in a function to save time in refactoring later.
    chose not to make a factory since memory could be factor in an
    large input file. interpreter will optimize this code

    :param num_items: number of items (int)
    :param rate: rate coefficient for processing each item (int)
    :return: checkout time in minutes(int)
    """
    return num_items * rate

if __name__ == "__main__":
    grocery(sys.argv[1])