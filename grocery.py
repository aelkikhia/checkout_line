
import sys

from models.models import Registers


def grocery(argv):
    num_registers, num_customers, customers = extract_data_from_file(argv)
    # sort customers
    store = Registers(num_registers, num_customers, customers)
    store.process_customers()
    # store.completion_time()


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
        num_customers = 0
        customers = dict()
        # store and order the rest of the lines in the file...
        #TODO: generator seems out of the question.
        #TODO: data might not be in sequential order
        for line in in_file:
            customer = line.split()
            if int(customer[1]) in customers:
                customers[int(customer[1])].append([customer[2], customer[0]])
            else:
                customers[int(customer[1])] = [[customer[2], customer[0]]]
            num_customers += 1
    in_file.close()

    return num_registers, num_customers, customers

if __name__ == "__main__":
    grocery(sys.argv[1])