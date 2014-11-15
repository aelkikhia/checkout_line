
import sys

from models.models import GroceryStore


def grocery(argv):
    """
    Type A always chooses shortest line, if tie, lowest register number

    Type B always chooses  empty line or else be behind the customer with the
    fewest number of items

    Customers just finishing checking out do not count as being in line
    (for either kind of customer).

    arrival tie: fewest items, if tie on item num A then B

    """

    num_registers, customers = extract_data_from_file(argv)

    # sort customers
    customers.sort(key=lambda s: (s[1], s[2], s[0]))

    # create registers
    store = GroceryStore(num_registers)
    store.init_registers()
    store.process_customers(customers)
    print(store.completion_time)


def extract_data_from_file(argv):
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
    return num_registers, customers

if __name__ == "__main__":
    grocery(sys.argv[1])