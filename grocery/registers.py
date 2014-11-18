
import sys
from collections import deque


class Registers(object):
    """
    Type A always chooses shortest line, if tie, lowest register number

    Type B always chooses empty line or else be behind the customer with the
    fewest number of items

    Customers just finishing checking out do not count as being in line
    (for either kind of customer).

    arrival tie: fewest items, if tie on item num A then B
    """

    def __init__(self):
        """ Constructor for cash registers """
        self.num_registers = 0
        self.num_customers = 0
        self.time = 0
        self.customers = dict()
        self.registers = []

    def load_file(self, argv):
        self.num_registers, self.num_customers, self.customers = \
            _extract_data_from_file()

    def get_time(self):
        """ Returns int time of the Registers
        :return: (int)
        """
        return self.time

    def process_customers(self):
        """ Processes the customers """

        # initialize registers before we rock and roll
        self._init_registers()

        while True:
            self._update_registers()
            if self.time in self.customers:
                for customer in self.customers[self.time]:
                    self._queue_customer(customer)
            if self.num_customers == 0:
                break
            self.time += 1

    def _queue_customer(self, customer):
        """ Logic for queueing customers based on number of items and type
        :param customer: (array)
        """

        length, short_line = self._find_shortest_line()

        # length is zero means empty or criterion for queueing 'A' type
        if length == 0 or customer[1] is 'A':
            # queue up customer
            self.registers[short_line]['line'].appendleft(customer[0])
            # update pop_time for register if register is empty
            if length == 0:
                self._reset_pop_time(self.registers[short_line])
        else:
            # criterion for queueing up 'B' type
            least_items = self._find_last_customer_with_least_items()
            self.registers[least_items]['line'].appendleft(customer[0])

    def _init_registers(self):
        """ set up the cash registers including trainee """
        for x in range(0, self.num_registers - 1):
            self.registers.append(_create_register())
        # add trainee register
        self.registers.append(_create_register(rate=2))

    def _update_register(self, register):
        """ Updates register based on time """
        if register['pop_time'] == self.time:
            register['line'].pop()
            self.num_customers -= 1
            self._reset_pop_time(register)

    def _reset_pop_time(self, register):
        """ Resets pop time if needed """
        if len(register['line']) == 0:
            register['pop_time'] = -1
        else:
            register['pop_time'] = \
                register['rate'] * register['line'][-1] + self.time

    def _update_registers(self):
        """ check time against the register's pop_times and if customer gets
        popped, decrement the number of customers to let us know when we're
        finished looping
        """
        for register in self.registers:
            self._update_register(register)

    def _find_shortest_line(self):
        """ Finds the first shortest line
        :return: (int, int)
        """
        length, shortest_line = min((len(register['line']), idx)
                                    for (idx, register)
                                    in enumerate(self.registers))
        return length, shortest_line

    def _find_last_customer_with_least_items(self):
        """ finds line whose last customer has the fewest items
        :return: (int)
        """
        length, least_items = min((register['line'][0], idx)
                                  for (idx, register)
                                  in enumerate(self.registers))
        return least_items

###########################################################################
# Static method(s)
###########################################################################


def _create_register(rate=1):
    """ Creates a default register, chose dict over class for simplicities sake
    :param rate: (int)
    :return: (dict)
    """
    return dict({'rate': rate, 'pop_time': -1, 'line': deque([])})


def _extract_data_from_file():
    """ takes text file input first line is number of registers. All following
    lines are separated into three space divided columns in the order of
    (1)Customer type A/B (2) Line choosing time (3) number of items
    :return: (int, int, dict)
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
                customers[int(customer[1])].append([int(customer[2]),
                                                    customer[0]])
            else:
                customers[int(customer[1])] = [[int(customer[2]), customer[0]]]
            num_customers += 1
    in_file.close()

    # sort by customer type
    for key in customers:
        customers[key].sort(key=lambda x: x[1])

    return num_registers, num_customers, customers
