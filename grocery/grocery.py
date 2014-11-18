import sys

from registers import Registers


def grocery(argv):

    # sort customers
    store = Registers()
    store.load_file(argv)
    store.process_customers()
    print("Finished at: t={0} minutes".format(store.get_time()))

if __name__ == "__main__":
    grocery(sys.argv[1])