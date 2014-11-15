from collections import deque


class GroceryStore(object):

    def __init__(self, num_registers):
        self.time = 0
        self.num_registers = num_registers
        self.registers = None

    def completion_time(self):
        print("Finished at: t={0} minutes".format(self.time))

    def _find_shortest_line(self):
        length, self.shortest_line = min((len(line), idx) for (idx, line)
                                         in enumerate(self.registers))
        return length, self.shortest_line

    def _find_last_customer_with_least_items(self):
        length, self.shortest_line = min((line[0], idx) for (idx, line)
                                         in enumerate(self.registers))

    def init_registers(self):
        """
        returns data structure model for registers using a dictionary of deques
        :param num_registers: int
        :return: dict
        """
        self.time = 0
        self.registers = [deque] * self.num_registers

    def process_customers(self, customers):

        self.init_registers()

        while True:

            self.time += 1



    # def _update_stats(self):
    #     # default number that is higher than number of registers
    #     self.shortest_line = self.num_registers +1
    #     self.fewest_items = self.num_registers +1
    #     self.empty_line = self.num_registers + 1
    #     for index, line in enumerate(self.registers):
    #         # find first empty list
    #         if not line:
    #             self.empty_line = index
    #         else:
    #             # find shortest line
    #             if self.shortest_line > len(line):
    #                 self.shortest_line = index
    #
    #         # find last customer with least items