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

    def __init__(self, num_registers, num_customers, customers):
        self.time = 0
        self.customers = customers
        self.num_customers = num_customers
        self.num_registers = num_registers
        self.registers = []
        self._init_registers()

    def completion_time(self):
        print("Finished at: t={0} minutes".format(self.time))

    def process_customers(self):
        """ Processes the customers
        :return:
        """
        print(self.customers)

        while self.time != 8:
            self._update_registers()
            print ("num customers {0}".format(self.num_customers))
            print ("Time {0}".format(self.time))
            print (self.registers)
            if self.time in self.customers:
                print(self.customers[self.time])
                for customer in self.customers[self.time]:
                    self._queue_customer(customer)
            self.time += 1
        self.completion_time()
        #  should be cleared
        print(self.registers)

    def _queue_customer(self, customer):
        """ Logic for queueing customers based on number of items and type
        :param customer: (array)
        """

        print ("queue customer")
        # first come first serve customers should be ordered,
        # A takes precedence over B
        # find empty and shortest lines
        length, short_line = self._find_shortest_line()

        # length is zero means empty or criterion for queueing 'A' type
        if length == 0 or customer[1] is 'A':
            # queue up customer
            self.registers[short_line]['line'].appendleft(customer[0])
            # update pop_time for register if register is empty
            if length == 0:
                self._update_register(self.registers[short_line])
        else:
            # criterion for queueing up 'B' type
            least_items = self._find_last_customer_with_least_items()
            self.registers[least_items]['line'].appendleft(customer[0])

    def _init_registers(self):
        """ Hidden method to set up the cash registers including trainee """
        print ("initialize registers")
        for x in range(0, self.num_registers - 1):
            self.registers.append(create_register())
        # add trainee register
        self.registers.append(create_register(rate=2))

    def _update_register(self, register):
        """ Updates register based on time
        :param register: (dict)
        """
        print ("update register")
        if register['pop_time'] == self.time:
            register['line'].pop()
            self.num_customers -= 1

        if len(register['line']) == 0:
            register['pop_time'] = -1
        else:
            register['pop_time'] = \
                register['rate'] * int(register['line'][-1]) + self.time

    def _update_registers(self):
        """
        check time against the register's pop_times and if customer gets
        popped, decrement the number of customers to let us know when we're
        finished looping
        :return:
        """
        print ("update registers")
        for register in self.registers:
            self._update_register(register)

    def _find_shortest_line(self):
        """ Finds the first shortest line
        :return: (int, int)
        """
        print ("finding shortest line")
        length, shortest_line = min((len(register['line']), idx)
                                    for (idx, register)
                                    in enumerate(self.registers))
        return length, shortest_line

    def _find_last_customer_with_least_items(self):
        """ finds line whose last customer has the fewest items
        :return: (int)
        """
        print ("finding least items")
        length, least_items = min((register['line'][0], idx)
                                  for (idx, register)
                                  in enumerate(self.registers))
        return least_items


# Static method(s)

def create_register(rate=1):
    """ Creates a default register, chose dict over class for simplicities sake
    :param rate:
    :return:
    """
    return dict({'rate': rate, 'pop_time': -1, 'line': deque([])})
